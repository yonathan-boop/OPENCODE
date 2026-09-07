# Template Session Report

Template baku untuk laporan akhir sesi. Salin ke `PC-XX/docs/SESSION-YYYY-MM-DD.md`
(setiap kali sesi selesai) dan isi bagian yang relevan. Template ini juga dipakai
sebagai acuan laporan night-shift otomatis.

---

## 1. Info Sesi

| Field | Isi |
|-------|-----|
| Tanggal | YYYY-MM-DD |
| PC | PC-06 / yonat-PC / PC-Advan / server-linux / dll |
| Model | opencode/big-pickle |
| Durasi | (jam mulai - selesai, opsional) |

## 2. Aktivitas / Tugas

- [ ] Ringkas apa yang dikerjakan (1-3 kalimat per task)
- [ ] Sertakan file hasil + path-nya
- [ ] Sertakan perintah yang dipakai (kalau perlu diulang)

Contoh blok per task:

```
### Task: <nama>
- Aksinya: <ringkasan>
- Hasil file: <path file>
- Validasi: <bukti cek ulang>
```

## 3. Keputusan User

- [ ] Catat setiap keputusan penting user di sesi ini
- [ ] Keputusan permanen → promosikan ke MASTER-MEMORY.md

## 4. Error / Masalah

- [ ] Error & solusi → catat ke `COMMON/docs/MEMORY-ERRORS.md` (pakai hashtag)
- [ ] Pola/insight baru → catat ke `COMMON/docs/MEMORY-LEARNINGS.md`

## 5. Status Backlog

- [ ] Update `COMMON/docs/BACKLOG.md` (Done / In Progress / Backlog)

## 6. Ringkasan untuk summary

- [ ] Update `PC-XX/summary.md`: sesi terakhir, total sesi, aktivitas singkat

## 7. Format Laporan Singkat (untuk bot/laporan otomatis)

```
## Laporan <jenis> <tanggal>
- SELESAI: <apa yang dikerjakan>
- BELUM: <yang ditunda dan kenapa>
- CATATAN: <insight / kabar penting buat user>
```

---

## Checklist Penutup

- [ ] Semua hasil divalidasi sebelum lapor (pola execute → verify → report)
- [ ] Memory sudah disimpan & di-commit ke GitHub