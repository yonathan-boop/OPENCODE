# Workflow Absensi

## Langkah-Langkah

1. **Cek file terbaru** di `PC-06/docs/` — lihat file Absensi Mei dengan tanggal terakhir
2. **Duplicate file** — copy file Absensi terbaru, rename ke format:
   `Absensi <Bulan> <Tanggal> <Tahun> <Hari> <Jam>.xlsx`
   Contoh: `Absensi Mei 12 2026 Tuesday 09_00_00.xlsx`
3. **Update script** — ganti `FILE_PATH` di `COMMON/scripts/absensi.py` ke file baru
4. **Jalankan absensi** — `python absensi.py <nama> <kelas> <tanggal> <kode>`
5. **Catat memory** — simpan hasil absensi

## Kode
- S = Sakit
- I = Izin
- A = Alpha
- . = Hadir

## Kelas
- TKa, TKB1, TKB(2), PG
