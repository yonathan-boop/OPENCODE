# Trigger Commands untuk Memory System

---

## DI AWAL SESI (Load Memory)

Ketik ini di awal sesi:

```
/loadmemory
```

otomatis akan:
1. deteksi folder memory aktif (`C:\Users\Admin\Desktop\memory` atau `C:\Users\Advan\Desktop\memory`)
2. git pull (ambil data terbaru)
3. baca semua file `.md` di `COMMON/docs`, `PC-06`, `PC-Advan`
4. baca juga file pembelajaran aktif:
   - `COMMON/docs/MEMORY-LEARNINGS.md`
   - `COMMON/docs/MEMORY-ERRORS.md`
   - `COMMON/docs/MEMORY-FEATURE-REQUESTS.md`
5. gabungkan jadi konteks
6. laporkan `Memory loaded!` + ringkasan yang relevan

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
4. pastikan update hari ini, koreksi user, dan keputusan penting sudah dicatat ke memory sebelum push

---

## LAIN-LAIN

```
/ingat "<isi>"    → catat info penting ke MASTER-MEMORY.md
/status            → cek status memory & commit terbaru
```

Tambahan perilaku yang WAJIB diingat:
- Kalau user memberi contoh hasil, screenshot, atau referensi, anggap itu sebagai patokan utama
- Kalau user memberi instruksi singkat seperti `lebih clean`, `lebih enak dilihat`, `kayak yang tadi`, jangan minta user mengulang panjang; tafsirkan dari konteks dan memory
- Kalau ada error, koreksi user, atau pola berulang, catat juga ke file pembelajaran agar sistem berkembang

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
