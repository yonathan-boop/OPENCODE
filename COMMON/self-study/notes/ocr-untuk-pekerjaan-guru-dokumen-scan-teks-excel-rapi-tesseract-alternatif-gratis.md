# OCR untuk pekerjaan guru: dokumen scan → teks/Excel rapi (Tesseract & alternatif gratis)

## Ringkasan
OCR berguna untuk guru/admin sekolah supaya dokumen hasil scan (rapor, absensi, daftar nilai, berita acara, surat) bisa jadi **teks yang bisa dicari**, **PDF searchable**, atau diekstrak ke **Excel/CSV**. Di 2026, **Tesseract** tetap mesin OCR open-source paling praktis untuk kebutuhan offline murah; alternatifnya berupa **app scanning + OCR** (lebih ramah pengguna) atau **OCR engine lain** kalau hasil Tesseract kurang akurat pada dokumen rumit.

Kunci sukses: **kualitas scan** (minimal ~300 DPI, teks gelap di latar terang, lurus) + preprocessing ringan (tegas/threshold, koreksi rotasi, hapus noise). Setelah dapat teks, ubah ke tabel pakai script (Python/openpyxl) sesuai pola dokumen sekolah.

## Poin praktis untuk admin sekolah
### Pakai Tesseract (offline, gratis, fleksibel)
- **Jalur cepat (teks biasa):** gunakan Tesseract CLI langsung.
  - `tesseract scan.png hasil -l ind+eng --psm 3` → menghasilkan `hasil.txt`
  - Untuk PDF searchable: `tesseract scan.png hasil -l ind+eng pdf`
- **Kalau butuh Excel/CSV:** ekstrak dulu ke teks/TSV/hOCR, lalu parse ke tabel dengan Python.
  - Contoh alur: scan → pytesseract `image_to_data()` → ambil kata + koordinat baris → kelompokkan per baris → tulis ke Excel/openpyxl.
- **Setelan paling sering dipakai:**
  - `--psm 3` (auto halaman penuh).
  - `--psm 6` (blok teks seragam, misalnya daftar/lembar isian).
  - `--psm 7` (satu baris saja).
  - `--oem 1` (LSTM) umumnya paling akurat di Tesseract 5.

### Alternatif gratis yang mempermudah kerja
- **NAPS2** (Windows/Mac/Linux): app scanning gratis + OCR via Tesseract.
  - Cocok untuk guru/admin yang mau scan langsung ke PDF searchable tanpa了很多 CLI.
  - Bisaatur DPI, koreksi rotasi, crop, lalu OCR bahasa Inggris/100+ bahasa (tergantung data bahasa terpasang).
- **GImageReader**: GUI untuk Tesseract (buka gambar/PDF, seleksi area, copy teks).
- **OpenScan**: app mobile/privasi-first untuk scan ke PDF + OCR.
- **OCR4all**: lebih ke arah dokumen historis/kuno (butuh anotasi/lebih teknis), jarang dibutuhkan untuk administrasi sekolah biasa.
- **Solusi modern**: PaddleOCR/Docling (akurat, fitur tabel/letak) tapi biasanya butuh setup lebih teknis; bagus kalau Anda punya tim IT/developer pendukung.

### Workflow untuk data sekolah (absensi/nilai)
- Jangan paksa OCR langsung jadi Excel “sempurna” dari scan rumit.
- Lebih aman: **OCR → teks/JSON → script mapping ke format Excel** sesuai template sekolah.
- Simpan juga PDF hasil scan sebagai bukti asli (data visual), dan file Excel hasil ekstraksi untuk keperluan data.

## Jebakan / error umum
- **Hasil OCR berantakan saat tabel/garis tebal:** Tesseract kurang optimal langsung me-resolve tabel kompleks. Solusi: pre-crop per kolom/baris, atau ekstrak via koordinat (pytesseract `image_to_data`).
- **Scan rendah DPI / buram / miring:** akurasi turun drastis. Pastikan minimal ~300 DPI, teks cukup kontras, dan halaman lurus.
- **Bahasa campuran (Indonesia + nama sendiri/asing):** pakai bahasa ganda (`-l ind+eng`) atau siapkan custom dictionary kalau banyak nama unik.
- **PDF password/terproteksi atau hasil export dari aplikasi** (bukan scan): OCR tidak diperlukan; langsung ekstrak teksnya (jika memungkinkan).
- **Linux/macOS tanpa data bahasa terpasang:** perlu install paket data bahasa tambahan agar OCR Indonesia berfungsi.

## Sumber
- Tesseract OCR (resmi): https://tesseractocr.org/ ; https://github.com/tesseract-ocr/tesseract
- Tesseract docs (install/CLI/OEM/PSM): https://tesseractocr.org/doc
- Improve quality (preprocessing): https://github.com/tesseract-ocr/tessdoc/blob/main/ImproveQuality.md
- pytesseract (Python wrapper): https://pypi.org/project/pytesseract/
- NAPS2 (free scanner + OCR via Tesseract): https://www.naps2.com/ ; https://github.com/cyanfish/naps2
- Alternatives overview (2026, komersial + open-source): https://www.klippa.com/en/blog/information/the-best-alternative-to-tesseract
