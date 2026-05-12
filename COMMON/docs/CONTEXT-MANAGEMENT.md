# Context Management

Context adalah sumber daya terbatas. Harus efisien.

## Prinsip Dasar
- **Jangan baca semua memory setiap sesi.** Hanya yang relevan.
- **Prioritaskan memory per-PC.** PC-06 ya baca PC-06, bukan PC-Advan.
- **Memory lintas-PC** hanya dibaca jika task relevan.

## Fase LOAD (Sesi Baru)
WAJIB baca:
- `PC-XX/summary.md` — ringkasan PC
- `PC-XX/facts.md` — fakta PC
- `COMMON/docs/MEMORY-LEARNINGS.md` — pembelajaran masa lalu
- `COMMON/docs/MEMORY-ERRORS.md` — error masa lalu
- Cek 3 file terbaru di `PC-XX/docs/`

JANGAN baca (kecuali relevan):
- Semua file di `PC-XX/scripts/`
- Semua file di `PC-XX/screenshots/`
- Semua file di `PC-XX/output/`
- Memory PC lain (PC-Advan, linux-hp, dll)

## Fase PLAN (Per Task)
Sebelum mulai task, cari memory relevan:
- Gunakan grep dengan keyword dari task
- Cuma baca file yang match
- Jangan baca semua memory cuma "biar aman"

Contoh:
- Task: absensi → cari `absensi` di memory
- Task: install software → cari `install` atau nama software
- Task: edit file → baca file itu aja, plus file terkait

## Fase EXECUTE
- **File yang sudah dibaca** jangan dibaca ulang tanpa perlu
- Kalau perlu referensi, simpan poin penting, bukan raw file
- Sub-agent: kirim konteks minimal (path, instruksi, data), bukan full history

## Fase SAVE
- Simpan ke `PC-XX/docs/` — relevan per PC
- Hanya simpan ke `COMMON/docs/` jika berlaku lintas PC (learning, error, workflow)
- Jangan duplikasi: cek dulu apakah info sudah ada
