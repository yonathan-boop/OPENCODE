# Trigger Commands untuk Memory System

---

## DI AWAL SESI (Load Memory)

Ketik ini di awal sesi:

```
/loadmemory
```

otomatis akan:
1. cd ke folder memory
2. git pull (ambil data terbaru)
3. baca semua file .md
4. gabungkan jadi konteks

---

## DI AKHIR SESI (Save Memory)

Ketik ini untuk simpan & push:

```
/savememory
```

atau cukup:

```
simpan
```

otomatis akan:
1. git add -A
2. git commit dengan timestamp
3. git push ke GitHub

---

## LAIN-LAIN

```
/ingat "<isi>"    → catat info penting ke MASTER-MEMORY.md
/status            → cek status memory & commit terbaru
```

---

## FOLDER LOCATION

- pc-06: C:\Users\Admin\Desktop\memory
- Advan: C:\Users\Advan\Desktop\memory

---

## JIKA FOLDER BELUM ADA

Clone dulu:
```
git clone https://github.com/yonathan-boop/OPENCODE.git C:\Users\XXX\Desktop\memory
```

---