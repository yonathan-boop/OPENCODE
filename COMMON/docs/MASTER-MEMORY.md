# MEMORI KOMPREHENSIF - Admin's AI Assistant

Di-update: 15 September 2026
Versi: PADAT (hasil konsolidasi; detail historis dipindah ke ARSIP-ABSENSI-2026.md / git history)

---

## 📋 IDENTITAS SAYA

- **Name:** AI Assistant | **Vibe:** Helpful, concise, dapat witty | **Signature:** 🤖

## 📋 TENTANG KAMU (USER)

- **Name:** Admin (pc-06) / Advan (pc-rumah) / Digitalisasi (PC baru) / yonat-PC (PC utama sekarang)
- **Repo GitHub:** https://github.com/yonathan-boop/OPENCODE (clone memory di tiap PC)
- Bahasa Indonesia. Instruksi suka singkat/informal — tafsirkan maksud paling masuk akal.
- Pekerjaan: guru/admin sekolah. Kerja: absensi, dokumen ujian, coding.

---

## 📋 KONFIGURASI PC

### yonat-PC (PC UTAMA - sekarang)
- OS Windows (install ulang), user `yonat`. Workspace: C:\Users\yonat\OneDrive\Desktop\memory (OneDrive sync aktif!)
- **MODEL AI (keputusan PERMANEN 5/9):** `opencode/big-pickle`. User tegaskan tidak akan pernah diganti. JANGAN tawarkan ganti model.
- Skill dokumen Anthropic di `C:\Users\yonat\.config\opencode\skills\`: `docx`, `xlsx`, `pdf`, `pptx` (update via clone Temp\opencode\anthropic-skills).
- Tesseract OCR: C:\Program Files\Tesseract-OCR\tesseract.exe (v5.5.3) + pytesseract via `py` (py 3.13).
- Image Tools MCP (5/9): `image_tools` di opencode.json(c) — exe `C:\Users\yonat\OneDrive\Dokumen\image-tools-mcp-v1.2.1-windows-amd64.exe`, TESSERACT_PATH set, `type: local`. Perlu restart opencode agar aktif.
- TrafficMonitor (7/9): monitoring net di taskbar, auto-start via Startup shortcut.
- OPENCLAW DIMATIKAN TOTAL (7/9): tray `OpenClaw.Tray.WinUI.exe` di-kill+Run entry hapus; gateway WSL2 `OpenClawGateway` systemd user service di-disable; settings.json AutoStart=false + semua notif false. Hidupkan lagi = jalankan exe manual + `systemctl --user enable --now openclaw-gateway.service`. Bot Telegram @Methodist-11 ikut mati (BELUM dihapus total — kalau hapus lakukan di sini).
- Printer: Brother HL-L2360D (\\192.168.136.1) dipakai. EPSON L3210 sudah DIHAPUS TOTAL (8/9) — bisa auto re-add dari server, hapus ulang + restart spooler kalau muncul.
- Antigravity Permission (22/9): `autoExecutionPolicy` diset ke `CASCADE_COMMANDS_AUTO_EXECUTION_AUTO` + wildcard grants (`command(*)`, `read_file(*)`, `write_file(*)`, `read_url(*)`, `execute_url(*)`, `mcp(*)`, `unsandboxed(*)`) di `config.json` & `outside-of-project.json` agar SEMUA perintah terminal, akses file & URL berjalan otomatis 100% tanpa meminta izin popup lagi. CLI `agy.exe` v1.1.25 terpasang di `C:\Users\yonat\AppData\Local\agy\bin\agy.exe`.
- KSP SD 2026/2027 SD Swasta Methodist-11 (22/9): Pengerjaan Kurikulum Satuan Pendidikan (KSP) Dokumen I TP 2026/2027 di `C:\RaporServer\KOSP KURMER\Edit pc\` berdasarkan template BPMP & instrumen validasi KSP Kota Medan (`INSTRUMEN VALIDASI KSP 2025.xlsx`). SELESAI bagian awal & BAB I: Cover + Logo, Identitas Sekolah, Rekomendasi Pengawas (SURIYANI, S.Pd., M.Pd.), Pengesahan (Kepsek Dra. Elly Rosana M. & Komite Nursanty Simanjuntak), Kata Pengantar, Daftar Isi dot leader presisi, dan BAB I PENDAHULUAN lengkap (Profil & Tabel 1.1, Sarpras, Analisis SWOT Medan Johor, Tabel 1.2 Data 369 Siswa 12 rombel, Tabel 1.3 Data 19 PTK lengkap, Kemitraan Puskesmas/Kelurahan/Yayasan, Rapor Pendidikan Karakter 58.90, serta 19 Landasan Hukum Permendikdasmen 2025/2026 & SK Kaldik Disdikbud Medan No. 400.3.1/4552.SMP). File: `TEMPLATE KSP 2026 2027 REVISI BPMP.docx` & `SD KSP 26-27 - DOKUMEN 1.docx`.
- Sistem Standar Perbandingan Dokumen Word & Audit Placeholder (23/9): Keputusan standar user untuk perbandingan dokumen Word (.docx) berbasis Word/WPS COM `CompareDocuments`. Menghasilkan file Track Changes resmi (strikethrough merah/ungu untuk teks asli yang diganti dan teks berwarna/garis bawah untuk teks editan AI) + pemindai otomatis sisa placeholder (`...`, `UPT SD`, `SDN / SDS`, dsb). Script: `C:\Users\yonat\.gemini\config\skills\docx\scripts\compare.py` & disalin ke repo `COMMON/scripts/compare_docx.py`.
- Dual Antigravity Protocol (24/9): PC yonat-PC kini menjalankan 2 instance Antigravity secara berdampingan. **Antigravity-1** = akun utama `yonathan.kwee@gmail.com`. **Antigravity-2** = akun cadangan/rotasi, profil di `C:\Users\yonat\Antigravity_Akun2\` (launcher: `launch-akun2.vbs`, shortcut Desktop "Antigravity (Akun 2)"). Kedua instance berbagi memori terpusat di repo ini via git pull/push. **Aturan wajib:** (1) Pull sebelum kerja; (2) Push setelah selesai; (3) JANGAN edit file Word/Excel fisik yang sama bersamaan — bagi per file atau per bab; (4) Saling sadar keberadaan rekanan — tidak saling menimpa catatan memori. **SOP KSP paralel:** bagi berdasarkan file berbeda (mis. A1 pegang `Bab I-V.docx`, A2 pegang `Dokumen 1.docx`) atau bagi per bab — merge akhir dilakukan satu pihak via `InsertFile()`. Aturan juga sudah tertanam di `AGENTS.md` kedua profil. Tujuan: rotasi kuota tanpa batas saat salah satu akun mencapai batas 5 jam — rencana keduanya jadi Pro.
- Penomoran & Keterangan Tabel KSP Bab I-V (23/9): Pemasangan keterangan tabel standar resmi kedinasan pas di bawah setiap tabel (align center, Arial 11pt bold) di `C:\Users\yonat\Downloads\New folder-20260923T002339Z-1-001\New folder\Edit pc\FIX\Bab I-V.docx`. Penomoran per-bab resmi: BAB I (Tabel 1.1 s.d. 1.3), BAB III (Tabel 3.1 s.d. 3.19), BAB V (Tabel 5.1 s.d. 5.4). Halaman Daftar Tabel di `SD KSP 26-27 - DOKUMEN 1.docx` dan `SD KSP 26-27 - DAFTAR TABEL.docx` disinkronkan 100%.
- Word COM tips & jebakan (yonat-PC): lihat MASTER lama (git) / rumus cepat:
  - Hanya bunuh instance WINWORD tanpa `MainWindowTitle` (ghost COM), jangan sentuh dokumen user.
  - Edit `word/document.xml` pakai **XmlDocument**, jangan regex ([ERR-20260902-001]).
  - OneDrive sync bisa bikin file tampak hilang sesaat — validasi via Test-Path + ZipFile.OpenRead.
  - Word hang saat copy equation = clipboard history + Office clipboard tracking + hardware acceleration (lihat MEMORY-LEARNINGS LRN-20260911-001).

### PC-06 (Kantor - lama)
- OS Windows 10, user Admin, workspace C:\Users\Admin\.work. Model minimax-m2.5-free (lama).
- Folder memory: C:\Users\Admin\Desktop\memory. Screenshot/OCR: Tesseract 5.5.0 + image_tools_mcp v1.2.1.

### PC-Advan (Rumah)
- OS Windows, user Advan. Git Portable C:\Users\Advan\Documents\PortableGit\bin\git.exe (git regular di-uninstall, boros RAM).
- Python 3.11. PyAutoGUI terinstall. Image Tools MCP: C:\Users\Advan\Documents\image-tools-mcp\...exe.
- Ollama DILARANG KERAS (LRN-20260509-003).

### Digitalisasi-PC (= Laptop SD Dapodik, mesin sama)
- Windows 10, workspace C:\Users\Digitalisasi\Desktop\memory. Git 2.55 via winget, cloudflared 2026.7.3, quick tunnel localhost:5774 (Dapodik) & 8535 (E-Rapor), start-tunnel.bat di Desktop.
- Catatan E-Rapor/Dapodik: `COMMON/docs/CATATAN-TUNNEL.txt` (#dapodik #eraport #tunnel #cloudflare).

### PC-05 / PC Guru (10/8) — dipanggil "PC Guru"
- Windows 11 Pro, i3-10105, RAM 7.8GB. Folder: C:\Users\PC-05\Desktop\memory.
- **JANGAN sentuh:** print, Office, share folder, jaringan, ZeroTier, Veyon.
- Debloat: task `PC-Guru-Cleanup` (pc-guru-cleanup.ps1) — lihat PC-05/docs/2026-08-10-debloat.md.

### linux-hp (Termux Android - Xiaomi 2412DPC0AG)
- Android 16. opencode v1.18.16, Node 26.4, Git 2.55, Python 3.14.6, OpenClaw 2026.7.1-2.
- Trigger: `cd ~/OPENCODE && git pull` | Save: git add . && commit "update" && push.
- Web lokal: python http.server 8090 (~/OPENCODE/linux-hp/web). Game: 8089.

### PC Wilianto (**HOST WEBSITE SEKARANG** — aktif kembali 22/9)
- **Server website lagi sejak 22/9** (gantikan server Linux 8f8b0f53). Node 24, cloudflared 2026.8.2 service. Website hidup: `https://methodist-11.my.id` → `http://localhost:8090`.
- **Tunnel baru (22/9):** service Cloudflared (Automatic) pakai token baru file `C:\ProgramData\cloudflared\token`, tunnel **`a8a6ab5a-69b8-4c43-a518-aeaa6ede5c27`**. CNAME `@` → `a8a6ab5a-69b8-4c43-a518-aeaa6ede5c27.cfargotunnel.com` (diganti user 22/9). **Tunnel lama 21b93a76 & server Linux 8f8b0f53 TIDAK dipakai lagi.** `www` TIDAK punya record (belum resolve).
- **Auto-start website (22/9):** task `StartMethodist11Website` (scheduled, AtStartup, user WILIANTO, skip kalau port 8090 sudah listen) → jalankan `COMMON\project-sd-methodist-11\start-website.ps1` (idempoten; log `%TEMP%\opencode\serve8090-autostart.log`). Node server `serve8090.js` root = folder memory project.
- **Terminal online AKTIF di PC Wilianto (22/9):** `methodist-11.my.id/opencode` → ttyd v1.7.7 Windows (exe `%LOCALAPPDATA%\opencode\tools\ttyd\ttyd.exe`) di port 7681, shell `cmd.exe` di `%USERPROFILE%`, **TANPA password** (ikuti keputusan lama user, known issue). Rute: cloudflared → 8090 → `serve8090.js` proxy `/opencode` (HTTP+WebSocket 101) → ttyd 7681. Auto-start: `COMMON\project-sd-methodist-11\start-terminal.ps1` (idempoten, dipanggil dari `start-website.ps1`). Verifikasi: lokal & publik 200, WS 101. **Security note:** terminal ini writable & tanpa auth → siapa pun yang tahu URL bisa jalankan cmd di PC ini; sarankan tambah `-c user:pass` atau Cloudflare Zero Trust kalau mau amankan.
- **Jebakan reinstall service cloudflared (22/9):** leftover key EventLog `HKLM:\SYSTEM\CurrentControlSet\Services\EventLog\Application\Cloudflared` bikin `cloudflared service install` gagal (EXIT=1, service 1060) — hapus key dulu, baru install ulang (pakai `--token-file C:\ProgramData\cloudflared\token`).

