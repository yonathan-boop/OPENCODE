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

## DUKUNGAN GAMBAR DALAM SOAL (implementasi 18/9, teruji live)

Builder kini MEMPERTAHANKAN gambar di dalam soal (sebelumnya DROP senyap).
- **Deteksi:** paragraf dianggap ber-gambar jika `next(el.iter(qn("w:drawing")), None)` — cari REKURSIF (gambar inline `p>r>drawing`; jangan `el.find` direct-child → pasti miss). Catat: `any(el.iter(...))` memicu FutureWarning lxml (truth-test elemen) → pakai `next(..., None) is not None`.
- **Clone paragraf:** sumber `.docx` di-`deepcopy` per elemen `w:p` (teks+gambar+rumus utuh), `pPr` lama dibuang, nomor lama dihapus dari run pertama ber-teks, label `"N.\t"` di-insert run baru di depan, format indent/hanging/tab diterapkan di klon. Fungsi `clone_runs()` mengembalikan elemen hasil → remap gambar.
- **Remap gambar = rahasia utama:** `doc.part.relate_to(part, RT.IMAGE)` langsung DARI part sumber → **Duplicate name 'word/media/image1.png'** karena part sumber & kop punya partname sama → zipfile peringatan + gambar kacau. Fix: baca `part.blob` → `doc.part.get_or_add_image(io.BytesIO(blob))` (kembali `(rId, image)`; spek namanya unik per paket). Terapkan ke BLIP dgn `relmap = {rid: p for rid,p in part.related_parts.items() if 'media' in str(p.partname)}` + `set(qn("r:embed"), new_id)`. `remap_images(doc, src_doc, element)` dipanggil utk tiap elemen yang disalin.
- **Hasil teruji:** `B. Inggris 7 Linda edit.docx` (2 drawing paragraf, 1 di tabel, 3 part gambar, → …) → output 3 media (`image1/2/3.png`), 2 drawing paragraf + 2 di tabel, render PDF: gambar terpasang di posisi benar, kop SMP benar, nomor 1–20 mulus. Regresi IPA & IPS 3 (jalur teks) masih 2 seksi × 1–10 tanpa reset.
- **Batasan:** gambar di paragraf **kosong** (diagram berdiri sendiri) tetap disalin tapi TIDAK diberi nomor (plain); gambar dalam tabel berisi ikut di-remap.

## Rekomendasi ke depan

1. Perluas `--check` agar membandingkan output vs contoh "OK Edit P" (pixel/teks) otomatis untuk KPU (kop lengkap, nomor urut, tidak ada teks potong).
2. Untuk sumber `.doc` yang isinya gambar/equation banyak: pesan ke user — minta dokumen dalam .docx (atau biarkan Word COM untuk merge).
3. Kalau kelak dipakai guru di komputer lain (tanpa Python/LibreOffice): bungkus exe (PyInstaller) — baru setelah workflow stabil di PC.

## Benchmark vs file jadi sekolah (riset lanjutan 18/9)

Proses 6 bahan mentah asli dari `@backup` dan bandingkan dengan file jadi "… OK Edit P" sekolah:

- **Terbukti handle:** PKn 3 (2 seksi/20 soal), Seni Musik 3 (2/20), Matematika 4 (4/40), E. Math 6 (10 seksi/11 soal), Matematika 3, IPA 3, IPS 3 (2/20), Mandarin 8 (3/20) & 9 (3/15). Total 5 draft "… 3 DRAFT.docx" validasi Gemini = **siap cetak**.
- **Struktur file jadi sekolah yang TIDAK ditiru builder (belum):**
  1. **Kop diulang per halaman** (tbl=2–3 pada file jadi) — builder cuma 1 kop di awal. Diperlukan opsi `--kop-each-page` / section break per seksi.
  2. **Nomor via AutoNumbering** (`ListParagraph`, w:numPr) — teks tak memuat angka; builder pakai nomor literal `"N.\t"` (identik visual, beda mekanisme; saat guru edit di Word penomoran jadi tetap/sinkron dengan gaya list).
  3. Label seksi sekolah memakai bobot: `Isian CP 2 (50%)`, `Esai (50%)`, `CP 1 Bilangan Cacah (100%)` dst — builder menyalin label sumber apa adanya.
  4. **Nomor di dalam sel TIDAK ikut di-renum** — tabel data disalin apa adanya (Mandarin 8: seksi II bertahan 11–15 padahal seharusnya 6–10). Batas yang disadari.
- **Gap kelas yang belum dibuat sekolah (raw ada, draft dibuat hari ini):** Matematika 3, IPA 3, IPS 3, B. Mandarin 8–9 (SMP; perlu `--unit SMP`), B. Inggris 7–9 (file besar ber-gambar → lebih aman Word COM / periksa manual). IPA-IPS juga kena gap kelas 3.
- **Fitur baru:** `--unit SD|SMP` untuk ganti kop "SD SWASTA METHODIST-11" → "SMP SWASTA METHODIST-11" (default SD).
- **Bug fix:** check_visual.py crash `UnicodeEncodeError cp1252` saat Gemini balas pakai emoji (✅) → `sys.stdout.reconfigure(errors="replace")` (pola ERR-20260917-002).

- **Deteksi kop dobel (bug nyata):** string teks kop bisa TERPECAH antar `<w:t>` run (mis. "SMP" / " " / "SWASTA") → cek `xml` mentah (substring "SD SWASTA") MISS terhadap kop sumber SMP. `is_kop_table()` wajib membaca teks gabungan per sel via `Table(tbl, None)` + regex `(SD|SMP)\s+SWASTA` + label KOP_LABELS. Sebelum fix, output 2 tabel kop (standar + sumber); terverifikasi B.Inggris 7 (SMP) & IPA/IPS 3 (SD) = 1 kop.

- **Judul seksi BOLD + jarak antar seksi (18/9):** judul khas sekolah seperti `KD 3.1` / `Complete each sentence with a or an. (50%)` / `Read the texts below...` kini **bold** dan memulai seksi baru (nomor reset) dengan **jarak 18pt sebelum judul** (baris judul lanjutan 3pt). Deteksi `is_title_line()`: baris bukan soal/opsi yang (1) diawali `KD <angka>` (KD_RE), atau (2) diawali kata kerja instruksi Inggris (complete/read/choose/match/... INSTRUCT_RE) DAN memuat `(xx%)` (PCT_RE) atau baris persis setalah judul. Baris pengantar panjang tetap non-bold (mis. "Short Answer Questions").

## Referensi

- Tool: `COMMON/scripts/ujian_builder.py` · kop: `COMMON/scripts/kop-methodist.docx` · verifier: `COMMON/scripts/check_visual.py`
- Contoh jadi sekolah: `@backup` + "… OK Edit P.docx" di `\\192.168.136.1\Methodist-11 Document\SOAL UJIAN\Soal Ujian UTS 1 T.P. 2026-2027\`
- LRN terkait: LRN-20260918-004 (python-docx) · LRN-20260917-002 (penyemak visual) · LRN-20260918-001 (fidelity LO vs Word)