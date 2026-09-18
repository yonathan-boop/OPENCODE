# Format Soal Ujian di Word: PG (a-d) & Isian/Essay dari Sumber Campuran

- Topik queue: "Format soal Pilihan Ganda (a-d) & isian/essay di Word dari sumber campuran (.doc/.docx/.txt): indentasi-tab konsisten, gambar/equation di dalam soal, batas python-docx vs Word COM (terkait ujian_builder.py)"
- Claim: PC (yonat-PC) · Tanggal: 18 September 2026
- Konteks: user selalu minta dokumen ujian rapi dari soal guru yang berantakan; hasil kerja dibangun menjadi tool `COMMON/scripts/ujian_builder.py`.

---

## Best practice format soal ujian di Word

- **Penomoran soal:** pakai numbered list (outline numbering) biar otomatis & rapi — di ujian_builder cukup tulis `"N.\t<teks>"` dengan tab stop; tab membuat angka rata kiri & teks rapi di kolom yang sama (contoh sekolah: nomor di x≈72, teks di x≈89).
- **Opsi a-d:** diletakkan di bawah soal dengan indent lebih dalam (2× indent soal) + tab; huruf `a.` dipertahankan, bukan dibuang. Keep huruf label di baris sendiri per opsi.
- **Anti soal/opsi terpisah halaman:** set `keep_with_next` pada paragraf soal + tiap opsi (dan header bagian), plus `keep_with_next` header→soal. Ini lazy, tanpa tabel.
- **Header bagian** (A./B./Isian/Essay): deteksi via awalan kata kunci + huruf besar A-C / angka romawi; hati-hati "A." besar vs opsi "a." kecil — bedakan case-sensitive (lama regex `\b` gagal di "." + spasi, dan case-insensitive menelan opsi a-d → 2 bug nyata yang ditemukan hari ini).
- **Jangan pernah mengetik `•`/`1.` literal** → pakai label + tab manual (pola sekolah), atau style List Bullet/List Number (harus ada di template).

## Temuan ujian_builder.py (teruji di PC 18/9)

- Input: `.docx`, `.doc` (auto-convert via LibreOffice headless), `.txt` plain. Output: 1 kop form 6×7 terisi (Mata Pelajaran/Hari/Kelas/NIS-Nama) + soal bernomor ulang per bagian, format Folio TNR 11 mengikuti contoh "OK Edit P" yang disetujui user.
- Terbukti valid (Gemini vision render PDF): PG 2 bagian, 4 soal, opsi a-d rapi, "siap cetak".
- Bug yang sempat ditemukan & diperbaiki:
  1. `strip_num`/`strip_opt` mengiris `text[m.end():]` padahal regex punya `(.*)$` → hasil selalu kosong. Gunakan `m.group(2)`.
  2. Header "A. Pilihan Ganda" terdeteksi sebagai opsi karena `\b` gagal setelah "." + regex case-insensitive. Solusi: fungsi `is_header()` eksplisit (tolak yang bernomor/ber-opsi dulu, baru cek kata kunci & huruf besar).
  3. File kerja bernama `inspect.py` membayangi stdlib lxml. Rename.
  4. `body.append(tabel)` meletakkan tabel setelah `sectPr` → dokumen korup. Pakai `sectPr.addprevious(el)`.
- Keterbatasan yang DISADARI, belum diselesaikan:
  - Struktur di dalam tabel data (kolom NIS/Nama per baris) buat soal dalam tabel — ujian_builder tidak merestrukturisasi isi tabel berisi, hanya tabel kop yang dibuang/pertahankan.
  - Soal bergambar (OLE/equation MathType) via `.doc` lama: LibreOffice mengubah OMML → objek/gambar; python-docx tidak paham oMath → `p.text` tidak melihat equation. Untuk soal campuran gambar/equation, ground truth & edit final tetap pakai Word (COM) atau edit via XML (lihat bagian bawah).

## Batas python-docx vs Word COM (gambar/equation)

- **python-docx** (v1.2.0 terpasang): aman & cukup utk teks/format/nomor — tanpa ghost WINWORD & tanpa lock OneDrive. TIDAK punya API oMath: equation tetap tersimpan utuh di XML (jangan diubah), tapi tidak terbaca melalui `paragraph.text`.
- **Word COM**: satu-satunya cara andal utk dokumen yang dimodifikasi dengan equation/gambar yang harus layout-akurat (page-break, tabel, equation — lihat LRN-20260918-001).
- **Konversi .doc (lama) → .docx via LibreOffice:**
  - OMML equation dari .docx → ke .doc lalu kembali → diubah jadi gambar (LibreOffice docxexport/import).
  - Equation di .doc lama umumnya berupa objek MathType/Equation Editor → hasil konversi tidak pasti (berubah menjadi gambar/objek atau hilang detail).
  - Saran pakai untuk kecepatan: convert pakai LibreOffice hanya jika soal dominan teks; kalau banyak equation/gambar → minta versi .docx dari guru atau edit di Word saja.
  - Gambar `inline` paling portabel (floating anchor bisa loncat posisi).
- **Verifikasi layout:** loop penyemak visual (LRN-20260917-002): LibreOffice headless → PDF → pymupdf PNG (dpi≥150) → Gemini vision. Ingat: render LO ≠ Word persis (LRN-20260918-001), jadinya quick-check.

## Rekomendasi ke depan

1. Perluas `--check` agar membandingkan output vs contoh "OK Edit P" (pixel/teks) otomatis untuk KPU (kop lengkap, nomor urut, tidak ada teks potong).
2. Untuk sumber `.doc` yang isinya gambar/equation banyak: pesan ke user — minta dokumen dalam .docx (atau biarkan Word COM untuk merge).
3. Kalau kelak dipakai guru di komputer lain (tanpa Python/LibreOffice): bungkus exe (PyInstaller) — baru setelah workflow stabil di PC.

## Referensi

- Tool: `COMMON/scripts/ujian_builder.py` · kop: `COMMON/scripts/kop-methodist.docx` · verifier: `COMMON/scripts/check_visual.py`
- Contoh jadi sekolah: `@backup` + "… OK Edit P.docx" di `\\192.168.136.1\Methodist-11 Document\SOAL UJIAN\Soal Ujian UTS 1 T.P. 2026-2027\`
- LRN terkait: LRN-20260918-004 (python-docx) · LRN-20260917-002 (penyemak visual) · LRN-20260918-001 (fidelity LO vs Word)