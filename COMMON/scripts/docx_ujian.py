import argparse
import os
import re
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn


FOLIO_W = Inches(8.5)
FOLIO_H = Inches(13)
FONT = "Times New Roman"
SIZE = Pt(11)


def set_run(run, bold=False, size=SIZE):
    """Set font ke Times New Roman + eastAsia (agar konsisten di Windows)."""
    run.font.name = FONT
    run.font.size = size
    run.bold = bold
    run.underline = False
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), FONT)
    rfonts.set(qn("w:hAnsi"), FONT)
    rfonts.set(qn("w:eastAsia"), FONT)


def p_add(doc, text="", bold=False, align=None, left=Inches(0.0), hanging=Inches(0.0),
          keep_with_next=False):
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.left_indent = left
    fmt.first_line_indent = -hanging if hanging else None
    fmt.space_before = Pt(0)
    fmt.space_after = Pt(0)
    fmt.line_spacing = 1.0
    if align is not None:
        p.alignment = align
    if keep_with_next:
        fmt.keep_with_next = True
    if text:
        set_run(p.add_run(text), bold=bold)
    return p


def validasi_nomor_urut(items):
    """Pastikan daftar soal/nomor urut (1..n). Mismatch -> raise."""
    for i, it in enumerate(items, 1):
        m = re.match(r"^(\d+)", it.strip())
        if m and int(m.group(1)) != i:
            raise ValueError(
                f"Nomor urut salah di urutan ke-{i}: '{it[:40]}...' (harus {i})"
            )


def doc_ujian(out, sekolah="SD SWASTA METHODIST-11",
              judul="PENILAIAN TENGAH SEMESTER GANJIL T.A. 2026/2027",
              info=None, bagian=("I. Pilih Jawaban yang Benar!", "II. Isilah Titik-Titik di Bawah Ini!"),
              soal=None, margin=(Inches(0.5), Inches(0.6), Inches(1), Inches(1))):
    """Buat dokumen ujian Folio 8.5x13'', TNR 11, spacing 1, tanpa Word.

    margin = (top, bottom, left, right). soal = list paragraph soal.
    """
    soal = soal or ["1. Contoh pertanyaan pertama?"]
    bagian = list(bagian) + [""] * (max(0, 1) if False else 0)
    if len(bagian) > 1:
        pass
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = FOLIO_W, FOLIO_H
    sec.top_margin, sec.bottom_margin, sec.left_margin, sec.right_margin = margin

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = SIZE
    nf = normal.paragraph_format
    nf.space_before = Pt(0)
    nf.space_after = Pt(0)
    nf.line_spacing = 1.0

    # Kop (contoh; sesuaikan kebutuhan)
    p_add(doc, "YAYASAN PENDIDIKAN METHODIST MEDAN", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    p_add(doc, sekolah, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, keep_with_next=True)
    p_add(doc, judul, align=WD_ALIGN_PARAGRAPH.CENTER, keep_with_next=True)
    if info:
        p_add(doc, info, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Soal: hanging indent 0.65" (seperti spesifikasi ujian di MASTER-MEMORY)
    groups = re.split(r"(?=^\d+\.)", "".join(soal).strip(), flags=re.M)
    groups = [g for g in groups if g.strip()]
    j = 0
    for g in groups:
        if j < len(bagian) and g.strip().startswith("1.") and bagian[j]:
            if j:
                pass
        j += 1

    for b in [x for x in bagian if x and x.strip()]:
        p_add(doc, b, bold=True, keep_with_next=True)
        # paragraf soal hingga bertemu bagian berikutnya / habis
    # gabung dua-dua saja via mapping bagian -> jumlah
    if len(bagian) == len(soal):
        for b, txt in zip(bagian, soal):
            p_add(doc, b, bold=True, keep_with_next=True)
            for line in txt.split("\n"):
                p_add(doc, line, left=Inches(0.65), hanging=Inches(0.65))
    else:
        # fallback: bagian tunggal
        p_add(doc, bagian[0], bold=True, keep_with_next=True)
        for item in soal:
            for line in item.split("\n"):
                p_add(doc, line, left=Inches(0.65), hanging=Inches(0.65))

    doc.save(out)
    return out


def main():
    ap = argparse.ArgumentParser(description="Template dokumen ujian python-docx (tanpa Word COM)")
    ap.add_argument("--out", default="ujian.docx")
    ap.add_argument("--info", default=None, help="baris info mapel/kelas/waktu")
    ap.add_argument("--soal", nargs="+", required=True, help="daftar item soal (tiap item bisa multi-baris, baris opsi a/b/c/d larut)")
    args = ap.parse_args()
    out = doc_ujian(args.out, info=args.info, soal=args.soal)
    print("SAVED", os.path.abspath(out))


if __name__ == "__main__":
    main()