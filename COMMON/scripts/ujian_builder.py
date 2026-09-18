#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ujian_builder.py - Rombakan docx_ujian.py jadi workflow nyata "soal mentah guru -> dokumen ujian rapi".

Nyambung ke bahan yang sudah ada:
  - Kop : COMMON/scripts/kop-methodist.docx (form identitas SD SWASTA METHODIST-11, 6x7)
  - Sumber: file .docx / .doc (auto-convert via LibreOffice) / .txt di @backup guru
  - Format target: mengikuti contoh hasil DISETUJUI ("Agama 6 ... OK Edit P", "Matematika 6 ... OK P")
      TNR 11, line spacing 276 (1.15), indent kiri/hanging 284 twips (~0.2"),
      nomor literal per bagian (auto-reset tiap section), header bagian bold.

Cara pakai:
  py ujian_builder.py --soal "path/soal.doc" [--mapel "Agama"] [--kelas "VIB SD"]
      [--hari "Selasa, 15 September 2026"] [--out "out.docx"] [--check]

  --soal   .docx/.doc/.txt. .doc dikonversi dulu via LibreOffice headless ke temp.
  --mapel/--kelas/--hari  diisi ke form kop (kosongkan -> dibiarkan sesuai template).
  --check  render PDF + hitung halaman + jalankan check_visual.py (Gemini vision).
  --no-norenum  kalau soal sudah bernomor literal dan mau DIPERTAHANKAN apa adanya.

Catatan validasi: nomor urut per bagian otomatis 1..n (standar sekolah). Kalau sumber bernomor
tidak urut, warning ditampilkan. Tabel yang isinya form identitas (Mata Pelajaran/NIS) dibuang;
tabel data soal (mis. tabel latihan B. Inggris) dipertahankan. Page-break eksplisit di sumber
=> halaman baru diawali kop lagi (pola lembar per halaman).
"""

import argparse
import copy
import os
import re
import shutil
import subprocess
import sys
import tempfile

from docx import Document
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.shared import Pt, Twips

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_KOP = os.path.join(SCRIPT_DIR, "kop-methodist.docx")
SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

FONT = "Times New Roman"
SIZE = Pt(11)
TW = 20  # 1 twip = 1/20 pt
LINE = 276          # line spacing 1.15 (seperti contoh OK Edit P)
IND_L = 284         # left indent twips
IND_H = 284         # hanging twips
HDR_BEFORE = 360    # pt/20 -> 18pt
HDR_AFTER = 60      # pt/20 -> 3pt

HEADER_WORDS = ("isian", "isi", "essay", "uraian", "urian", "pilihan ganda",
                "pilgan", "pg", "menjodohkan", "bacaan", "isilah", "jawablah",
                "berilah", "kerjakan", "cp")
NUM_RE = re.compile(r"^\s*(\d{1,3})[\.\)]\s*(.*)$")
OPT_RE = re.compile(r"^\s*([a-d])[\.\)]\s*(.*)$")
HDR_BAGIAN_RE = re.compile(r"^[Bb]agian\s+([A-Za-z]|\d|[IVX])[\.\)]?\s")
BLANK_RE = re.compile(r"[_\.]{2,}\s*$")  # baris isian berujung kosong (________)


def is_header(text):
    t = text.strip()
    if not t:
        return False
    if NUM_RE.match(t):          # bernomor -> soal, bukan header
        return False
    if OPT_RE.match(t):          # opsi a-d -> bukan header
        return False
    if HDR_BAGIAN_RE.match(t):   # "Bagian A/B/I/1" -> header seksi
        return True
    low = t.lower()
    if low.startswith(("bagian ", "bagian\t")):   # kalimat "Bagian luar mata..." BUKAN header
        return False
    if low.startswith(HEADER_WORDS):
        return True
    if re.match(r"^[A-C][\.\)\s]", t) or re.match(r"^[IVX]+[\.\)\s]", t):
        return True
    return False


def classify(text):
    if is_header(text):
        return "header"
    if NUM_RE.match(text):
        return "q"
    if OPT_RE.match(text):
        return "opt"
    return "plain"


def strip_num(text):
    m = NUM_RE.match(text)
    return m.group(2).strip() if m else text


def strip_opt(text):
    m = OPT_RE.match(text)
    return m.group(2).strip() if m else text


KOP_LABELS = ("Mata Pelajaran", "Hari", "Kelas", "Nomor", "Nama", "NIS", "Nilai")


def warn(msg):
    print("WARN:", msg, file=sys.stderr)


def convert_doc(path, tmpdir):
    """Konversi .doc -> .docx via LibreOffice headless. Return path docx hasil."""
    outdir = os.path.join(tmpdir, "lo")
    os.makedirs(outdir, exist_ok=True)
    subprocess.run([SOFFICE, "--headless", "--nologo", "--convert-to", "docx",
                    "--outdir", outdir, path],
                   check=False, capture_output=True)
    base = os.path.splitext(os.path.basename(path))[0]
    cand = os.path.join(outdir, base + ".docx")
    if not os.path.exists(cand):
        # LibreOffice kadang menambah akhiran; cari .docx di outdir
        hits = [f for f in os.listdir(outdir) if f.lower().endswith(".docx")]
        if not hits:
            raise RuntimeError("Gagal konversi .doc -> .docx: " + path)
        hits.sort(key=lambda f: os.path.getmtime(os.path.join(outdir, f)))
        cand = os.path.join(outdir, hits[-1])
    return cand


def load_source(path):
    """Kembalikan (ext, list_items, srcdoc).
    items: ('p', text, page_break, has_num, element) | ('tbl', elem).
    srcdoc: Document sumber (utk remap gambar), None bila .txt."""
    ext = os.path.splitext(path)[1].lower()
    items = []
    if ext == ".txt":
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                items.append(("p", line.rstrip("\n").rstrip("\r"), False, False, None))
        return ext, items, None
    tmpdir = tempfile.mkdtemp(prefix="ujian_builder_")
    work = path
    if ext == ".doc":
        work = convert_doc(path, tmpdir)
    doc = Document(work)
    for child in doc.element.body.iterchildren():
        tag = child.tag.split("}")[-1]
        if tag == "tbl":
            items.append(("tbl", copy.deepcopy(child)))
        elif tag == "p":
            from docx.text.paragraph import Paragraph
            p = Paragraph(child, doc)
            text = p.text
            page_break = any(
                br.get(qn("w:type")) == "page"
                for br in child.iter(qn("w:br"))
            )
            ppr = child.find(qn("w:pPr"))
            has_num = ppr is not None and ppr.find(qn("w:numPr")) is not None
            items.append(("p", text, page_break, has_num, child))
    return ext, items, doc


def is_kop_table(tbl):
    """Tabel berisi form identitas (label khas kop) -> dibuang dari konten."""
    from docx.table import Table
    t = Table(tbl, None)
    text = " ".join(c.text for row in t.rows for c in row.cells)
    if not re.search(r"(SD|SMP)\s+SWASTA", text):
        return False
    return any(lbl in text for lbl in KOP_LABELS)


def set_run(run, size=SIZE):
    run.font.name = FONT
    run.font.size = size
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(a), FONT)


def add_par(doc, text="", bold=False, before=0, after=60, indent=(IND_L, IND_H),
            page_break_before=False, keep_with_next=False):
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.line_spacing = LINE / 240.0  # 276 twips line -> 1.15
    fmt.space_before = Twips(before)
    fmt.space_after = Twips(after)
    if indent:
        fmt.left_indent = Twips(indent[0])
        fmt.first_line_indent = Twips(-indent[1])
    if page_break_before:
        fmt.page_break_before = True
    if keep_with_next:
        fmt.keep_with_next = True
    if text:
        r = p.add_run(text)
        r.bold = bold
        set_run(r)
    return p


def clone_para(p_src):
    """Clone paragraph XML, strip numbering, kembalikan element baru."""
    el = copy.deepcopy(p_src._p)
    npr = el.find(qn("w:pPr"))
    if npr is not None:
        for tag in ("w:numPr", "w:ind"):
            e = npr.find(qn(tag))
            if e is not None:
                npr.remove(e)
    return el


def fill_kop_field(tbl, label, value):
    """Isi sel nilai berdasarkan label (mis. 'Mata Pelajaran', 'Hari/Tgl', 'Kelas')."""
    if not value:
        return
    from docx.table import Table
    t = Table(tbl, None)
    for row in t.rows:
        cells = row.cells
        if len(cells) < 5:
            continue
        cell_label = cells[2].text.strip() if len(cells) >= 3 else ""
        if not cell_label:
            continue
        label_norm = re.sub(r"\s+", " ", label).strip().lower()
        cell_norm = re.sub(r"\s+", " ", cell_label).lower()
        if label_norm in cell_norm or cell_norm == label_norm:
            tgt = cells[4]
            runs = tgt.paragraphs[0].runs
            if runs:
                runs[0].text = value
                for extra in runs[1:]:
                    extra._element.getparent().remove(extra._element)
            else:
                tgt.text = value
            return


def apply_kop_unit(tbl, unit):
    """Ganti 'SD SWASTA' -> '<unit> SWASTA' di semua sel kop (utk SMP dsb)."""
    from docx.table import Table
    if not unit or unit.strip().lower() in ("sd", ""):
        return
    t = Table(tbl, None)
    for row in t.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in p.runs:
                    if "SD SWASTA" in r.text:
                        r.text = r.text.replace("SD SWASTA", unit.strip() + " SWASTA")


def get_kop_table(path):
    tpl = Document(path)
    tbl = copy.deepcopy(tpl.tables[0]._tbl)
    return tbl, tpl


def _relink_blips(doc, element, relmap):
    """Sambungkan ulang tiap gambar (blip) ke part baru di dokumen hasil."""
    import io
    for blip in element.iter(qn("a:blip")):
        embed = blip.get(qn("r:embed"))
        if embed and embed in relmap:
            part = relmap[embed]
            try:
                new_id, _ = doc.part.get_or_add_image(io.BytesIO(part.blob))
            except Exception:
                continue
            blip.set(qn("r:embed"), new_id)


def remap_kop_images(doc, tpl, tbl):
    """Salin part gambar kop dari file template ke dokumen hasil (fix logo rusak)."""
    relmap = {rid: p for rid, p in tpl.part.related_parts.items()
              if p.partname is not None and "media" in str(p.partname)}
    _relink_blips(doc, tbl, relmap)


def remap_images(doc, src_doc, element):
    """Remap SEMUA gambar dalam element ke dokumen hasil (fix rId menggantung)."""
    if src_doc is None:
        return
    relmap = {rid: p for rid, p in src_doc.part.related_parts.items()
              if p.partname is not None and "media" in str(p.partname)}
    _relink_blips(doc, element, relmap)


def _strip_leading_number(el):
    """Hapus nomor literal lama di awal paragraf (mis. '1. ' / 'a) ') agar bisa di-renum."""
    for r in el.findall(qn("w:r")):
        ts = r.findall(qn("w:t"))
        if not ts:
            continue
        joined = "".join(t.text or "" for t in ts)
        if joined.strip() == "":
            continue
        m = NUM_RE.match(joined)
        if m is None:
            m = OPT_RE.match(joined)
        if m is not None:
            new_text = m.group(2).strip()
            ts[0].text = new_text
            for extra in ts[1:]:
                r.remove(extra)
        return


def clone_runs(doc, p_el, label=None, indent=(IND_L, IND_H), bold=False,
               page_break_before=False, keep_with_next=False, before=0, after=60):
    """Salin paragraf SUMBER apa adanya (teks+gambar+rumus), rapikan nomornya."""
    from docx.text.paragraph import Paragraph
    el = copy.deepcopy(p_el)
    oldppr = el.find(qn("w:pPr"))
    if oldppr is not None:
        el.remove(oldppr)
    # buang leading number & tab/space kosong di depan, sisipkan label baru
    if label is not None:
        _strip_leading_number(el)
        while len(el) and el[0].tag == qn("w:r"):
            joined = "".join(t.text or "" for t in el[0].findall(qn("w:t")))
            if joined.strip() == "":
                el.remove(el[0])
            else:
                break
        r = el.makeelement(qn("w:r"), {})
        t = el.makeelement(qn("w:t"), {})
        t.text = label
        r.append(t)
        el.insert(0, r)
    p = Paragraph(el, doc)
    fmt = p.paragraph_format
    fmt.line_spacing = LINE / 240.0
    fmt.space_before = Twips(before)
    fmt.space_after = Twips(after)
    if indent:
        fmt.left_indent = Twips(indent[0])
        fmt.first_line_indent = Twips(-indent[1])
    if page_break_before:
        fmt.page_break_before = True
    if keep_with_next:
        fmt.keep_with_next = True
    body = doc.element.body
    sectPr = body.find(qn("w:sectPr"))
    sectPr.addprevious(el)
    return el


def build(out, kop_tbl, items, mapel=None, kelas=None, hari=None, unit="SD",
          renum=True, margin=(0.20, 0.24, 0.39, 0.39), kop_tpl=None, src_doc=None):
    doc = Document()
    if kop_tpl is not None:
        remap_kop_images(doc, kop_tpl, kop_tbl)
    sec = doc.sections[0]
    sec.page_width = Twips(8.5 * 1440)
    sec.page_height = Twips(13.0 * 1440)
    sec.top_margin = Twips(int(margin[0] * 1440))
    sec.bottom_margin = Twips(int(margin[1] * 1440))
    sec.left_margin = Twips(int(margin[2] * 1440))
    sec.right_margin = Twips(int(margin[3] * 1440))

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = SIZE
    nf = normal.paragraph_format
    nf.space_before = Pt(0)
    nf.space_after = Pt(0)
    nf.line_spacing = 1.15

    fill_kop_field(kop_tbl, "Mata Pelajaran", mapel)
    fill_kop_field(kop_tbl, "Hari/Tgl", hari)
    fill_kop_field(kop_tbl, "Kelas", kelas)
    apply_kop_unit(kop_tbl, unit)

    body = doc.element.body
    sectPr = body.find(qn("w:sectPr"))

    def put_kop():
        # kop_tbl sudah terisi -> copy yang sudah jadi, sisipkan SEBELUM sectPr
        sectPr.addprevious(copy.deepcopy(kop_tbl))

    put_kop()

    section_count = 0
    total_q = 0
    total_hdrs = 0
    n = 0          # nomor berjalan dalam section
    section_open = False

    def new_section():
        nonlocal n, section_open
        section_open = True
        n = 0

    for item in items:
        kind = item[0]
        if kind == "tbl":
            if is_kop_table(item[1]):
                continue  # kop mentah, ganti standar
            section_open = True
            tbl_el = copy.deepcopy(item[1])
            remap_images(doc, src_doc, tbl_el)
            sectPr.addprevious(tbl_el)
            continue
        text, page_break, has_num, el = item[1], item[2], item[3], item[4]
        has_image = el is not None and next(el.iter(qn("w:drawing")), None) is not None
        if has_image:
            # paragraf berisi gambar -> salin apa adanya (gambar terjaga), rapikan nomor
            cls = classify(text) if text.strip() else ("q" if has_num else "plain")
            if cls == "header":
                total_hdrs += 1
                new_section()
                el = clone_runs(doc, el, label=None, before=HDR_BEFORE, after=HDR_AFTER,
                                indent=None, page_break_before=page_break, keep_with_next=True)
                remap_images(doc, src_doc, el)
                continue
            if cls == "q" or (cls == "plain" and (has_num or BLANK_RE.search(text))):
                if renum:
                    n += 1
                    if has_num and not text.strip():
                        label = "%d." % n
                        warn("soal berisi gambar (tanpa teks) di nomor %d" % n)
                    else:
                        label = "%d." % n
                else:
                    m = NUM_RE.match(text)
                    label = (m.group(1) + ".") if m else (str(n + 1) + ".")
                total_q += 1
                el = clone_runs(doc, el, label=label + "\t" if not text.strip() else label,
                                page_break_before=page_break, keep_with_next=True)
                remap_images(doc, src_doc, el)
                continue
            if cls == "opt":
                letter = (OPT_RE.match(text).group(1) if text.strip() else "")
                el = clone_runs(doc, el, label=("%s." % letter) + "\t", indent=(IND_L * 2, IND_H),
                                keep_with_next=True)
                remap_images(doc, src_doc, el)
                continue
            el = clone_runs(doc, el, label=None, page_break_before=page_break)
            remap_images(doc, src_doc, el)
            continue
        if not text.strip():
            continue
        cls = classify(text)
        if cls == "header":
            total_hdrs += 1
            new_section()
            add_par(doc, text.strip(), bold=True, before=HDR_BEFORE, after=HDR_AFTER,
                    indent=None, page_break_before=page_break, keep_with_next=True)
            continue
        if cls == "q" or (cls == "plain" and (has_num or BLANK_RE.search(text))):
            raw = strip_num(text)
            if renum:
                n += 1
                label = "%d." % n
                if not raw:
                    warn("soal kosong di nomor %d: %r" % (n, text))
            else:
                m = NUM_RE.match(text)
                label = (m.group(1) + ".") if m else (str(n + 1) + ".")
            total_q += 1
            add_par(doc, label + "\t" + raw, bold=False, page_break_before=page_break,
                    keep_with_next=True)
            continue
        if cls == "opt":
            m = OPT_RE.match(text)
            letter = m.group(1) if m else ""
            rest = strip_opt(text)
            add_par(doc, "%s.\t%s" % (letter, rest), bold=False,
                    indent=(IND_L * 2, IND_H), keep_with_next=True)
            continue
        # plain: instruksi/teks pengantar
        add_par(doc, text.strip(), bold=False, page_break_before=page_break)

    if not section_open:
        new_section()  # minimal satu section agar rekap nomor valid

    # tab stop pada posisi hanging (agar nomor bertab lurus)
    from docx.enum.text import WD_TAB_ALIGNMENT
    for p in doc.paragraphs:
        if p.paragraph_format.left_indent is not None:
            try:
                p.paragraph_format.tab_stops.add_tab_stop(Twips(IND_L), WD_TAB_ALIGNMENT.LEFT)
            except Exception:
                pass

    doc.save(out)
    return {"sections": total_hdrs, "questions": total_q}


def render_pdf(pdf_out, docx_path, tmpdir):
    subprocess.run([SOFFICE, "--headless", "--nologo", "--convert-to", "pdf",
                    "--outdir", tmpdir, docx_path],
                   check=True, capture_output=True)
    base = os.path.splitext(os.path.basename(docx_path))[0]
    src_pdf = os.path.join(tmpdir, base + ".pdf")
    if not os.path.exists(src_pdf):
        raise RuntimeError("Render PDF gagal: " + docx_path)
    shutil.move(src_pdf, pdf_out)
    return pdf_out


def count_pages(pdf_path):
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    with pymupdf.open(pdf_path) as d:
        return d.page_count


def do_check(docx_path):
    tmp = tempfile.mkdtemp(prefix="ujian_check_")
    pdf_path = os.path.join(tmp, os.path.basename(docx_path).replace(".docx", ".pdf"))
    render_pdf(pdf_path, docx_path, tmp)
    pages = count_pages(pdf_path)
    print("PAGES:", pages)
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    pngdir = os.path.join(tmp, "png")
    os.makedirs(pngdir, exist_ok=True)
    d = pymupdf.open(pdf_path)
    n = min(pages, 2)  # cukup 1-2 halaman pertama
    for i in range(n):
        d[i].get_pixmap(dpi=150).save(os.path.join(pngdir, "page%d.png" % (i + 1)))
    d.close()
    script = os.path.join(SCRIPT_DIR, "check_visual.py")
    pngs = sorted(os.listdir(pngdir))
    if len(pngs) == 1:
        target = os.path.join(pngdir, pngs[0])
        args = [sys.executable, script, target,
                "Periksa dokumen ujian ini: apakah kop form di atas lengkap, "
                "nomor soal urut, teks tidak terpotong/bertabrakan, layout rapi?"]
    else:
        args = [sys.executable, script, "--dir", pngdir,
                "Periksa dokumen ujian ini: apakah kop form di atas lengkap, "
                "nomor soal urut, teks tidak terpotong/bertabrakan, layout rapi?"]
    sys.exit(subprocess.run(args, capture_output=False).returncode)


def main():
    ap = argparse.ArgumentParser(description="Generator dokumen ujian rapi dari soal mentah guru")
    ap.add_argument("--soal", required=True, help="sumber soal: .docx / .doc / .txt")
    ap.add_argument("--kop", default=DEFAULT_KOP, help="template kop (default kop-methodist.docx)")
    ap.add_argument("--mapel", default=None)
    ap.add_argument("--kelas", default=None)
    ap.add_argument("--hari", default=None)
    ap.add_argument("--unit", default="SD",
                    help="unit sekolah utk kop: SD/SMP (mengganti teks 'SD SWASTA')")
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-renum", action="store_true",
                    help="pertahankan nomor literal dari sumber, jangan renomer")
    ap.add_argument("--check", action="store_true",
                    help="setelah jadi: render PDF, hitung halaman, cek visual via Gemini")
    args = ap.parse_args()

    kop_tbl, kop_tpl = get_kop_table(args.kop)
    _, items, src_doc = load_source(args.soal)

    mapel = args.mapel
    kelas = args.kelas
    hari = args.hari
    if not args.out:
        # Konvensi sekolah: tambahkan status " Edit" saja (OK=diperiksa, Edit=diedit, P=di-print)
        base = os.path.splitext(os.path.basename(args.soal))[0]
        src_dir = os.path.dirname(os.path.abspath(args.soal))
        args.out = os.path.join(src_dir, base + " Edit.docx")

    stats = build(args.out, kop_tbl, items, mapel=mapel, kelas=kelas, hari=hari,
                  unit=args.unit, renum=not args.no_renum, kop_tpl=kop_tpl, src_doc=src_doc)

    print("SAVED:", os.path.abspath(args.out))
    print("SEKSI:", stats["sections"], "SOAL:", stats["questions"])
    if args.check:
        do_check(args.out)


if __name__ == "__main__":
    main()