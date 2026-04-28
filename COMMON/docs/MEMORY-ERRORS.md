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
