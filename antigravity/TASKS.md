# TASKS.md - Rutinitas & Alur Kerja Antigravity

Daftar checklist alur kerja rutin yang dapat langsung dijalankan oleh Antigravity:

## 1. Absensi Murid Harian
- **SOP:**
  1. Buat versi file baru 1 file/hari di `PC-06/docs/Absensi T.P 2026-2027/`.
  2. Update `FILE_PATH` di `COMMON/scripts/absensi.py`.
  3. Input absensi via `py absensi.py "<nama>" <kelas> <tgl> <alasan>`.
  4. Validasi isi cell Excel.
  5. Catat di `MASTER-MEMORY.md` & `PC-06/summary.md`.
  6. Commit & push ke GitHub.

## 2. Pengelolaan Dokumen Ujian & Sekolah
- Manfaatkan 4 skill di `antigravity/skills/`:
  - `docx`: Pembuatan soal ujian, format tabel, header/footer, eliminasi ghost Word COM.
  - `xlsx`: Olah data rapor, roster murid, rekap absensi.
  - `pdf`: Konversi, split, merge, ekstraksi dokumen cetak.
  - `pptx`: Slide presentasi sekolah & materi ajar.

## 3. Pengawasan Sistem & Backup
- Website `methodist-11.my.id` (Port 8090 / Cloudflare Tunnel / Server Linux).
- Skrip backup harian `PC-06/scripts/backup-methodist.ps1` (14:30 & 14:50) ke Google Drive.