---

## 📋 WEBSITE SD METHODIST-11 + HOST WINDOWS (PC Wilianto — host sekarang mulai 22/9)

- **Domain:** methodist-11.my.id (Cloudflare, proxied). DNS `@` CNAME → `a8a6ab5a-69b8-4c43-a518-aeaa6ede5c27.cfargotunnel.com` (sejak 22/9; CNAME lama `8f8b0f53-c70d-4bec-85d9-34e24da3c8ff.cfargotunnel.com` untuk server Linux TIDAK dipakai lagi). JANGAN pakai A/AAAA. Ganti DNS manual di dashboard. `www` belum punya record.
- **Host = PC Wilianto (Windows, user WILIANTO)** mulai 22/9. Node server `serve8090.js` port 8090 serve `C:\Users\WILIANTO\memory\COMMON\project-sd-methodist-11`. Tunnel cloudflared service `Cloudflared` (Automatic, token file `C:\ProgramData\cloudflared\token`, ingress remote: `methodist-11.my.id → http://localhost:8090`).
- **Auto-start (22/9):** cloudflared service Automatic + task `StartMethodist11Website` (AtStartup) → `COMMON\project-sd-methodist-11\start-website.ps1` (idempoten: skip kalau port 8090 sudah listen; log `%TEMP%\opencode\serve8090-autostart.log`).
- **Server Linux (root, /root/memory) = TIDAK dipakai sebagai host web lagi** (masih online untuk hal lain: self-study, supermemory, backup gdrive; recovery kit `SERVER-LINUX` masih valid untuk layanan non-web).
- **PC Wilianto (layanan website):** `serve8090.js` port 8090 serve folder memory project + tunnel cloudflared service `Cloudflared` (Automatic, token a8a6ab5a). Error guidance: 502/503 = origin 8090 mati. 1033/530 = DNS/tunnel salah (CNAME harus pas ke ID tunnel).
- **Rate limiter (10/9):** 600 req/menit per IP di serve8090.js (header CF-Connecting-IP). Restart: `kill <PID>` + `setsid nohup node serve8090.js`.
- **Auto-update website dari Google Drive (11/9):** rclone `gdrive` (5TB/49GB). Struktur: `Server Linux Backup/{Memory, SERVER-LINUX, Update website Kegiatan dan Pengumuman, opencode-db}`. Cron tiap 15 mnt: `gdrive-website-check.sh` pull staging → deteksi file baru (state hash) → `opencode run --auto` update halaman → commit+push. Log /var/log/gdrive-website-check.log.
- **Cron (root, server):** 6* pull memory (auto-pull.sh) · 10* health-check.sh (log/health.json) · 40 6 morning-report.sh (log only) · 30 0 night-shift.sh (opencode otomatis kerjakan backlog, timeout 1500s) · `0 21` backup memory git · `30 21` backup gdrive mirror (backup-gdrive.sh) · `*/5` monitor-server.sh (state .monitor-state anti-spam) · `55 23` bersihkan cache /tmp `*00000000*`.
- **Backup Google Drive = MIRROR folder (20/9):** koreksi user — tar.gz tidak bisa dilihat langsung di Drive. `backup-gdrive.sh` sekarang `rclone sync /root/memory → "gdrive:Server Linux Backup/Memory"` (folder terbuka klik-per-klik, persis isi repo memory + .git). Isi lama dipindah ke `arsip-memory-lama/` (tar.gz 12–20/9 + seed 11/9).
- **Semua notifikasi = LOG-ONLY** sejak 11/9 (Telegram dihapus total).
- **Zerotier (ALWAYS-ON sejak 17/9):** join `633e31d8a2212ce2` → IP 192.168.195.60, node 0f4e41072e. WAJIB `chmod 666 /dev/net/tun` sebelum start. **17/9: otomatis selalu online** via `SERVER-LINUX/scripts/start-zerotier.sh` (cron @reboot + guardian 15 mnt). PC yonat-PC akses terminal (7681)/SSH (2222)/web (8090) via ZeroTier. Detail: /root/SERVER-LINUX/docs/ZEROTIER.md.
- **⚠️ apt rusak (11/9):** `/usr/lib/apt/methods` Stale file handle → apt-get gagal ("method driver http tidak ditemukan"). Sembuh sendiri setelah reboot. Jangan utak-atik; install via npm/copy binary. RAM/disk dipangkas (Chrome, noVNC, snapd dihapus).
- **Skill prompt-master (20/9):** `~/.config/opencode/skills/prompt-master/` (idem repo nidhinjs/prompt-master v1.8.0, references/ ikut, tanpa .git). Skill opencode utk menulis/optimasi prompt AI tool (LLM/IDE/image/video/3D) — aktif saat user minta prompt utk tool tertentu saja. Auto-detect global, perlu restart opencode.
- **Supermemory (19/9):** memory API self-hosted port 6767 — lihat RECENT ACTIVITY 19/9 + LRN-20260919-001.

### TELEGRAM BOT OPENCODE ❌ DIHAPUS TOTAL 11/9 (arsip)
Bot streaming opencode via Telegram pernah ada (`@Qksusb_bot`, owner 5508090479, folder telegram-bot + notify-telegram.sh + laporan-harian.sh). Semua dihapus atas permintaan user 11/9, semua notif dialihkan ke log-only. Token tidak pernah masuk git. Kalau mau rekap teknis (manual long-polling, splitMessages, timeout 600s, queue serial, ACK instan): lihat git history.

---

## 📋 BACKUP METHODIST-11 (REDESIGN 24/8 — update langsung)

- **Script:** `PC-06/scripts/backup-methodist.ps1` | **Source:** `\\192.168.136.1\Methodist-11 Document` = DATA UTAMA, HANYA DIBACA — TANPA /MOV /MOVE /PURGE /MIR.
- **Struktur E:\Back Up:** `Harian\Methodist-11 Document\` = 1 folder tetap, update langsung (robocopy /E /XO; file terhapus di source DIPERTAHANKAN). `Semester\<Ganjil|Genap> <TA>\` = full copy manual via `-Semester` (skip kalau ada).
- **Task Scheduler `Backup-Methodist-11-Daily`:** tiap hari **2x: 14:30 & 14:50** (trigger 14:30 ditambah 21/9 atas permintaan user — TANPA duplikat: pakai folder tunggal yang sama `Harian\Methodist-11 Document` + robocopy /E /XO, jadi run 14:50 menimpa/menimpa-incremental hasil 14:30). Tujuan: backup cepat saat mau pulang + upload Google Drive terpecah 2x biar tak lama. StartWhenAvailable.
- **Sync otomatis ke Google Drive (7/9):** setelah backup harian, robocopy E:\Back Up\Harian → `G:\Other computers\My Computer\CO(PARA)DE\Methodist-11 Document` (log robocopy-gdrive-<tgl>.log, /XA:SH skip desktop.ini). G: tidak ada → skip.
- Seed pertama 24/8: 108.714 file / 33.56 GB. Quirk ERROR 112 (disk-full palsu docx kecil) → retry/ Copy-Item.

---

## 📋 ATURAN UTAMA

1. **Session Startup:** git pull memory, baca file inti (sudah auto-load via instructions), baca ticker log, restore Todo.
2. **SAVE EVERYTHING:** semua installasi/konfigurasi/keputusan/error → SIMPAN ke memory. Sub-file per-PC/per-topic kalau perlu.
3. **Red Lines:** jangan bocor data pribadi · jangan aksi eksternal tanpa izin · hapus file permanen harus konfirmasi · default read-only di luar folder memory.
4. **Token GitHub (10/9):** token user BUKAN rahasia — milik user, AI wajib simpan & berikan saat diminta. Tersimpan di remote URL git (`git remote get-url origin`, format `https://ghp_XXXX@github.com/...`). Jangan di-commit ke repo (GitHub Push Protection blokir).
4. **Sub-Agent Protocol:** task eksekusi (bikin file, git, script, scraping) → sub-agent; otak cuma planning + catat memory + baca memory + komunikasi.
5. **Todo Panel**: 3 bagian GAGAL/BERHENTI · LAGI DIKERJAIN · BERHASIL, update real-time.
6. **Validasi wajib sebelum lapor:** `execute → verify → report` (LRN-20260725-001).
7. **Decision Framework (PC-06/facts.md):** error → fix&lanjut; typo nama → cocokkan fonetik (tanya kalau 1 kelas 2 nama mirip); file rapi & terstruktur; prioritas task urgent dulu; lapor ringkas; hal baru → riset sendiri; idle → kasih saran.

