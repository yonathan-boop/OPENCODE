# SELF-STUDY — Sistem Belajar Mandiri AI (24/7)

Sistem agar asisten terus mengembangkan diri secara otomatis, tanpa diminta.
Ide inti dari user (17/9/2026): "kamu jelajah sendiri, berkembang, supaya bisa
membantu lebih banyak hal nantinya" — token murah, manfaatkan. Belajar jalan
**setiap saat**, tapi di **proses terpisah** (daemon) — terminal interaksi ini
khusus untuk ngobrol sama user.

## Cara Kerja
1. **Queue topik** di `topics.md` — daftar hal yang berguna untuk pekerjaan user
   (admin sekolah). Tambah/kurang bebas, diproses urut dari atas.
2. **Daemon 24/7** `SERVER-LINUX/scripts/self-study-daemon.sh`:
   - Loop terus-menerus: tiap siklus proses **satu topik** → tidur 15 mnt.
   - `opencode run --auto` = sesi fresh tiap topik → **konteks tidak menumpuk** (RAM aman).
   - **Guard RAM (<700MB free → skip)** dan **disk (>80% → skip)** supaya website
     (serve8090) & terminal online tidak ikut terganggu.
   - **Singleton** via flock; kalau mati, cron `*/15` / `@reboot` menghidupkan lagi.
   - Heartbeat: `/var/log/self-study-beat` · log: `/var/log/self-study-daemon.log`.
3. **Hasil** = catatan ringkas (Ringkasan / Poin praktis / Jebakan / Sumber) di `notes/`.

## Manual Run (kapan saja)
```bash
bash /root/SERVER-LINUX/scripts/self-study.sh          # satu topik
bash /root/SERVER-LINUX/scripts/self-study-daemon.sh   # mulai daemon
```
File di `notes/` ikut ke-sync lewat repo memory ke semua PC.

## "Mata" — Gemini Vision
Saat kerja mandiri, AI kadang perlu LIhat (screenshot/gambar) — pakai tool:
```bash
python3 COMMON/scripts/gemini_vision.py <gambar> "pertanyaan"
python3 COMMON/scripts/gemini_vision.py --text "pertanyaan"
```
- Kunci API: `/root/.config/gemini-api-key` (chmod 600, DI LUAR git — jangan commit).
- Model default `gemini-3.6-flash` (bisa ubah via env `GEMINI_MODEL`).
- Hasil akhir tetap divalidasi mata manusia (user).

## Aturan
- Topik harus praktis & relevan kerja user (bukan hiburan/teori murni).
- Catatan ditulis Bahasa Indonesia, ringkas, fokus "biar bisa langsung dibantu".
- Jangan sentuh service/kredensial/data user dalam proses riset.