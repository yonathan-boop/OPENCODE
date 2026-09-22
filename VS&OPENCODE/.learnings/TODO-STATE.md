# TODO-STATE.md — Persistent Todo Panel State

Di-update: 22 September 2026

## ≡≡≡ GAGAL / BERHENTI ≡≡≡
- (kosong)

## ≡≡≡ LAGI DIKERJAIN ≡≡≡
- (kosong)

## ≡≡≡ BERHASIL ≡≡≡
- **KSP 2026/2027 SD Swasta Methodist-11 (22/9 — Selesai Penuh Dokumen 1):** SELESAI LENGKAP seluruh naskah Dokumen 1 KSP (Cover s.d. BAB VI & Lampiran) di `C:\RaporServer\KOSP KURMER\Edit pc\`: (1) Bagian Awal: Cover resmi, Identitas, Rekomendasi Pengawas, Lembar Pengesahan, Kata Pengantar, Daftar Isi dot-leader; (2) BAB I: Profil Sekolah, Sarpras, SWOT Medan Johor, 369 siswa (12 rombel), 18 guru aktual Lapbul Agustus 2026, Rapor Pendidikan, TKA, 19 Landasan Hukum; (3) BAB II: Visi, Misi 4 butir, Tujuan Jangka Pendek (9 butir), Menengah (9 butir), Panjang (8 butir); (4) BAB III: Struktur Kurikulum Kelas I-VI, Kokurikuler 8 Dimensi & Tabel 8 lengkap 3 Fase, Ekstrakurikuler Tabel 15 (Pramuka wajib, Keagamaan, Olahraga, Seni, Olimpiade, UKS), Inklusi Tabel 16, 7 KAIH, PPK & Pembiasaan kultur Kristen Methodist (kebaktian siswa, renungan firman Tuhan, 5S, perayaan Natal/Paskah), Kalender Pendidikan Tabel 19-21 lengkap tanggal SK Kaldik Disdikbud Kota Medan No. 400.3.1/4552.SMP; (5) BAB IV: Ruang Lingkup Satuan Pendidikan & Kelas, Prinsip Pembelajaran & Asesmen, Pendekatan Deep Learning; (6) BAB V: Evaluasi, Pendampingan & Pengembangan Profesional, Matrik Supervisi; (7) BAB VI: Penutup & Daftar Pustaka; (8) Tata Letak: PageBreak pada semua BAB I-VI, keepNext pada semua heading agar tidak menggantung di bawah halaman, 0 sisa titik-titik placeholder. File: `SD KSP 26-27 - DOKUMEN 1.docx` & `TEMPLATE KSP 2026 2027 REVISI BPMP.docx`. Siap diperiksa via Word.
- **Resume session terminal online (21/9):** `linux-tablet/scripts/pilih-terminal.sh` sekarang deteksi session tmux lama (`web-*`) → tawarkan LANJUT (pilih nomor) atau buka baru (`b`). Max terminal 6 → **2**. Auto-cleanup session basi (>12 jam, gak dipakai) + guard opencode tunggal (warning kalau masih ada opencode jalan)
- **Wakelock Termux (21/9):** service runit `/usr/var/service/wakelock/run` diubah jadi `termux-wake-lock; exec sleep 86400` — CPU tetap hidup saat app di-minimize. Battery optimization Termux sudah dimatikan user di HP
- **Koreksi device (21/9):** linux-tablet = **Poco X7 Pro** (HP Xiaomi), bukan "Red Magic Tab Astra 3 Pro". Diperbaiki di MASTER-MEMORY + setup.md
- **Terminal online multi-pilih (21/9):** `linux-tablet/scripts/pilih-terminal.sh` — buka methodist-11.my.id/opencode → menu pilih jumlah terminal (1/2/dst, tmux window) → bisa tambah lagi (Ctrl-b + c). gotty service + start-website.sh sudah pakai script ini; nginx & cloudflared jadi service runit (file `down` dihapus, auto-restart boot)
- **Website balik live (21/9):** methodist-11.my.id → 200 setelah service cloudflared & nginx yang state `down` dihidupkan via runit
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