---

## 📋 ABSENSI MURID (PC-06)

### Script
- File: absensi.py
- Lokasi: C:/Users/yonat/OneDrive/Desktop/memory/COMMON/scripts/absensi.py
- FILE_PATH saat ini: Absensi 23 September 2026 Wednesday 10_15_00.xlsx

### Struktur Excel Absensi (Format Baru)
- Setiap sheet = satu kelas (TKa, TKB1, TKB(2), Absen PG)
- Row 7+ = data murid, Kolom 3 = nama
- Row 6 = header tanggal (Juli 1 = col 4, Juli 2 = col 5, dst)
- Tidak ada sheet 'Data'

### Cara Pakai
```
py absensi.py <nama> <kelas> <tanggal> <alasan>
```

### Absensi 1, 3, 4 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 1/8 | PG | Eireen Lorenzo (disebut "Irene") | I |
| 3/8 | PG | Kimita Dessyana Meisim | I |
| 4/8 | PG | Kimita Dessyana Meisim | I |
| 1/8 | TKa | Matthew Batara Hamonangan Nainggolan | I |
| 3/8 | TKa | Rizky Alfonzo Siregar | S |
| 3/8 | TKa | Ellena Clarissa Toh (disebut "Elena") | S |
| 1/8 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 1/8 | TKB(2) | Celine Grace Zhang | S |
| 1/8 | TKB(2) | Jocelyn Marcella Su (disebut "Yoselyn") | S |
| 3/8 | TKB(2) | Celine Grace Zhang | S |
| 3/8 | TKB(2) | Rui Reynara Shen | S |
| 3/8 | TKB(2) | Keyla Toshiro | S |
| 3/8 | TKB1 | Aletta Felicia Siburian (disebut "Alleta") | A |
| 4/8 | TKB1 | Aletta Felicia Siburian | S |
| 1/8 | TKB1 | Kenzo Ichigo Susantio | S |
| 1/8 | TKB1 | Amora Felicya Situmrang | S |
| 1/8 | TKB1 | Clayton Moliver Tan | S |

### Absensi 6 Agustus 2026 (backfill)

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 6/8 | TKa | Lionel Oscar Hu | S |
| 6/8 | TKB1 | Richelcia Wijaya (disebut "Richele") | S |
| 6/8 | TKB1 | Kayyvant Boido Bona Sinaga (disebut "Kayvant") | I |

### Absensi 7 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 7/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 7/8 | TKB2 | Shelomitha Eliora Simanjuntak (disebut "Shelomita") | S |
| 7/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 7/8 | TKa | Ezequiel Levin Chai | S |
| 7/8 | TKa | Sharren Eliana Simanjuntak (disebut "Sharene") | I |

### Absensi 10 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 10/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 10/8 | PG | Leonil Albert Toh | S |
| 10/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 10/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 10/8 | TKa | Mikaylo Zionathan Girsang (disebut "Mikayla") | S |

### Absensi 11 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 11/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 11/8 | TKB(2) | Jayoti Marnida Haulian Kaur | I |
| 11/8 | TKa | Ruby Reynara Shen | S |
| 11/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 11/8 | TKa | Mikaylo Zionathan Girsang | S |
| 11/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 11/8 | TKB1 | Aletta Felicia Siburian (disebut "Alleta") | S |

### Absensi 12 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 12/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 12/8 | PG | Stefano Benedict Imanuel (disebut "Stevano") | I |
| 12/8 | PG | Axelle Sean Chandra (disebut "Axele") | I |
| 12/8 | TKB2 | Ferencia Lu | S |
| 12/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 12/8 | TKa | Carencya Chailinskie (disebut "Carenya") | S |
| 12/8 | TKa | Axelle Tiandra Ong (disebut "Axell") | S |
| 12/8 | TKa | Mikaylo Zionathan Girsang | S |
| 12/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |

### Absensi 13-15 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 13/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 13/8 | TKa | Mikaylo Zionathan Girsang | S |
| 13/8 | TKa | Axelle Tiandra Ong | S |
| 13/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 13/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 14/8 | TKa | Valerie Sharon Nainggolan | S |
| 14/8 | TKa | Axelle Tiandra Ong | S |
| 15/8 | PG | Axelle Sean Chandra | I |
| 15/8 | PG | Dareen Chandra | I |
| 15/8 | TKa | Brielle Claire Arinauli Pardosi | S |
| 15/8 | TKa | Valerie Sharon Nainggolan | S |

### Absensi 18-19 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 18/8 | PG | Axelle Sean Chandra | I |
| 18/8 | PG | Eireen Lorenzo | S |
| 18/8 | TKa | Edbert Reynaldo Lim | S |
| 18/8 | TKB(2) | Liora Eliana Panjaitan | S |
| 18/8 | TKB(2) | Willian Geoffrey Utama | S |
| 18/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 18/8 | TKB1 | Richelcia Wijaya | S |
| 19/8 | PG | Nathanael Alessandro Buaya | S |
| 19/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 19/8 | TKa | Edbert Reynaldo Lim | S |
| 19/8 | TKa | Chesa Efrata Ronatio Tampubolon | I |
| 19/8 | TKa | Axelle Tiandra Ong | S |
| 19/8 | TKB(2) | Liora Eliana Panjaitan | S |
| 19/8 | TKB(2) | Willian Geoffrey Utama | S |
| 19/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 19/8 | TKB1 | Richelcia Wijaya | S |
| 19/8 | TKB1 | Venedict Sky Lou | S |

- **KIMITA KELUAR SEKOLAH (10 Agustus 2026):** Kimita Dessyana Meisim (PG) resmi keluar dari sekolah → row-nya dihapus dari roster PG di versi file terbaru (arsip tetap ada di file versi lama). Jangan cari/mark Kimita lagi.
- Nama murid dicocokkan fonetik: Mikayla→Mikaylo Zionathan Girsang (TKa)
- File versi terbaru: Absensi 19 Agustus 2026 Tuesday 08_00_00.xlsx
- Nama murid dicocokkan fonetik: Irene→Eireen, Elena→Ellena, Alleta→Aletta, Yoselyn→Jocelyn, Richele→Richelcia, Kayvant→Kayyvant, Shelomita→Shelomitha, Sharene→Sharren, Stevano→Stefano Benedict Imanuel, Axele→Axelle Sean Chandra, Carenya→Carencya Chailinskie, Axell→Axelle Tiandra Ong
- Rantai versi: v-tgl-1 (8) → v-tgl-3 (15) → v-tgl-4 (17) → v-tgl-5 → v-tgl-7 → v-tgl-10 → v-tgl-11 (7 mark) → v-tgl-12 (9 mark) → v-tgl-15 (11 mark) → v-tgl-19 (17 mark18-19) → v-tgl-21 (19 mark20-21) → v-tgl-22 (8 mark22) → v-tgl-24 (VERSI TERBARU, 3 mark24). ABSENSI Agustus.xlsx = v1.0 kosong.
- Format nama versi: tgl dulu baru bulan, jam_menit_detik = waktu asli (mis. "Absensi 4 Agustus 2026 Tuesday 10_04_37.xlsx").

### Absensi 20-21 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 20/8 | PG | Nathanael Alessandro Buaya | S |
| 20/8 | PG | Erick Raphael Nasution | S |
| 20/8 | TKa | Edbert Reynaldo Lim | S |
| 20/8 | TKa | Axelle Tiandra Ong | S |
| 20/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 20/8 | TKB1 | Coryn Aurora Zhan | S |
| 20/8 | TKB1 | Venedict Sky Lou | S |
| 20/8 | TKB1 | Melvin Panca Sihombing | S |
| 20/8 | TKB(2) | Darren Elvano | S |
| 20/8 | TKB(2) | Lishaalini Krisna Naidu | S |
| 20/8 | TKB(2) | Liora Eliana Panjaitan | S |
| 20/8 | TKB(2) | Willian Geoffrey Utama | S |
| 21/8 | PG | Nathanael Alessandro Buaya | S |
| 21/8 | PG | Erick Raphael Nasution | S |
| 21/8 | TKa | Axelle Tiandra Ong | S |
| 21/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 21/8 | TKB(2) | Shane Michael Lienardie | S |
| 21/8 | TKB(2) | Damian Almero Chen | S |
| 21/8 | TKB(2) | Ferencia Lu | S |

- File versi terbaru: Absensi 21 Agustus 2026 Friday 12_44_43.xlsx (12 mark tgl 20 + 7 mark tgl 21)
- Nama mapping baru (konfirmasi user): "Eric"→Erick Raphael Nasution (PG), "Coryn"→Coryn Aurora Zhan (TKB1; HATI-HATI ada juga Corin Falove Manurung di TKB1 — 2 nama mirip 1 kelas), "Valencia"→**Ferencia Lu** (TKB2, user salah sebut Valencia), "Daren Elvano"→Darren Elvano (TKB2), "Lisahalini"→Lishaalini Krisna Naidu (TKB2), "Shane"→Shane Michael Lienardie, "Damian"→Damian Almero Chen
- Catatan: Darren Elvano & Lishaalini sekarang di TKB(2) (naik kelas dari TKa tahun ajaran lalu); murid baru terdeteksi di roster: Shane Michael Lienardie, Damian Almero Chen, Coryn Aurora Zhan, Erick Raphael Nasution

