# Setup - Linux Tablet 5

Di-update: 29 April 2026

---

## 📋 Identitas

- **Device:** Linux Tablet 5 (Baru/Dedicated)
- **OS:** Android 15 → Ubuntu Linux (via Termux proot-distro)
- **Akses VNC:** localhost:5905 (Xtigervnc :5)
- **Path:** /data/data/com.termux/files/home/Desktop/New Folder/memory

---

## 📋Cara Kerja

1. **Load Memory (setiap sesi):**
```
cd /data/data/com.termux/files/home/Desktop/New\ Folder/memory && git pull
```

2. **Trigger Commands:**
```
/loadmemory   → git pull + baca memory
/savememory  → git add . && git commit -m "update" && git push
/ingat "isi" → catat ke MASTER-MEMORY.md
```

3. **Kerja**

4. **Simpan Memory (akhir sesi):**
```
cd /data/data/com.termux/files/home/Desktop/New\ Folder/memory
git add .
git commit -m "update"
git push
```

---

## 📋 Software Bawaan

- Chromium Browser ✅ (/usr/bin/chromium)
- Lainnya: lihat di setup linux-tablet

---

## 📋 VNC Servers Berjalan

- 5901 - Xvnc :1
- 5902 - Xvnc :2
- 5905 - Xtigervnc :5 ← Device ini

---

## 📋 Trigger Awal Sesi (WAJIB)

```
cd /data/data/com.termux/files/home/Desktop/New\ Folder/memory
git pull
```
Lalu baca:
- linux-tablet-5/docs/setup.md (file ini)
- COMMON/docs/MASTER-MEMORY.md
- linux-tablet/docs/setup.md (referensi)

Laporan ke user: "Linux Tablet 5 siap!"

- Ini device khusus untuk linux-tablet-5
- sisters: linux-tablet, linux-tablet-tiny

---

## 📋Riwayat

- 29 April 2026 - Dibuat folder linux-tablet-5