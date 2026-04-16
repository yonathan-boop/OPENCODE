# Konfigurasi Auto Memory System

## Trigger Commands

### /loadmemory
- Pull data terbaru dari GitHub
- Baca semua file memory (.md)
- Biasa dijalankan di awal sesi

### /savememory  
- Commit & push semua perubahan ke GitHub
- Biasa dijalankan di akhir sesi

### / ingat "<isi>"
- Langsung catat info penting ke MASTER-MEMORY.md

---

## Cara Kerja

### Awal Sesi (Auto)
```
cd C:\Users\XXX\Desktop\memory
git pull
```
→ Otomatis dapat data terbaru dari PC lain

### Akhir Sesi (Auto)
```
cd C:\Users\XXX\Desktop\memory
git add -A
git commit -m "Update: <timestamp>"
git push
```
→ Semua perubahan di-push ke GitHub

---

## Contoh Penggunaan

1. **Mulai sesi:**
   - Otomatis pull dari GitHub
   
2. **Setelah dapat info penting:**
   - `/ingat Saya punya 2 PC, pc-06 dan Advan`
   
3. **Sebelum tutup sesi:**
   - Otomatis push ke GitHub

---

## Lokasi Folder
- pc-06: C:\Users\Admin\Desktop\memory
- Advan: C:\Users\Advan\Desktop\memory

---

## Catatan
- Pastikan sudah `git pull` sebelum `git push` agar tidak konflik
- Jika konflik, cek file yang bentrok lalu resolve manual