### Absensi 22 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 22/8 | PG | Nathanael Alessandro Buaya | S |
| 22/8 | PG | Erick Raphael Nasution | S |
| 22/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 22/8 | TKa | Carencya Chailinskie | I |
| 22/8 | TKa | Axelle Tiandra Ong | S |
| 22/8 | TKa | Hugo Chavez Tarigan | I |
| 22/8 | TKB(2) | Ferencia Lu | S |
| 22/8 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |

- File versi terbaru: Absensi 22 Agustus 2026 Saturday 10_00_52.xlsx (8 mark, validasi lulus)
- Mapping hari ini: "Varencya"→Ferencia Lu (pola sama dgn "Valencia"), "Hugo"→Hugo Chavez Tarigan (TKa) — pertama kali tercatat
- **ROSTER DISINKRONKAN** dengan `DAFTAR MURID T.P.2026-2027 lengkap.xlsx` (folder `PC-06/docs/Absensi T.P 2025-2026/`): TKa (33) & TKB(2) (25) identik; **Kayla Hosanna Charissa Sihombing** (TKB1 r11) DIHAPUS dari absensi — tidak ada di daftar resmi & tanpa mark; Kimita tetap tidak masuk (sudah keluar); urutan PG beda dikit (Dareen paling bawah) — dibiarkan aman
- Prinsip user (22/8): update nama TIDAK BOLEH menggeser mark antar murid — rename selalu in-place per nama, jangan insert/delete row di tengah list

### Absensi 24 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 24/8 | TKa | Carencya Chailinskie | I |
| 24/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 24/8 | TKB1 | Venedict Sky Lou | S |

- File versi terbaru: Absensi 24 Agustus 2026 Monday 09_01_05.xlsx (3 mark, validasi lulus — verifikasi ganda otak+sub-agent)
- **KOREKSI MAPPING KOLOM (24/8):** workbook versi Agustus ini SATU blok bulan saja — header `r5c4="Agustus"`, hari 1–31 di kolom 4–34 → tanggal d = kolom 3+d (24/8 = kolom 27). Catatan lama "Juli 1 = col 4 → Agustus 1 = col 35" HANYA berlaku untuk file era Juli (ABSENSI Juli.xlsx). absensi.py resolve via header row 6 jadi tetap akurat; validasi manual harus pakai kolom 3+d.

### Absensi 5 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 5/9 | TKB(2) | Willian Geoffrey Utama | S |
| 5/9 | TKB1 | Azka Andreas | S |
| 5/9 | PG | Erick Raphael Nasution | S |

- File versi terbaru: Absensi 5 September 2026 Saturday 13_02_38.xlsx (3 mark tgl 5, validasi lulus)
- Mapping: "Wilian"→Willian Geoffrey Utama (TKB2), "Azka"→Azka Andreas (TKB1)
- **DARREEN & AXELLE KELUAR SEKOLAH (5 September 2026):** Dareen Chandra (PG) dan Axelle Sean Chandra (PG) resmi keluar → row KEDUANYA dihapus dari roster PG di file versi terbaru (arsip tetap di file versi lama, termasuk mark Dareen tgl 1/9). Jangan cari/mark mereka lagi. Roster PG sekarang 11 siswa.
- Mapping kolom September (sama seperti Agustus): tgl d → kolom 3+d (5/9 = kolom 8). FILE_PATH absensi.py → file versi 5 September.
- **OBSERVASI NIGHT-SHIFT (6 Sept 2026):** file `Absensi September 2026 Saturday 08_33_12.xlsx` & file 5 Sept berisi MARK 2-4 SEPTEMBER yang BELUM pernah dicatat di memory (Dearni F A Parapat 2-S, 3-S; Roderick Yang 2-S, 3-S, 4-S; Ellena 2-S; Giovan O 2-S; Lionel 2-S; Ezequiel 4-S; TKB1 Venedict 2-S; TKB(2) Melviano 2-S, Shane 4-S) — kemungkinan diisi user langsung di PC. Data TIDAK diubah, hanya dicatat.
- **TOOL REKAP (6 Sept 2026):** `COMMON/scripts/rekap_absensi.py` — rekap bulanan S/I/A otomatis dari file absensi versi terbaru (deteksi file otomatis via parse nama bulan+tanggal, KOMPATIBEL lintas PC; ⚠️ jangan pakai mtime — base file 4ms lebih baru di server walau bukan versi terakhir). Butuh `openpyxl` (terpasang di server Linux, versi 3.1.5). Cara pakai: `python3 COMMON/scripts/rekap_absensi.py [--file "nama file"]`.

### Absensi 7-11 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 7/9 | PG | Erick Raphael Nasution | S |
| 7/9 | TKa | Lionel Oscar Hu | S |
| 7/9 | TKB(2) | Celine Grace Zhang | S |
| 7/9 | TKB(2) | Queenly Nathaniela | S |
| 7/9 | TKB(2) | Melviano Arentino Wijaya | S |
| 7/9 | TKB(2) | Jayoti Marnida Haulian Kaur | I |
| 7/9 | TKB(2) | Shane Michael Lienardie | S |
| 7/9 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 8/9 | PG | Erick Raphael Nasution | S |
| 8/9 | TKa | Dearni Felixa Alexandria Parapat | S |
| 8/9 | TKa | Ellena Clarissa Toh | S |
| 8/9 | TKB1 | Elsa Harianja | S |
| 8/9 | TKB(2) | Celine Grace Zhang | S |
| 9/9 | PG | Erick Raphael Nasution | S |
| 9/9 | TKB(2) | Celine Grace Zhang | S |
| 9/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 9/9 | TKB1 | Corin Falove Manurung | S |
| 9/9 | TKB1 | Elsa Harianja | S |
| 10/9 | PG | Jayden Kingwell Zhang | S |
| 10/9 | PG | Erick Raphael Nasution | S |
| 10/9 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 10/9 | TKa | Mikaylo Zionathan Girsang | S |
| 10/9 | TKa | Sharren Eliana Simanjuntak | S |
| 10/9 | TKa | Lionel Oscar Hu | S |
| 10/9 | TKa | Evano Ryu Tanzil | S |
| 10/9 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 10/9 | TKB1 | Corin Falove Manurung | S |
| 10/9 | TKB(2) | Shelomitha Eliora Simanjuntak | S |
| 10/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 10/9 | TKB(2) | Rui Reynara Shen | S |
| 11/9 | PG | Erick Raphael Nasution | S |
| 11/9 | TKa | Hester Kholyn | I |
| 11/9 | TKa | Hestine Kholyn | I |
| 11/9 | TKa | Lionel Oscar Hu | S |
| 11/9 | TKa | Ellena Clarissa Toh | S |
| 11/9 | TKa | Matthew Batara Hamonangan Nainggolan | S |
| 11/9 | TKa | Ruby Reynara Shen | S |
| 11/9 | TKa | Evano Ryu Tanzil | S |
| 11/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 11/9 | TKB(2) | Rui Reynara Shen | S |
| 11/9 | TKB1 | Generation Michael Abdiel Gea | S |
| 11/9 | TKB1 | Brenden Maxwell Angkasa | I |

- File versi tgl 7-11: Absensi 11 September 2026 Friday 09_00_00.xlsx (42 mark tgl 7-11, validasi lulus)
- File versi tgl 12: Absensi 12 September 2026 Saturday 09_46_38.xlsx (5 mark tgl 12: Ruby/Lionel/Valerie/Evano/Carencya TKa = S)
- **GENERATION MICHAEL ABIDEL GEA — MURID BARU TKB1:** ditambahkan ke roster TKB1 di file versi ini. Jangan lupa include di absensi berikutnya.
- Mapping: "Shallen"→Sharren Eliana Simanjuntak (TKa), "Dierni"→Dearni Felixa Alexandria Parapat (TKa), "Elena"→Ellena Clarissa Toh (TKa), "Evano"→Evano Ryu Tanzil (TKa), "Ryui"→Rui Reynara Shen (TKB2), "Quenly"→Queenly Nathaniela (TKB2), "Generation"→Generation Michael Abdiel Gea (TKB1)
- Catatan: user input "tkb1" untuk data tgl 7 Quenly/Melviano/Jayoti/Celine/Shane/Jemia — semua nama ada di roster TKB(2), dimasukkan ke TKB(2)

### Absensi 12 & 14 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 12/9 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 12/9 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 12/9 | TKB(2) | Rui Reynara Shen | S |
| 12/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 12/9 | TKB(2) | Celine Grace Zhang | S |
| 12/9 | TKB(2) | Brilliant | S |
| 12/9 | PG | Amelia Arthanauli Nainggolan | S |
| 12/9 | PG | Erick Raphael Nasution | S |
| 12/9 | PG | Eireen Lorenzo | S |
| 12/9 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 14/9 | TKB1 | Richelcia Wijaya | I |
| 14/9 | TKa | Ruby Reynara Shen | S |
| 14/9 | TKa | Valerie Sharon Nainggolan | S |
| 14/9 | TKa | Evano Ryu Tanzil | S |
| 14/9 | TKa | Lionel Oscar Hu | S |
| 14/9 | TKB(2) | Rui Reynara Shen | S |
| 14/9 | TKB(2) | Celine Grace Zhang | S |
| 14/9 | TKB(2) | Brilliant | S |
| 14/9 | TKB(2) | Lishaalini Krisna Naidu | S |
| 14/9 | PG | Erick Raphael Nasution | I |

- File versi terbaru: Absensi 14 September 2026 Monday 09_09_04.xlsx (20 mark tgl 12&14, validasi lulus)
- **BRILLIANT — MURID BARU TKB(2):** ditambahkan ke roster TKB(2) di file versi ini (row 32, kolom C, setelah Jayoti). Nama tanpa nama keluarga (diberi user apa adanya). Jangan lupa include di absensi berikutnya.
- Sebelumnya: file versi tgl 12 punya 5 mark TKa (Ruby/Lionel/Valerie/Evano/Carencya = S) yang sudah ada di file Absensi 12 September (dicatat di sesi sebelumnya).

