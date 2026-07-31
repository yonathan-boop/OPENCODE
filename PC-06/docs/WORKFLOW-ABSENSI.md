# Workflow Absensi

## KONSEP PENTING (31 Juli 2026)

- **ABSENSI Juli.xlsx = file utama yang SELALU PALING LENGKAP.** Semua update absensi ditulis ke file ini.
- **File harian = arsip snapshot.** Setiap hari duplicate ABSENSI Juli.xlsx jadi file baru (1 file/hari) SEBELUM update.
- **JANGAN pernah** duplicate file harian lama untuk dijadikan base — file harian bisa kurang lengkap. Selalu dari ABSENSI Juli.xlsx.
- Kalau ragu data lengkap atau tidak → jalankan `merge_absensi.py` dulu, baru duplicate.

## Langkah-Langkah (WAJIB BERURUTAN)

1. **Tampilkan ringkasan absensi** — buat tabel dulu sebelum eksekusi:
   | Tanggal | Kelas | Nama | Alasan |
   |---------|-------|------|--------|
   | (isi dari user) | | | |

   **INI WAJIB** — user harus review dan konfirmasi tabel sebelum lanjut.

2. **Cek file terbaru** di `PC-06/docs/Absensi T.P 2026-2027/` — pastikan ABSENSI Juli.xlsx ada dan datanya lengkap.

3. **Duplicate file** — copy ABSENSI Juli.xlsx, rename ke format arsip:
   `Absensi <Bulan> <Tanggal> <Tahun> <Hari> <Jam>_<Menit>_<Detik>.xlsx`
   Contoh: `Absensi Juli 31 2026 Friday 10_00_00.xlsx`
   (1 file per hari, tidak lebih. File lama tidak dihapus.)

4. **Jalankan absensi** — edit ABSENSI Juli.xlsx (file utama):
   `python absensi.py <nama> <kelas> <tanggal> <kode>`

5. **VALIDASI WAJIB** — baca ulang ABSENSI Juli.xlsx:
   - Cek tanggal terisi benar (bukan blank)
   - Cek nama & kelas sesuai input
   - Kalau ada yang salah → fix dulu, baru lapor

6. **Report hasil** — tampilkan mana yang berhasil/gagal

7. **Catat memory** — simpan hasil absensi

## Script Bantuan

- `COMMON/scripts/absensi.py` — tulis satu tanda absen ke ABSENSI Juli.xlsx
- `COMMON/scripts/merge_absensi.py` — gabungkan SEMUA file harian Juli ke ABSENSI Juli.xlsx (untuk konsolidasi/bukti data lengkap)

## Kode
- S = Sakit
- I = Izin
- A = Alpha
- . = Hadir

## Kelas
- TKa, TKB1, TKB(2), PG
