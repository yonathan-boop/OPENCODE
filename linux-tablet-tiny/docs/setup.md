# Setup - Linux Tablet Tiny

Di-update: 29 April 2026

---

## 📋 Identitas

- **Device:** Linux Tablet Tiny (Baru)
- **OS:** Linux ( Langsung di Termux )
- **Path:** /root/Desktop/memory

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

## 📋 Riwayat Update

- 29 April 2026 - Dibuat setup linux-tablet-tiny

---