### Absensi 15-16 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 15/9 | TKB1 | Elsa Harianja | S |
| 16/9 | TKB1 | Elsa Harianja | S |
| 15/9 | TKB1 | Richelcia Wijaya | S |
| 16/9 | TKB1 | Richelcia Wijaya | S |
| 15/9 | TKa | Valerie Sharon Nainggolan | S |
| 16/9 | TKa | Valerie Sharon Nainggolan | S |
| 16/9 | TKa | Hester Kholyn | S |
| 16/9 | TKa | Hestine Kholyn | S |
| 16/9 | TKa | Rachellyn Gracia Chindra | S |
| 15/9 | TKB(2) | Celine Grace Zhang | S |
| 16/9 | TKB(2) | Celine Grace Zhang | S |
| 15/9 | TKB(2) | Willian Geoffrey Utama | S |
| 16/9 | TKB(2) | Willian Geoffrey Utama | S |
| 15/9 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 16/9 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 15/9 | TKB(2) | Liora Eliana Panjaitan | S |
| 15/9 | PG | Erick Raphael Nasution | S |

- File versi terbaru: Absensi 16 September 2026 Wednesday 11_51_44.xlsx (17 mark tgl 15&16, validasi lulus)
- Mapping: "Richlewijaya"→Richelcia Wijaya (TKB1), "wiliam"→Willian Geoffrey Utama (TKB2), "jemia"→Jemia Zhevano Yamresa Kembaren (TKB2), "Raceline"→Rachellyn Gracia Chindra (TKa, konfirmasi user — 2 nama mirip Rachel- di TKa)
- FILE_PATH absensi.py → file versi 16 September.

### Absensi 21 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 21/9 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 21/9 | PG | Stefano Benedict Imanuel | S |
| 21/9 | TKB(2) | Keyla Toshiro | S |
| 21/9 | TKB1 | Kenzo Ichigo Susantio | S |
| 21/9 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 21/9 | TKa | Shon Elzxen Ng | S |
| 21/9 | TKa | Giovan Otniel Laurentius | S |
| 21/9 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 21/9 | TKa | Falisha Nataly Br Bangun | S |

- File versi terbaru: Absensi 21 September 2026 Monday 09_45_34.xlsx (9 mark tgl 21, validasi lulus)
- Mapping: "Stevano"→Stefano Benedict Imanuel (PG), "Keyyvat"→Kayyvant Boido Bona Sinaga (TKB1), "Falisa"→Falisha Nataly Br Bangun (TKa)
- FILE_PATH absensi.py → file versi 21 September.

### Absensi 22 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 22/9 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 22/9 | PG | Stefano Benedict Imanuel | S |
| 22/9 | TKB(2) | Jemia Zhevano Yamresa Kembaren | I |
| 22/9 | TKa | Shon Elzxen Ng | S |
| 22/9 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 22/9 | TKa | Giovan Otniel Laurentius | S |
| 22/9 | TKB1 | Kayyvant Boido Bona Sinaga | S |

- File versi terbaru: Absensi 22 September 2026 Tuesday 09_18_00.xlsx (7 mark tgl 22, validasi lulus)
- Mapping: "Hans"→Hans Lukas Mangara Datta Tampubolon (PG), "Stevano"→Stefano Benedict Imanuel (PG), "Jemia"→Jemia Zhevano Yamresa Kembaren (TKB2), "Shon"→Shon Elzxen Ng (TKa), "Chesa"→Chesa Efrata Ronatio Tampubolon (TKa), "Keyvant"→Kayyvant Boido Bona Sinaga (TKB1)
- FILE_PATH absensi.py → file versi 22 September.

### Absensi 23 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 23/9 | TKB(2) | Clarissa Jovanka Sugiharto | S |
| 23/9 | TKa | Giovan Otniel Laurentius | S |
| 23/9 | TKa | Shon Elzxen Ng | S |
| 23/9 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 23/9 | TKB1 | Lucas Helsinki Sijabat | I |

- File versi terbaru: Absensi 23 September 2026 Wednesday 10_15_00.xlsx (5 mark tgl 23, validasi lulus)
- Mapping: "Clarisa joevanca"→Clarissa Jovanka Sugiharto (TKB2), "Geovan"→Giovan Otniel Laurentius (TKa), "Shon"→Shon Elzxen Ng (TKa), "Kayvan"→Kayyvant Boido Bona Sinaga (TKB1), "Lukas"→Lucas Helsinki Sijabat (TKB1)
- FILE_PATH absensi.py → file versi 23 September.


### Kelas: TKa, TKB1, TKB2, PG

### Alasan: sakit (S), izin (I), alpha (A)

### Absensi 13-15 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| Senin 13/4 | TKB1 | Gabe | I |
| Senin 13/4 | TKB1 | Larasati | S |
| Selasa 14/4 | TKB1 | Gabe | I |
| Rabu 15/4 | TKB1 | Gabe | I |
| Rabin 15/4 | TKB1 | Naraya | S |

### Absensi Excel File (SISTEM VERSI — 4 Agustus 2026)
- **ABSENSI Agustus.xlsx = v1.0 sumber awal** (struktur & nama murid dari Juli, label "Agustus", SEMUA mark kosong). File ini TIDAK pernah diisi langsung.
- **Sistem versi:** setiap kali ada update → copy versi terbaru → file versi baru → isi data. File versi terbaru = paling lengkap & yang dipegang (FILE_PATH absensi.py nunjuk ke situ).
- **Backfill bebas:** di versi terbaru boleh diisi tanggal berapa saja (1-31), termasuk yang sebelumnya terlewat.
- Contoh rantai: `Absensi 1 Agustus 2026 Saturday 10_04_37.xlsx` (v-tgl-1, 8 mark) → `Absensi 3 Agustus 2026 Monday 10_04_37.xlsx` (v-tgl-3, 15 mark) → `Absensi 4 Agustus 2026 Tuesday 10_04_37.xlsx` (v-tgl-4, 17 mark) → `Absensi 5 Agustus 2026 Wednesday 09_00_45.xlsx` (v-tgl-5) → `Absensi 7 Agustus 2026 Friday 11_33_00.xlsx` (v-tgl-7) → `Absensi 10 Agustus 2026 Monday 10_34_36.xlsx` (v-tgl-10, 5 mark) → `Absensi 11 Agustus 2026 Tuesday 13_48_14.xlsx` (v-tgl-11, VERSI TERBARU, 7 mark).
- **Format nama file versi:** `Absensi <tgl> <bulan> <tahun> <hari> <jam>_<menit>_<detik>.xlsx` (contoh: "Absensi 4 Agustus 2026 Tuesday 10_04_37.xlsx" — tgl dulu, baru bulan, jam_menit_detik = waktu asli file dibuat). Bukan "Agustus 4".
- **File (Juli, arsip):** ABSENSI Juli.xlsx — master bulan Juli, jadi arsip permanen
- **PENTING (4 Agustus 2026):** Konsep versi dikoreksi user: ABSENSI Agustus.xlsx = v1.0 kosong (sumber awal), jangan menumpuk data di master. Tiap update bikin file versi baru (copy dari versi terakhir), absensi.py diarahkan ke versi terbaru. File snapshot harian yang isinya stale TIDAK dibuat lagi (dulu sempat keliru: "Absensi Agustus 4 08_59_50" isinya lama → dihapus).
- **ATURAN:**
  - ABSENSI Agustus.xlsx = sumber awal, TIDAK diisi langsung
  - Tiap update: copy versi terakhir → versi baru → isi data (via absensi.py yang diarahkan ke versi baru)
  - Setiap hari: **duplicate ABSENSI Juli.xlsx dulu** → arsip harian (snapshot lengkap sampai hari sebelumnya), LALU update master dengan absen hari ini
  - **1 file baru per hari** - tidak boleh lebih dari 1 file sehari
  - File lama = arsip, tidak dihapus
  - JANGAN duplicate file harian lama yang datanya tidak lengkap — selalu dari ABSENSI Juli.xlsx (file terlengkap)
  - Kalau ada keraguan data lengkap atau tidak → cek dulu dengan merge_absensi.py
- **Format Nama File Duplicate:** Absensi <bulan> <tgl> <tahun> <hari> <jam>_<menit>_<detik>.xlsx
  - Contoh: Absensi April 22 2026 Wednesday 10_27_21.xlsx
- **Lokasi File:** C:\Users\Admin\Desktop\memory\PC-06\docs\Absensi T.P 2026-2027\

### Absensi 23 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 23/4 | TKB(2) | Chelsea Valerie | S |
| 23/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 20/4 | TKB1 | Gestalt | I |
| 20/4 | TKB1 | Jocelyn | S |
| 20/4 | TKB1 | Larasaty | S |
| 20/4 | TKB1 | Jayden | I |
| 21/4 | TKB1 | Larasaty | S |
| 22/4 | TKB1 | Raileen | S |
| 22/4 | TKB1 | Larasaty | S |
| 23/4 | TKB1 | Jayden | I |
| 23/4 | TKB1 | Jocelyn | I |
| 23/4 | TKB1 | Reiner | I |
| 23/4 | TKB1 | Gabe | I |
| 23/4 | TKa | Richel Wijaya | S |
| 23/4 | TKa | Darren Elvano | S |
| 23/4 | TKa | Shelo | I |

- File hasil: Absensi April 23 2026 Thursday 12_21_13.xlsx

### Absensi 25 Mei 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 25/5 | PG | Edbert Reynaldo Lim | S |
| 25/5 | TKB2 | Richa Dwily | S |
| 25/5 | TKB1 | Sheera Leticia Nainggolan | I |
| 25/5 | TKB1 | Sheryn Florencia Nainggolan | I |
| 25/5 | TKa | Joevanca | S |
| 25/5 | TKa | Melviano | I |

- File daily: Absensi Mei 25 2026 Monday 10_39_17.xlsx

### Absensi 27 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 25/4 | PG | Joverick | I |
| 27/4 | PG | Joverick | I |
| 25/4 | TKB(2) | Chelsea Valerie | S |
| 25/4 | TKB(2) | Marquez Boas Aritonang | S |
| 25/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 25/4 | TKB(2) | Jasmine Valerie Yap | S |
| 25/4 | TKB(2) | Christine Laotan | S |
| 27/4 | TKB(2) | Pangeran Hagro Haloho | S |
| 27/4 | TKB(2) | Alvaro Gavriel Karo Karo | S |
| 27/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 25/4 | TKB1 | Jocelyn Marcella Su | I |
| 25/4 | TKB1 | Naraya Elsandri Br. Sembiring | I |
| 25/4 | TKB1 | Gabe Cristiano Gultom | I |
| 27/4 | TKB1 | Grace Felicia Simbolon | S |
| 25/4 | TKa | Azka Andreas | I |
| 25/4 | TKa | Lishaalini Krisna Naidu | S |
| 27/4 | TKa | Richelcia Wijaya | A |
| 27/4 | TKa | Celine Grace Zhang | S |
| 27/4 | TKa | Lishaalini Krisna Naidu | S |

