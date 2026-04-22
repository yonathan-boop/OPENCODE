INIT MEMORY SYSTEM

1. Deteksi folder memory aktif:
   - `C:\Users\Admin\Desktop\memory` (pc-06 / kerja)
   - `C:\Users\Advan\Desktop\memory` (PC-Advan / rumah)
2. `git pull`
3. Baca semua `.md` di folder `COMMON/docs`, `PC-06`, `PC-Advan`
4. Baca juga log pembelajaran di `COMMON/docs/MEMORY-LEARNINGS.md`, `COMMON/docs/MEMORY-ERRORS.md`, `COMMON/docs/MEMORY-FEATURE-REQUESTS.md`
5. Gabungkan jadi konteks
6. Laporkan ke user: "Memory loaded!" + ringkasan

TRIGGER:
/loadmemory → git pull + baca memory
/savememory → commit + push
/ingat "isi" → catat ke MASTER-MEMORY.md

CATATAN:
- Jika ada contoh hasil / referensi user, jadikan itu acuan utama untuk vibe, style, dan kualitas output
- Jika instruksi user singkat atau ambigu, pilih interpretasi paling masuk akal berdasarkan konteks memory dan percakapan
