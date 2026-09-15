# GENERATOR-RPP for SD Swasta Methodist-11 Medan

#generator-rpp #methodist-11 #rpp #html #gemini #localstorage #word

Di-update: 15 September 2026 (yonat-PC)

## Ringkasan

File `GENERATOR-RPP.html` (di `C:\Users\yonat\OneDrive\Dokumen\`) semula template untuk SDN Payudan Nangger/Sumenep, diadaptasi penuh untuk penggunaannya di yonat-PC. **Backup di repo memory:** `COMMON/project-generator-rpp/` (file kerja + backup sebelum customisasi, di-commit & push 15/9):

- **Nama sekolah** → dropdown: SD Swasta Methodist-11 Medan (default) / SMP Swasta Methodist-11 Medan.
- **Kepala Sekolah** → dropdown: Dra. Linda Mahadjana (default) / Dra. Elly Rosana M. NIP keduanya `-` (belum tersedia).
- **Nama guru** → dropdown otomatis berdasar Mapel × Kelas (data dari jadwal mengajar), jabatan otomatis Guru Kelas (jika wali kelas) / Guru Mapel.
- **Tempat tanggal** → "Medan, " (bukan "Sumenep, ").
- **Logo/teks** "Kurikulum Merdeka · Deep Learning" + "GENERATOR RPP" di rail kiri → dihapus.
- **Simpan Data** (localStorage, key `GENERATOR_RPP_DATA_V1`) dipisah dari **Cetak/PDF** — 2 tombol di panel kiri. Semua isian (sekolah, mapel, kelas, semester, topik, CP/ATP/TP, tanggal, kepsek, jabatan, guru, centang Bloom/SOLO, 8 dimensi, 3 pilar, model) tersimpan dan dimuat ulang saat refresh.
- **Fitur AI "3 Pilar"** → pakai **Google Gemini API** (`gemini-3.6-flash`, endpoint `generativelanguage.googleapis.com`), key di `const API_KEY_GEMINI`. **⚠️ Key tertanam di file HTML** — jangan di-share ke publik; kalau bocor, buat ulang key di Google AI Studio.

## Sumber data (jadwal mengajar)

- `C:\RaporServer\JADWAL PELAJARAN\Edit11 (1).xlsx` — T.P.2026/2027 (diparsing manual via PowerShell Zip/XML, tanpa openpyxl; dump `edit11_parsed.txt`).
  - sheet2 = jadwal pelajaran per kelas + wali kelas.
  - sheet4 = matriks guru per mapel×kelas (IA–VIB).
- `C:\RaporServer\JADWAL MENGAJAR\` berisi .doc lama (2011–2020-an), tidak dipakai.

### Wali Kelas SD (terverifikasi)
I: Rini, S.E. & Henny Permata Sari, S.Ak. · II: Erica Halim, S.M. & Patricia · III: Erica Wijaya, S.Tr.Par, BHM. & Jellys Halim, S.Ak. · IV: Viviyanty, S.Kom. & Chelsea Christian · V: Winna, S.S. & Selly Silvana Hutagalung, S.Pd. · VI: Steven & Sahata Simanjuntak, S.Si.

Mata pelajaran (18): PAdBP, Pendidikan Pancasila, Bahasa Indonesia, Matematika, IPAS, IPA, IPS, Bahasa Inggris, English Math, Bahasa Mandarin, PJOK, Seni Musik, Seni Rupa, KTK, TIK, Literasi, Numerasi, Lab Bahasa Inggris.

## Mengingat / jebakan

- Struktur data guru ada di JS: `GURU_PROFILE` (semua NIP "-"), `WALI_KELAS`, `DATA_GURU_MAPEL`. Fungsi: `guruOtomatisKelas()`, `updateGuruOtomatis()`, `sinkronJabatanGuru()`, `terapkanGuruTersimpan()`.
- Mapel tanpa data guru untuk kelas tertentu → fallback ke wali kelas (by design).
- Model Gemini lama (`gemini-2.0-flash`) sudah tidak tersedia → gunakan `gemini-3.6-flash` (11/9 sudah dicek live).
- `DATA_GURU_MAPEL` untuk kelas III–VI mapel IPA/IPS/Seni Rupa/TIK/Literasi/Numerasi/Lab B.Ing sebagian perkiraan asisten — akan lebih akurat bila diverifikasi sekali lagi ke `Edit11 (1).xlsx`.
- Reset data yang tersimpan: tombol Simpan hanya simpan — untuk hapus, jalankan `localStorage.removeItem("GENERATOR_RPP_DATA_V1")` di console browser.