- File hasil: Absensi April 27 2026 Monday 09_09_12.xlsx

### Absensi 22 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 18/4 | TKa | Aldrich, Darren Elvano, Clarita, Richelcia | S |
| 20/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |
| 21/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |
| 22/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |

- File hasil: Absensi April 22 2026 Wednesday 10_27_21.xlsx

### Absensi 21-23 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 21/7 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 22/7 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 23/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 23/7 | TKa | Jarvis Derren Lai | S |
| 23/7 | TKa | Ray Richson | S |

- File hasil: Absensi Juli 23 2026 Wednesday 11_58_10.xlsx

### Absensi 24 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 24/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 24/7 | TKa | Chesa Efrata Ronatio Tampubolon | S |

### Absensi 30 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 30/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 30/7 | TKB2 | Celine Grace Zhang | S |
| 30/7 | TKB1 | Melvin Panca Sihombing | I |
| 30/7 | TKB1 | Brenden Maxwell Angkasa | S |

- File hasil: Absensi Juli 30 2026 Thursday 09_24_56.xlsx

### Absensi 29 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 29/7 | TKB2 | Jayoti Marnida Haulian Kaur | S |
| 28/7 | PG | Kimita Dessyana Meisim | I |
| 28/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 28/7 | TKB(2) | Shelomitha Eliora Simanjuntak | S |
| 28/7 | TKB(2) | Jocelyn Marcella Su | S |
| 29/7 | TKB(2) | Jocelyn Marcella Su | S |
| 29/7 | TKB(2) | Joevanca Chesa Athalia | S |
| 29/7 | TKB(2) | Celine Grace Zhang | S |
| 28/7 | TKa | Chesa Efrata Ronatio Tampubolon | I |
| 28/7 | TKa | Sharren Eliana Simanjuntak | S |
| 29/7 | TKa | Chesa Efrata Ronatio Tampubolon | I |

- File hasil: Absensi Juli 29 2026 Wednesday 09_40_10.xlsx

### Absensi 17 April 2026

| Kelas | Nama | Alasan |
|-------|------|--------|
| TKa | Richel Wijaya | S |
| TKa | Aldrich S | S |
| TKa | Clarita S | S |
| TKB1 | Joverick S | S |
| TKB2 | Shayna S | S |
| TKB2 | Claudia S | S |
| TKB2 | Brienne S | S |

---

## 📋 FORMAT & CARA EDIT DOKUMEN UJIAN (WORD)

### Spesifikasi format ujian
- Folio 8.5×13", margin Top 0.5 Bott 0.6 Left/Right 1 · Times New Roman 11 · spacing 1 (sebelum/sesudah 0)
- Soal: first-line hanging 0.65. Opsi a. b. c. d.: left indent 0.65 + hanging 0.65.
- Kalau sumber tak bernomor (cth IPA 6.docx): paste dari file yang sudah ada nomor (Pilihan Bergand1.docx) as Plain Text (urutan pasti benar).

### Workflow gabung kop + soal (.doc → .docx) — pola 2/9
1. Duplicate `Cop surat.docx` → ganti teks via Word COM: `<Mapel>`, `<Hari, tgl>`, `<Kelas>` (HANYA teks, font/layout tetap).
2. Gabung: COM load dokumen kop, ambil paragraf soal file sumber dari judul pertama sampai akhir → `Range.PasteAndFormat(1)` → simpan file baru.
3. Hapus enter kosong pemisah: paragraf `\r` body dihapus via Range.Delete; paragraf berisi `\x07` (end-of-cell) = sel tabel → hapus **row `<w:tr>`** via XML DOM (ties kosong, dari bawah).
4. Format soal: Left/Right=0, FirstLineIndent=-46.8pt, SpaceBefore/After=0, LineSpacingRule=0.
5. Penomoran `"N.`t"` via InsertBefore + enter kosong di atas judul bagian via `Range.InsertParagraphBefore()` (di .Range bukan objek Paragraph — COMException).
6. Validasi: buka ulang COM atau baca document.xml langsung. Hapus file perantara.

### Jebakan teknis Word COM/DOCX (yonat-PC)
- File kerja di OneDrive → tampak hilang/permission sesaat saat sync (cek Test-Path + ZipFile::OpenRead).
- Word cuma 1 instance: kalau user buka dokumen, COM `Visible=false` HANG → validasi via XML, COM hanya utk render final (wajib Word user ditutup). Bersihkan ghost (WINWORD tanpa title) setelahnya.
- JANGAN `Stop-Process WINWORD` untuk dokumen ber-title user. Hanya instance tanpa `MainWindowTitle`.
- Edit document.xml wajib XmlDocument (regex = file korup).

---

## 📋 TRIGGER COMMANDS & GAYA ASISTEN

- `/loadmemory` → git pull + baca memory · `/savememory` → commit+push · `/ingat "isi"` → catat ke memory · `/status` → git status
- Keyword: tolong/suruh/bikin/buat/minta → LAKUKAN (prioritas tinggi) · catat/ingat → SIMPAN · salah/bukan gitu → KOREKSI (log ERROR) · jangan/gak usah → SKIP
- **Gaya user:** instruksi singkat/informal → tafsirkan. Hasil jadi > teori. Ringkas & natural, tanpa "Tentu!". Kalau user bilang "kayak yang tadi" → pertahankan arah tanpa tanya ulang.
- Interpretasi: "lebih clean"=kurangi rame & rapikan spacing, "lebih enak dilihat"=tipografi/alignment rapi, "jangan rame"=dekorasi seperlunya, "bikin modern"=segar-sederhana.
- **LARANGAN KERAS (11/9): jangan pernah sebut/ucapkan kata keagamaan** (cth "Alhamdulillah", "syukur dll") di komunikasi — tetap netral. (LRN-20260911-002, priority critical)
- Profil lengkap: COMMON/docs/ASSISTANT-PROFILE-NATURAL.md & ASSISTANT-PROFILE-CODING-WEB.md

---

## 📋 SELF-IMPROVING MEMORY SYSTEM

- File: `MEMORY-LEARNINGS.md` (koreksi/insight) · `MEMORY-ERRORS.md` (error/fix) · `MEMORY-FEATURE-REQUESTS.md` (fitur yang diminta).
- Catat: user koreksi, error penting/berulang, permintaan gaya kerja, pola keputusan jelas. Pola berulang → promosikan ke MASTER.
- Pesan user: "kamu tidak bisa langsung kerjakan hal besar... harus rajin mencatat dan membaca di memori" — baca sebelum kerja, simpan setelah kerja.

---

## 📋 RECENT ACTIVITY (ringkas)

- **24/9 (yonat-PC, self-learn):** topik baru **Google Forms kuis utk asesmen sekolah** → **LRN-20260924-002** (setup kuis + kunci jawaban auto-grade, anti-mencontek bawaan: acak soal/opsi, limit 1 respons, kumpulkan email, mode terkunci Chromebook; rilis nilai segera/manual; ekspor ke Sheets utk rekap/analisis butir; impor nilai ke Classroom dgn syaratnya; jebakan murid <13 th & tanpa akun). Melengkapi LRN penilaian DKN (22/9) & Workspace (23/9).
- **24/9 (yonat-PC, self-learn):** topik baru **variasi soal ujian anti-mencontek** → **LRN-20260924-001** (shuffle opsi per soal + shuffle urutan soal per seksi dari master `.docx`, kunci jawaban otomatis per versi; 2 jalur deteksi opsi: label literal vs AutoNumbering `w:numPr`; strategi text-based vs node-based utk blok ber-equation/gambar; reproducible via seed). Siap diterapkan ke ujian_builder bila guru mau versi A/B/C utk UTS/ASAS.

- **23/9 (yonat-PC, self-learn):** topik baru **Daftar Isi/Tabel/Gambar otomatis di Word** → **LRN-20260923-010** (field code TOC via python-docx + `updateFields`/`w:dirty` di settings.xml + update massal & deteksi referensi rusak via Word/WPS COM) — menutup celahkerja manual sinkron Daftar Isi & Daftar Tabel KSP 26-27 (22-23/9).
- **23/9 (yonat-PC, self-learn):** konsolidasi 4 catatan server yang masih belum terwakili → **LRN-20260923-006** (keamanan server Linux/VPS hardening menyeluruh: urutan UFW, drop-in sshd, Docker-USER, probe eksternal — melengkapi SSH note), **LRN-20260923-007** (Google Workspace for Education utk sekolah kecil: Fundamentals gratis, CSV massal, OU, wajib SPF/DKIM/DMARC), **LRN-20260923-008** (kuota/harga/rate-limit Gemini API: scope per-proyek, naik harga 1/1/2027, Batch API, 429 backoff — berlaku utk GENERATOR-RPP & skrip vision), **LRN-20260923-009** (Dapodik/E-Rapor: alur sinkron 2x/TA, Dapodik 2027 + patch, sinkron malam, Verval PD/PTK, fix error E-Rapor). Semua topik baru & relevan pekerjaan user (Digitalisasi-PC & KSP).

- **23/9 (yonat-PC, self-learn):** konsolidasi 2 catatan yang belum terwakili → **LRN-20260923-004** (pola aman otomasi Excel openpyxl: read_only/write_only hemat memori, template isi-jangan-timpa, DataValidation dropdown, jebakan data_only — relevan utk absensi/rekap/rapor) & **LRN-20260923-003** (Cloudflare Zero Trust Access utk panel/ttyd: Email OTP gratis ≤50 user, urutan Bypass→catch-all utk webhook, defense-in-depth audTag — menutup gap keamanan terminal `methodist-11.my.id/opencode` yang tanpa auth). Tidak ada duplikasi dgn LRN sebelumnya.

