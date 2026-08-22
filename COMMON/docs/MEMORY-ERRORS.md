# Memory Errors

Catatan error penting, tool failure, atau kegagalan workflow yang perlu diingat agar tidak terulang.

---

## [ERR-20260428-001] Kill VNC Server Saat Remote Session

**Tanggal**: 2026-04-28
**Device**: linux-tablet (Termux)
**Severity**: high

### Summary
Saat mencoba restart VNC untuk refresh desktop, saya menggunakan `pkill -9 Xvnc` yang membunuh proses VNC yang sedang digunakan untuk koneksi remote session ini sendiri.

### Action
- **JANGAN pernah** kill proses Xvnc/XFCE yang sedang digunakan untuk remote
- Untuk restart, gunakan cara yang lebih aman atau tanya user dulu
- Lebih baik start ulang VNC di display lain daripada kill yang aktif

### Catatan
- User sudah restore sendiri
- Symlink /root/Desktop -> /data/data/com.termux/files/home/Desktop sudah dibuat
- Desktop files sudah ada: Files.desktop, Firefox.desktop, Proot.desktop, Terminal.desktop, New Folder

---

## [ERR-20260819-001] Absensi_Langsung_Edit_Buat_Sistem_Versi

**Tanggal**: 2026-08-19
**Severity**: high
**Status**: fixed

### Summary
AI langsung mengedit file Excel absensi yang sudah ada tanpa membuat versi baru terlebih dahulu. Melanggar aturan sistem versi yang sudah ditetapkan sejak 4 Agustus 2026.

### Gejala
- File `Absensi 15 Agustus 2026 Saturday 10_18_23.xlsx` langsung diedit untuk menambah data18-19 Agustus
- Tidak ada proses: copy versi terbaru → file baru → isi data
- Tidak ada update FILE_PATH di absensi.py

### Penyebab
- AI tidak mengikuti prosedur sistem versi yang sudah ada di MASTER-MEMORY.md
- AI menganggap "edit in-place" sebagai cara cepat, padahal melanggar aturan utama

### Lokasi
- File: `Absensi 15 Agustus 2026 Saturday 10_18_23.xlsx`
- Script: `COMMON/scripts/absensi.py`

### SOLUSI
1. File lama di-restore via `git restore` (belum di-commit, jadi bisa dikembalikan)
2. File baru dibuat: `Absensi 19 Agustus 2026 Tuesday 08_00_00.xlsx` (isi: data13-15 + 18-19)
3. FILE_PATH di absensi.py diupdate ke file baru
4. Validasi: 17 mark18-19 ✅, 11 mark13-15 ✅

### ATURAN WAJIB (PENGINGAT)
```
SETIAP KALI UPDATE ABSENSI:
1. Copy versi terbaru → file versi baru (nama: Absensi <tgl> <bulan> <tahun> <hari> <jam>_<menit>_<detik>.xlsx)
2. Update FILE_PATH di absensi.py ke file baru
3. Isi data di file BARU (bukan file lama)
4. Validasi sebelum lapor
```

---

## [ERR-20260822-001] Sub-Agent Return Kosong Beruntun

**Tanggal**: 2026-08-22
**Severity**: medium
**Status**: workaround ditemukan

### Summary
Task tool (sub-agent) balik hasil kosong 3x berturut-turut dengan state "completed": (1) simpan memory absensi 22 Agu, (2) retry simpan memory, (3) update roster absensi v22. Pekerjaan tidak jadi/tidak tuntas tanpa pesan error apapun.

### Gejala
- `<task_result>` kosong padahal prompt instruksi lengkap & detail
- Bukti fisik menunjukkan kerjaan cuma separuh jalan (cuma explore.py dibuat di temp, file target tidak tersentuh)

### SOLUSI
1. Jangan percaya laporan — cek bukti fisik: `git log`, `git status`, LastWriteTime file target, isi folder temp
2. Kalau gagal senyap berulang → otak eksekusi manual langsung (python/bash) + validasi sendiri
3. Laporan sub-agent yang sukses pun sempat korup karakter (teks Indonesia rusak) → indikasi masalah encoding pipeline output

---
