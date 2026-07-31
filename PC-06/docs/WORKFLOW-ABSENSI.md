# Workflow Absensi

## Langkah-Langkah (WAJIB BERURUTAN)

1. **Tampilkan ringkasan absensi** — buat tabel dulu sebelum eksekusi:
   | Tanggal | Kelas | Nama | Alasan |
   |---------|-------|------|--------|
   | (isi dari user) | | | |
   
   **INI WAJIB** — user harus review dan konfirmasi tabel sebelum lanjut.

2. **Cek file terbaru** di `PC-06/docs/Absensi T.P 2026-2027/` — lihat file Absensi Juli dengan tanggal terakhir
3. **Duplicate file** — copy file Absensi terbaru, rename ke format:
   `Absensi <Bulan> <Tanggal> <Tahun> <Hari> <Jam>.xlsx`
   Contoh: `Absensi Juli 12 2026 Saturday 09_00_00.xlsx`
4. **Update script** — ganti `FILE_PATH` di `COMMON/scripts/absensi.py` ke file baru
5. **Jalankan absensi** — `python absensi.py <nama> <kelas> <tanggal> <kode>`
6. **Report hasil** — tampilkan mana yang berhasil/gagal
7. **Catat memory** — simpan hasil absensi

## Kode
- S = Sakit
- I = Izin
- A = Alpha
- . = Hadir

## Kelas
- TKa, TKB1, TKB(2), PG