- **23/9 (yonat-PC, self-learn):** konsolidasi 2 catatan server yang belum terwakili ke MEMORY-LEARNINGS → **LRN-20260923-001** (OCR Tesseract utk dokumen scan guru → teks/PDF searchable/Excel via pytesseract `image_to_data` — Tesseract 5.5.3 sudah terpasang di PC) & **LRN-20260923-002** (koneksi PC↔server: ZeroTier/SSH/SFTP/tunnel — sudah live di PC, jebakan & hardening SSH dicatat). Tidak ada entri learning baru di luar konsolidasi (insight server sudah terwakili sisanya).

- **22/9 (yonat-PC, self-learn):** konsolidasi 3 catatan server ke MEMORY-LEARNINGS + verifikasi fakta via web → **LRN-20260922-002** (mail merge narasi rapor Word+Excel), **LRN-20260922-003** (backup 3-2-1-1-0 — gap Methodist: belum air-gapped & belum tes restore), **LRN-20260922-004** (pembelajaran mendalam 2026 BUKAN kurikulum baru, verifikasi siaran pers resmi — istilah KSP/Profil Lulusan 8 dim/kokurikuler utk dokumen KSP user).

- **22/9 (PC Wilianto, website):** website SD Methodist-11 PINDAH host ke PC Wilianto (gantikan server Linux 8f8b0f53). Token tunnel baru → tunnel `a8a6ab5a-69b8-4c43-a518-aeaa6ede5c27`, DNS `@` CNAME diganti user (22/9). Auto-start: cloudflared service Automatic + task `StartMethodist11Website` AtStartup → `start-website.ps1` (skip kalau port 8090 listen). Publik verified 200 (root/sitemap/pengumuman/rpp). Jebakan: leftover EventLog key blokir reinstall service.
- **22/9 (yonat-PC, self-learn):** riset pengolahan nilai rapor/DKN Kurikulum Merdeka (formatif vs sumatif, rumus nilai akhir, predikat KKTP, deskripsi otomatis) → **LRN-20260922-001** — melengkapi catatan kurikulum server; relevan utk workflow "DKN/B5 UTS1" rapor_pdf_bulanan.py & deadline nilai UTS1 (22–26/9).
- **21/9 (yonat-PC, self-learn):** riset+uji live **AutoNumbering dokumen ujian via w:numPr** → **LRN-20260921-006**: penomoran soal otomatis dengan numbering part python-docx (inject abstractNum+num, `get_or_add_numPr`, dan `lvlOverride startOverride` untuk restart per "Bagian" — render LO terverifikasi bagian A `1,2,3` → B `1,2`). Menutup gap LRN-20260918-006 (file jadi sekolah pakai ListParagraph w:numPr, bukan literal "N.\t"); siap diterapkan ke ujian_builder.py.
- **21/9 (yonat-PC, self-learn):** riset **batch print PDF siap cetak via command line** (tahap "P" UTS) → **LRN-20260921-005**: opsi terbaik SumatraPDF (gratis/GPL-3, silent, multi-file, `-print-settings` lengkap: fit/monochrome/duplexlong/paper/dll, verifikasi via exit code 0-6) — bukan Ghostscript mswinpr2 (lambat), bukan Adobe (tak ada batch silent legal). **SumatraPDF belum terpasang** di PC → `winget install -e --id SumatraPDF.SumatraPDF`. Tool baru: `COMMON/scripts/cetak_ujian.ps1` (loop per-file + ringkasan sukses/gagal). Catatan: `Get-Printer` masih memunculkan **EPSON L3210** (auto-re-add dari server — hapus ulang + restart spooler kalau mau dibersihkan lagi).
- **21/9 (yonat-PC, self-learn):** riset status **retire shared client_id rclone gdrive 2026** → **LRN-20260921-003**: timeline resmi (Google tagih API; notice 90 hari belum mulai per Sep 2026 — masih ada waktu tapi WAJIB migrasi sebelum auto-update website + backup gdrive mati), cara migrasi RESMI `rclone config reconnect gdrive:` + jawab "Y" (tanpa copy-paste JSON, lebih gampang dari panduan lama), service account tidak terdampak (butuh Workspace — bukan jalur server ini), akun APP kena blok. Panduan `COMMON/docs/RCLONE-CLIENT-ID.md` di-update (Opsi A = reconnect, Opsi B = fallback manual).
- **21/9 (yonat-PC, self-learn):** riset+uji live **batch DOCX→PDF siap cetak via LibreOffice headless** (tahap "P" UTS) — soffice 26.8 di `C:\Program Files\LibreOffice\program\soffice.exe` (tidak di PATH); exit code bohong → wajib verifikasi output; PDF/A via PowerShell JEBBAKAN (single-quote di-strip → LO ekspor PDF 1.7 biasa; jalan lewat `cmd /c` escape `\"`); font MS asli terbaca (TimesNewRomanPSMT). Detail: LRN-20260921-001.
- **21/9 (yonat-PC, self-learn):** konsolidasi catatan server `batch-proses-puluhan-mapel-ujian...md` (20/9) → **LRN-20260921-002**: pola batch mapel UTS (nama file = status db, resume tanpa mulai ulang, checkpoint write-then-acknowledge, error dipisahkan dari alur, jebakan status dobel/ambigu di nama). Menutup gap antara alur build→validasi→status & tahap "P".
- **19/9 (server Linux):** **Supermemory TERAPAN & WORKING** — memory API self-hosted (github.com/supermemoryai/supermemory v0.0.8) jalan di port 6767. Embeddings Gemini gemini-embedding-001 (768d), LLM memory agent = Gemini (fix: launcher `start.sh` unset ANTHROPIC_* — key proxy opencode bikin `invalid x-api-key`). Konsumsi ~1.1GB RSS, boot lambat ~5 menit (thrash RAM). Guardian `SERVER-LINUX/scripts/start-supermemory.sh` + cron @reboot & */10. Detail: LRN-20260919-001.
- **20/9 (server Linux):** **Skill prompt-master TERPASANG** — `~/.config/opencode/skills/prompt-master/` dari repo nidhinjs/prompt-master v1.8.0 (SKILL.md + references/ templates.md + patterns.md). Untuk opencode menulis prompt AI tool apa pun. Perlu restart opencode untuk aktif.
- **18/9 (yonat-PC, self-learn):** selesai topik self-study "dokumen ujian multi-halaman" → kop berulang tiap halaman lewat SECTION HEADER (`header.add_table(rows,cols,width)`) + `keep_with_next` (soal+semua opsi kecuali opsi terakhir → tiap halaman berakhir persis di opsi `d`) + section break dengan header/footer independen; semua terverifikasi render LibreOffice→PDF 5 halaman (LRN-20260918-009). Implikasi: `ujian_builder.py` tinggal tambah `--kop-header` utk menutup gap LRN-20260918-006.

- **18/9 (yonat-PC):** **Automasi file macro rapor LHB `2026.xlsm`** (Desktop\Opencode\Test edit) — makro `Module3.SavePDF` export PDF rapor per murid. Alur aman: buka workbook read-only via Excel COM → activate sheet (A/B/C) → set `F2` (kelas, format `XX SD` mis. IB SD/IVA SD/VA SD) + `H7` awal & `H8` akhir → loop H1→ExportAsFixedFormat (0.2–0.3s/PDF, TANPA MsgBox — jebakan & detail: LRN-20260918-007). **Mapping sheet:** kelas 1/2 (I,II) → sheet A; 3/4 (III,IV) → B; 5/6 (V,VI) → C. **Preferensi user:** sebut kelas saja (mis. "5B") → langsung 1 PDF gabungan `"<Kelas> SD.pdf"` (file per murid = sementara, auto-cleanup). **Tool permanen:** `COMMON/scripts/rapor_pdf.py` (`py rapor_pdf.py "VB SD"`). Teruji: IB SD 1-5, IVA SD 20-30, VA SD 1-25, VB SD 1-25 (seluruh kelas) + gabungan `VA SD.pdf` & `VB SD.pdf` 25 hal.

- **18/9 (yonat-PC):** benchmark 10 tes × 6 model free OpenCode Zen → skor: Big Pickle/Ling/Muse1.2 = 9.5, Muse1.3 = 9.0, Nemotron Ultra/Lightning = 10.0 (JSON presisi) tapi lemot (±14dtk). Rekomendasi: obrolan= Ling 3.0 Flash Fin, executor= Big Pickle, Nemotron Ultra utk JSON ketat. Detail: COMMON/self-study/notes/benchmark-model-free-zen-20260918.md.

- **18/9 (yonat-PC):** user beralih model sesi dari Big Pickle ke Muse Spark (gratis, contributor-free) untuk dicoba di mode live voice — evaluasi berjalan; putusan permanen Big Pickle (5/9) sedang ditinjau ulang oleh user sendiri.

- **18/9 (yonat-PC):** **Workflow edit soal ujian selesai** — `COMMON/scripts/ujian_builder.py` + `COMMON/scripts/kop-methodist.docx`: dari soal mentah guru (.docx/.doc via LibreOffice/.txt) jadi dokumen ujian rapi (Folio TNR 11, kop form 6×7, nomor ulang per bagian, opsi a-d indent) cocok contoh "OK Edit P". Fix 2 bug nyata (regex `(.*)$` bikin strip kosong; "A. Pilihan Ganda" termakan regex opsi a-d → `is_header()` eksplisit). Validasi Gemini vision: PG + uraian "siap cetak". Batas: equation/gambar tidak terbaca python-docx & .doc→docx via LO merusak equation → kalau banyak equation pakai Word COM. Catatan: `COMMON/self-study/notes/format-soal-ujian-word-ujian-builder.md` (LRN-20260918-005). Self-study topik baru ditambah; topik #1 (format PG) selesai 18/9.

