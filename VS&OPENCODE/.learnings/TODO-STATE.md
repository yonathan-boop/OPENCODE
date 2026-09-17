# TODO-STATE.md — Persistent Todo Panel State

Di-update: 15 September 2026

## ≡≡≡ GAGAL / BERHENTI ≡≡≡
- (kosong)

## ≡≡≡ LAGI DIKERJAIN ≡≡≡
- **Self-study daemon 24/7 aktif** (server): belajar mandiri terus-menerus, proses terpisah, guard RAM/disk. Topik berikutnya dari queue (Kurikulum Deep Learning 2026). Monitor: `/var/log/self-study-daemon.log` + beat `/var/log/self-study-beat`.
- GENERATOR-RPP Methodist-11: file HTML aktif di `OneDrive\Dokumen\`, backup di repo memory. API key Gemini tertanam. User mungkin mau verifikasi NIP/NUPTK guru → belum ada data.
- **rclone gdrive shared client_id akan di-retire 2026** → user perlu buat client_id sendiri (panduan: `COMMON/docs/RCLONE-CLIENT-ID.md`). Urgent karena auto-update website & backup gdrive bergantung ke sana.

## ≡≡≡ BERHASIL ≡≡≡
- **"Mata" Gemini vision (17/9):** `COMMON/scripts/gemini_vision.py`, key di `/root/.config/gemini-api-key` (di luar git), model gemini-3.6-flash, teruji (teks + baca gambar)
- **SELF-STUDY naik ke 24/7 (17/9):** daemon terpisah + guard memori + cron guardian (`*/15`,`@reboot`); terminal online khusus interaksi user
- **absensi.py matching fix (17/9):** token-matching Levenshtein+SequenceMatcher, 24/24 test lulus, ambigu → skip aman
- **RCLONE-CLIENT-ID.md (17/9):** panduan ganti shared client_id (butuh aksi user sekali)
- website SD Methodist-11 LIVE di server Linux (22 Agustus 2026)
- GENERATOR-RPP diadaptasi ke Methodist-11: guru 18 mapel, kepsek/sekolah dropdown, Gemini API, localStorage save, logo dihapus (15 September 2026)
- GENERATOR-RPP + backup di-commit & push ke repo memory (`COMMON/project-generator-rpp/`) (15 September 2026)
- MASTER-MEMORY konsolidasi: 81→36KB, context startup turun 23%→19% (15 September 2026)
- Telegram bot & notif dihapus total → log-only (11 September 2026)
- Backup harian Methodist ke G: Drive otomatis (14:50 tiap hari)
- Auto-update website dari Google Drive (cron tiap 15 mnt)
- install 4 skill dokumen, model big-pickle permanen (5 September 2026)
- EPSON L3210 dihapus total dari yonat-PC (8 September 2026)
- TrafficMonitor + OpenClaw dinonaktifkan (7 September 2026)
- bikin sub-agent protocol
- todo panel standar + auto-restore
- restore memory dari Windows.old (18 Juli 2026)
