# Setup - Linux Tablet Tiny

Di-update: 29 April 2026

---

## 📋 Identitas

- **Device:** Linux Tablet Tiny (Baru)
- **OS:** Linux ( Langsung di Termux )
- **Path:** /root/Desktop/memory (di Termux langsung, bukan proot)

---

## 📋 Cara Kerja

1. **Load Memory (setiap sesi):**
```
cd /root/Desktop/memory && git pull
```

2. **Baca panduan:**
- `COMMON/docs/MASTER-MEMORY.md`
- `linux-tablet/docs/setup.md` (referensi dari tablet utama)
- `linux-tablet-tiny/docs/setup.md` (file ini)

3. **Kerja**

4. **Simpan Memory (akhir sesi):**
```
cd /root/Desktop/memory
git add .
git commit -m "update"
git push
```

---

## 📋 Trigger Commands

```
/loadmemory  → cd memory && git pull
/savememory  → git add . && git commit -m "update" && git push
/ingat      → catat ke notes.md
```

---

## 📋 Catatan

- Ini setup sederhana dari linux-tablet
- Stay di Termux (tanpa VNC/Ubuntu)
- Belajar dari linux-tablet/docs/setup.md

---

## 📋 Software Terinstall

- **WPS Office:** `/opt/kingsoft/wps-office/office6/wps`
- **Backup di Shared Storage:** `/storage/emulated/0/wps-office-backup/`

---

## 📋 Riwayat Update

- 29 April 2026 - Dibuat setup linux-tablet-tiny
- 29 April 2026 - Cek WPS, tersedia di /opt/kingsoft/wps-office/
- 30 April 2026 - Setup SMB connection

---

## 📋 SMB Connection (30 April 2026)

### Server
- IP: 192.168.1.200
- Share: `Methodist-11 Document`
- Username: wilianto
- Password: wilianto

### Cara Akses via CLI
```bash
# List folder
smbclient "//192.168.1.200/Methodist-11 Document" -U wilianto%wilianto -c "ls"

# Download file
smbclient "//192.168.1.200/Methodist-11 Document" -U wilianto%wilianto -c "get \"nama file.docx\" ~/file.docx"

# Upload file
smbclient "//192.168.1.200/Methodist-11 Document" -U wilianto%wilianto -c "put ~/file.docx \"nama file.docx\""
```

### Catatan
- Mount CIFS tidak support di Android kernel (Function not implemented)
- Alternatif: Download-edit-upload via smbclient
- Atau: ES File Explorer (Android) → SMB → open with WPS (Android)

---