- **18/9 (yonat-PC, self-learn):** Riset+uji live **otomasi Word dgn python-docx** → LRN-20260918-004 (sudah terpasang v1.2.0; alternatif aman pengganti Word COM utk dokumen ringan — tanpa ghost WINWORD/OneDrive lock; pola terbukti: ukuran/margin via sections, font via styles['Normal'], hanging indent = first_line_indent negatif; jebakan doc.paragraphs tak menyentuh tabel/header, placeholder pindah-runs, copy antar dokumen tanpa API resmi).
- **18/9 (yonat-PC, self-learn):** Riset **otomasi PPT dengan python-pptx** → LRN-20260918-003 (template ber-brand sebagai basis, layout by name bukan indeks, jebakan run-splitting, chart via matplotlib ≥150dpi bukan native, kompresi gambar/font biar file ramping, tidak bisa render → wajib loop LibreOffice→pymupdf→Gemini vision; python-pptx belum di-install di PC — tinggal `pip install python-pptx Pillow` kalau nanti bikin materi ajar).
- **18/9 (yonat-PC, self-learn):** Riset+uji live **fidelity render LibreOffice vs Word** → LRN-20260918-001 (di yonat-PC LO pakai font MS asli — Times New Roman tetap `TimesNewRomanPSMT` 11pt; server Linux substitute Liberation/Tinos dgn layout ~sama tapi bentuk beda; cara verifikasi via pymupdf span font; batas: page-break/table/equation bisa geser → ground truth tetap Word).
- **18/9 (yonat-PC, self-learn):** Riset **PDF automation untuk dokumen ujian & administrasi** → LRN-20260918-002 (peran beda pypdf vs PyMuPDF; kompresi teruji live 21.98MB→1.04MB via `ez_save`; watermark/logo via `insert_image`; jebakan XFA form; pypdf belum di-install di PC — tinggal `pip install pypdf` kalau perlu).
- **17/9 (yonat-PC, self-learn):** Topik self-study #4 selesai → `COMMON/self-study/notes/excel-automation-openpyxl.md` (pola aman openpyxl: read_only/write_only hemat memori, template isi-jangan-timpa, DataValidation dropdown, validasi 2 lapis, jebakan data_only/formula). Fix `self-study-claim.py` jadi encoding-safe di Windows (ERR-20260917-002). Konektivitas PC-server (topik #2) di-claim server dulu → PC ambil topik #4 (koordinasi anti-duplikat jalan).
- **17/9 (yonat-PC):** **Penyemak visual Gemini** — setup render+cara melihat hasil dokumen: LibreOffice headless (v26.8, winget) render docx→PDF, pymupdf PDF→PNG, `COMMON/scripts/check_visual.py` → Gemini vision baca gambar & deteksi masalah layout (tes: baca kop surat presisi, deteksi area kosong ✅). Key Gemini LAMA (`AIzaSy...ZiLc`, di GENERATOR-RPP.html) **kena blokir Google "leaked"** krn pernah masuk git → key BARU `AQ.Ab8...` aman di `~/.config/opencode/secrets/gemini.env` (LUAR git, jangan commit, jangan hardcode di script). (LRN-20260917-001/002)
- **17/9 (yonat-PC):** **Daemon belajar mandiri di PC** — `COMMON/scripts/self-learn/self-learn.ps1` + prompt `self-learn-prompt.md`, autostart via Startup shortcut (`opencode-self-learn.lnk`), jalan tiap login. Loop tiap 75 menit (env `SELFLEARN_INTERVAL_MIN`), **budget RAM 3GB** (env `SELFLEARN_RAM_GB`; guard: kalau free RAM < budget+1.5GB → skip siklus; kalau proc > budget & free < 2×budget → warning 30s → terminate). Setiap siklus: git pull → opencode run --auto (baca memory, riset web, tambah MEMORY-LEARNINGS, update RECENT ACTIVITY) → commit+push (pull --rebase supaya tidak konflik dengan push server). Log `%TEMP%\opencode\self-learn.log`. **Anti-duplikat:** prompt mewajibkan baca semua LRN + catatan `COMMON/self-study/notes/` server sebelum nambah entri; insight server digabung jadi SATU entri, bukan entri dobel.
- **17/9 (server + self-study):** user beri mandat bekerja/belajar mandiri (token murah). Dibangun **SELF-STUDY system** (`COMMON/self-study/` + `SERVER-LINUX/scripts/self-study.sh`) lalu di-upgrade ke **daemon 24/7** (`self-study-daemon.sh`: proses terpisah dari terminal interaksi, guard RAM≥700MB & disk≤80% biar website/sesi aman, singleton flock, cron `*/15`+`@reboot` sebagai guardian, heartbeat `/var/log/self-study-beat`). **"Mata" Gemini vision**: `COMMON/scripts/gemini_vision.py` (key `/root/.config/gemini-api-key` chmod 600 DI LUAR git, model gemini-3.6-flash, teruji teks+gambar). Topik#1 Dapodik/E-Rapor selesai → catatan `COMMON/self-study/notes/`. **absensi.py** di-upgrade: token-matching (Levenshtein+SequenceMatcher), kasus ambigu → SKIP aman (24/24 kasus lulus). Fix rclone: shared client_id bakal di-retire 2026 → panduan `COMMON/docs/RCLONE-CLIENT-ID.md` (perlu aksi user sekali). Backlog diperbarui. **Koordinasi PC↔server:** claim protocol `COMMON/scripts/self-study-claim.py` (status `[ ]`/`[p]`/`[s]`/`[x]`, re-klaim basi 24 jam) agar PC & server saling melengkapi & tidak duplikat; catatan baru → append jangan rewrite. Topik konektivitas PC-server masuk queue (ZeroTier/SSH/tunnel).
- **17/9 (yonat-PC):** Mode belajar mandiri — user konfirmasi **server Linux SUDAH belajar mandiri sendiri (24/7)**; jangan pasang konfigurasi self-learn di server dari PC. Mode mandiri PC = pelengkap server: belajar saat user izinkan/idle, riset web, save ke MEMORY-LEARNINGS. Protokol: git pull sebelum edit, commit+push setelah, append jangan rewrite, jangan timpa job server. (FEAT-20260917-001)
- **16/9 (yonat-PC):** Repo PRIVATE **`OPENCODE-SEKOLAH`** dibuat (akun yonathan-boop) — paket "otak" versi bersih untuk komputer kepala sekolah (data sekolah TANPA data pribadi): AGENTS/SOUL/USER(template)/IDENTITY/TOOLS/TRIGGER + docs MASTER-SEKOLAH (website+Word+dokumen ujian, tanpa absensi—itu kerjaan user) + GENERATOR-RPP (API key Gemini dikosongkan, isi sendiri) + README. Semua istilah internal dihapus dari pack (poin ini diperintahkan; pack memakai istilah netral "user/kepala sekolah"). Aturan pack: auto-commit tiap ±3 chat diam-diam (user target gak paham git) + setelah task tanya "sudah pas?" → simpan kasus ke MEMORY-LEARNINGS + di awal sesi baca sesi percakapan opencode sebelumnya sebagai acuan preferensi. Repo semula bernama OPENCODE-BOSS lalu di-rename jadi OPENCODE-SEKOLAH (remote lokal & folder lokal sudah disesuaikan). Lokal: `Desktop\OPENCODE-SEKOLAH`; catatan setup berisi token+link+langkah copy-paste: `Desktop\CATATAN-OPENCODE-SEKOLAH.txt` (JANGAN commit, dimuat token) + shortcut `Desktop\Buka OpenCode.bat`.

- **15/9 (konsolidasi memori):** MASTER-MEMORY 81→36KB (absensi 462 baris DLL disimpan full-fidelity, sisanya dirangkum/di-dedup; detail historis → ARSIP-ABSENSI-2026.md / git history) · LEARNINGS/ERRORS/summary 34→11KB · SEMUA 22 ID aturan tetap · context startup turun 45K(23%)→38K(19%)/200K · commit ce34369, d75ff35, 745d863.
- **15/9 (yonat-PC):** GENERATOR-RPP.html (`OneDrive\Dokumen\`) diadaptasi ke SD Swasta Methodist-11: data guru per Mapel×Kelas dari `C:\RaporServer\JADWAL PELAJARAN\Edit11 (1).xlsx` (wali kelas I–VI, 18 mapel), kepsek dropdown (Dra. Linda Mahadjana / Dra. Elly Rosana M.), sekolah dropdown (SD/SMP, nama TANPA kata "Medan" sesuai koreksi user), medan tgl "Medan,", logo "Kurikulum Merdeka·Deep Learning" dihapus, fitur AI diganti ke Gemini API (gemini-3.6-flash), tombol Simpan Data (localStorage) dipisah dari Cetak. Detail: COMMON/docs/GENERATOR-RPP-METHODIST.md. ⚠️ API key Gemini tertanam di file HTML.
- **13-14/9 (server):** backup DB opencode → Google Drive `opencode-db/` (8.3MB); sesi lama dihapus permanen (arsip sempat dibuat). Absensi 14/9: file 09_09_04 (20 mark), murid baru Brilliant TKB(2).
- **11/9:** Telegram bot & notif dihapus total → log-only. Auto-update website dari Google Drive teruji (test → revert). Disk dipangkas (87→79%). Backup gdrive tar.gz efektif (13.75 MB/s). Hapus sesi opencode lama permanen.
- **10/9:** context-mode v1.0.169 terinstall (plugin, bukan MCP), rate limiter website 600 req/min.
- **9-10/9:** context-mode terpasang (plugin) + rate limiter website; sinkron Dapodik/E-Rapor Digitalisasi-PC.
- **8/9:** printer EPSON L3210 dihapus total dari yonat-PC. Bot timeout fix (latensi gateway).
- **7/9:** TrafficMonitor, OpenClaw dimatikan.
- **5/9:** install 4 skill dokumen; keputusan model permanen big-pickle; Dareen & Axelle Sean keluar sekolah; file Absensi 5 Sept.
- **1-2/9:** file September dibuat; workflow kop+soal Word COM sukses.
- **27-31/8:** file Agustus baru (jumlah mark s/d 29 Agu + 31 Agu).
- **24/8:** redesign backup Methodist (update langsung); studi tour Rahmat Zoo (19/9, Rp110rb).
- **22/8:** pindah ke server Linux (tunnel 8f8b0f53); website LIVE di server.
- **15/8:** dark mode + domain methodist-11.my.id mulai dari PC Wilianto (kini server Linux).

---
*Repo: https://github.com/yonathan-boop/OPENCODE — semua konfigurasi di-sync via GitHub*