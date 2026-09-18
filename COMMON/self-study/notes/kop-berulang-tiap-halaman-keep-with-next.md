# Dokumen Ujian Multi-Halaman: Kop Berulang, Section Break, Keep-With-Next

- Topik queue: "Dokumen ujian multi-halaman: kop berulang tiap halaman, section breaks, header/footer berbeda, keep-with-next agar soal+opsi tidak terpisah halaman"
- Claim: PC (yonat-PC) · Tanggal: 18 September 2026
- Konteks: menutup gap LRN-20260918-006 — file jadi sekolah "... OK Edit P" mengulang kop di tiap halaman (menyalin tabel body per halaman), sedangkan ujian_builder cuma menghasilkan 1 kop di awal. Sebelumnya belum ada metode python-docx yang teruji.

---

## Metode terverifikasi (uji live 18/9, python-docx 1.2.0 + render LibreOffice headless)

Skenario uji: dokumen kop 3×3 + 14 soal PG + section break → render → PDF 5 halaman → pymupdf.

### 1. Kop berulang tiap halaman = taruh di SECTION HEADER

```python
from docx.enum.section import WD_SECTION   # PENTING: bukan docx.enum.text!
header = doc.sections[0].header
header.is_linked_to_previous = False
kop = header.add_table(rows=3, cols=3, width=Inches(6.7))  # width WAJIB
```

- Hasil render: kop muncul persis di halaman 1–4 (semua halaman section 1), hilang di halaman 5 (section 2).
- Kalau kop sudah ada sebagai tabel body (dari template kop-methodist.docx), pindahkan ke header via XML: `copy.deepcopy(reason_source._tbl)` lalu sisip ke element header (append sebelum `w:p`/di awal `w:hdr`). Header TIDAK menampilkan tabel via `doc.tables` (cuma body) — bagus untuk builder yang iterasi tabel body.
- `width` argumen wajib; header v1.2.0 sudah mendukung `add_table` (tidak seperti rilis lama).

### 2. Keep-with-next agar soal+opsi tidak putus halaman

```python
q.paragraph_format.keep_with_next = True                  # soal
for lab in ("a","b","c","d"):
    o.paragraph_format.keep_with_next = (lab != "d")      # semua opsi kecuali opsi terakhir
```

- Hasil render: tiap halaman BERAKHIR persis di opsi `d` — tidak pernah putus di tengah opsi/antara soal-opsi.

### 3. Section break dengan header/footer sendiri

```python
sec2 = doc.add_section(WD_SECTION.NEW_PAGE)
sec2.header.is_linked_to_previous = False
sec2.header.paragraphs[0].text = "kop section 2 (beda)"
sec2.footer.is_linked_to_previous = False
```

- Hasil: section 2 punya header teks berbeda + footer sendiri (halaman 5 dengan teks "KOP BEDA...").
- `WD_SECTION` di-import dari `docx.enum.section` (ImportError bila dari `docx.enum.text`).

### 4. Repeat header row tabel (tblHeader) — utk tabel yang memotong ganti halaman

```python
def set_repeat_table_header(row):
    tr = row._tr; trPr = tr.get_or_add_trPr()
    el = OxmlElement('w:tblHeader'); el.set(qn('w:val'), 'true'); trPr.append(el)
```

- Dipakai bila ada tabel data panjang (mis. NIS/Nama per halaman), bukan untuk kop per halaman.

## Caveat

- Header tabel butuh `sec.header_distance` mencukupi kalau body padat (di Word body bisa menimpa header bila header tinggi & jarak kecil). Saat uji default 0.5" cukup (kop ~3 baris tanpa overlap).
- Render LibreOffice = quick-check cepat; ground truth layout tetap Word (LRN-20260918-001). Font/kerning beda dikit tapi posisi header/keep-next konsisten.

## Implikasi untuk ujian_builder.py

- Tambahkan opsi `--kop-header`: setelah membangun body (0 kop), pindahkan/salin tabel kop form 6×7 ke section header → semua halaman otomatis dapat kop tanpa duplikasi body.
- `doc.tables` lalu memuat hanya 1 tabel (yang body) — beda dari file jadi sekolah (2-3 tabel body karena menyalin kop per section) — tapi visual di Word identik.

## Referensi

- LRN-20260918-009 (ringkasan), LRN-20260918-006 (gap), LRN-20260918-004 (python-docx), LRN-20260918-001 (fidelity LO vs Word)
- python-docx header/footer API: https://python-docx.readthedocs.io/en/latest/user/hdrftr.html
- tblHeader via OxmlElement: github.com/python-openxml/python-docx issue #322 & StackOverflow "add the column headers on every page"