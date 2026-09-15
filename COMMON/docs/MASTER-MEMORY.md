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

### PC Wilianto (server website LAMA - tidak dipakai lagi)
- Tunnel 21b93a76 & PC Wilianto tidak lagi melayani website (22/8). Node 24, cloudflared 2026.8.2 service.

---

## 📋 WEBSITE SD METHODIST-11 + SERVER LINUX (host sekarang)

- **Domain:** methodist-11.my.id (Cloudflare, proxied). DNS `@` CNAME → `8f8b0f53-c70d-4bec-85d9-34e24da3c8ff.cfargotunnel.com`. JANGAN pakai A/AAAA. Ganti DNS manual di dashboard.
- **Host = SERVER LINUX** (root, /root/memory, online >5 bulan). Recovery kit repo **`SERVER-LINUX`** di /root/SERVER-LINUX (docs/SERVER-SETUP.md + scripts/start-website.sh — token tunnel di variabel TOKEN).
- **Layanan (setelah reboot jalan `bash ~/SERVER-LINUX/scripts/start-website.sh`):** web `serve8090.js` port 8090 (serve /root/memory/COMMON/project-sd-methodist-11), tunnel utama 8f8b0f53, ttyd port 7681 (admin:Xbq17rwIE7DSj63e), tunnel terminal quick (URL acak, lihat /var/log/cloudflared-terminal.log). TIDAK ada systemd → setsid double-fork.
- **Error guidance:** 502/503 = origin 8090 mati. 1033/530 = DNS/tunnel salah.
- **Rate limiter (10/9):** 600 req/menit per IP di serve8090.js (header CF-Connecting-IP). Restart: `kill <PID>` + `setsid nohup node serve8090.js`.
- **Auto-update website dari Google Drive (11/9):** rclone `gdrive` (5TB/49GB). Struktur: `Server Linux Backup/{Memory, SERVER-LINUX, Update website Kegiatan dan Pengumuman, opencode-db}`. Cron tiap 15 mnt: `gdrive-website-check.sh` pull staging → deteksi file baru (state hash) → `opencode run --auto` update halaman → commit+push. Log /var/log/gdrive-website-check.log.
- **Cron (root, server):** 6* pull memory (auto-pull.sh) · 10* health-check.sh (log/health.json) · 40 6 morning-report.sh (log only) · 30 0 night-shift.sh (opencode otomatis kerjakan backlog, timeout 1500s) · `0 21` backup memory git · `30 21` backup gdrive tar.gz (backup-gdrive.sh) · `*/5` monitor-server.sh (state .monitor-state anti-spam) · `55 23` bersihkan cache /tmp `*00000000*`.
- **Semua notifikasi = LOG-ONLY** sejak 11/9 (Telegram dihapus total).
- **Zerotier (on-demand):** join `633e31d8a2212ce2` → IP 192.168.195.60, node 0f4e41072e. WAJIB `chmod 666 /dev/net/tun` sebelum start. Detail: /root/SERVER-LINUX/docs/ZEROTIER.md.
- **⚠️ apt rusak (11/9):** `/usr/lib/apt/methods` Stale file handle → apt-get gagal ("method driver http tidak ditemukan"). Sembuh sendiri setelah reboot. Jangan utak-atik; install via npm/copy binary. RAM/disk dipangkas (Chrome, noVNC, snapd dihapus).

### TELEGRAM BOT OPENCODE ❌ DIHAPUS TOTAL 11/9 (arsip)
Bot streaming opencode via Telegram pernah ada (`@Qksusb_bot`, owner 5508090479, folder telegram-bot + notify-telegram.sh + laporan-harian.sh). Semua dihapus atas permintaan user 11/9, semua notif dialihkan ke log-only. Token tidak pernah masuk git. Kalau mau rekap teknis (manual long-polling, splitMessages, timeout 600s, queue serial, ACK instan): lihat git history.

---

## 📋 BACKUP METHODIST-11 (REDESIGN 24/8 — update langsung)

- **Script:** `PC-06/scripts/backup-methodist.ps1` | **Source:** `\\192.168.136.1\Methodist-11 Document` = DATA UTAMA, HANYA DIBACA — TANPA /MOV /MOVE /PURGE /MIR.
- **Struktur E:\Back Up:** `Harian\Methodist-11 Document\` = 1 folder tetap, update langsung (robocopy /E /XO; file terhapus di source DIPERTAHANKAN). `Semester\<Ganjil|Genap> <TA>\` = full copy manual via `-Semester` (skip kalau ada).
- **Task Scheduler `Backup-Methodist-11-Daily`:** tiap hari **14:50**, StartWhenAvailable. **1x/hari saja** (backup 11:35 & 14:30 dibatalkan 12/9).
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

## 📋 ABSENSI MURID

### Cara pakai
```
py absensi.py <nama> <kelas> <tanggal> <alasan>   # alasan: S=sakit, I=izin, A=alpha
```
- Script: `COMMON/scripts/absensi.py`. Folder file: `PC-06/docs/Absensi T.P 2026-2027\` (di yonat-PC: OneDrive\Desktop\memory\...).
- Kelas: **TKa, TKB1, TKB2 (ditulis TKB(2) di sheet), PG**.

### Struktur Excel
- Setiap sheet = satu kelas (TKa, TKB1, TKB(2), Absen PG). Row 7+ = murid, kolom 3 (C) = nama. Row 6 = header tanggal. TIDAK ada sheet 'Data'.
- **Mapping kolom:** workbook per bulan = 1 blok bulan → tanggal d = **kolom 3+d** (cth 15/9 = kolom 18). Header r5c4 = nama bulan.
- absensi.py resolve tanggal via header row 6 (tetap akurat).

### SISTEM VERSI (WAJIB — pelanggaran = dimarahi user)
```
SETIAP UPDATE: 1) copy versi terbaru → file versi BARU  2) update FILE_PATH absensi.py
              3) isi data di file BARU  4) validasi (baca ulang, cek sel & tanggal) sebelum lapor
```
- Format nama versi: `Absensi <tgl> <bulan> <tahun> <hari> <jam>_<menit>_<detik>.xlsx` (contoh: "Absensi 15 September 2026 Tuesday 09_00_00.xlsx"). Maks 1 file baru/hari. File lama = arsip (jangan diubah).
- Backfill bebas: boleh isi tanggal berapa saja di versi terbaru.
- **JANGAN rename dengan insert/delete row tengah daftar** — rename in-place per nama, jangan geser mark (prinsip 22/8).

### Status file
- **FILE_PATH saat ini:** `Absensi 14 September 2026 Monday 09_09_04.xlsx` (20 mark tgl 12&14, validasi lulus)
- Tool rekap bulanan: `COMMON/scripts/rekap_absensi.py` (deteksi file terbaru via **parse nama**, BUKAN mtime — base file 4ms lebih baru walau bukan versi akhir). Butuh openpyxl.

### Mapping fonetik (aktif — cek ke roster kalau nama tak ketemu)
Irene→Eireen Lorenzo · Elena→Ellena Clarissa Toh · Alleta→Aletta Felicia Siburian · Yoselyn→Jocelyn Marcella Su · Richele→Richelcia Wijaya · Kayvant→Kayyvant Boido Bona Sinaga · Shelomita→Shelomitha Eliora Simanjuntak · Sharene/Shallen/Shalene→Sharren Eliana Simanjuntak · Stevano→Stefano Benedict Imanuel · Axele→Axelle Sean Chandra (PG, KELUAR) · Carenya→Carencya Chailinskie · Axell→Axelle Tiandra Ong · Mikayla→Mikaylo Zionathan Girsang · Eric→Erick Raphael Nasution (PG) · Coryn→Coryn Aurora Zhan (TKB1; hati-hati Corin Falove Manurung juga TKB1) · Valencia/Varencya→Ferencia Lu (TKB2) · Daren Elvano→Darren Elvano · Lisahalini→Lishaalini Krisna Naidu · Shane→Shane Michael Lienardie · Damian→Damian Almero Chen · Defan→Devan Ivander Siahaan · Corine→Corin Falove Manurung · Brile/Brilie→Brielle Claire Arinauli Pardosi · Axel→Axel Gevariel Manurung (TKa) · Daren→Dareen Chandra (PG, KELUAR) · Wilian→Willian Geoffrey Utama · Azka→Azka Andreas · Dierni→Dearni Felixa Alexandria Parapat · Evano→Evano Ryu Tanzil · Ryui→Rui Reynara Shen · Quenly→Queenly Nathaniela · Generation→Generation Michael Abdiel Gea (TKB1) · Hugo→Hugo Chavez Tarigan · Vinsen/Venedict→Venedict Sky Lou

### Kasus khusus (jangan salah lagi)
- **KIMITA Dessyana Meisim (PG) KELUAR 10/8** → row dihapus dari roster. Jangan cari/mark.
- **DAREEN Chandra & AXELLE Sean Chandra (PG) KELUAR 5/9** → row dihapus. Roster PG sekarang **11 siswa**.
- **MURID BARU:** Shane Michael Lienardie, Damian Almero Chen, Coryn Aurora Zhan, Erick Raphael Nasution (terdeteksi 21/8) · Generation Michael Abdiel Gea → TKB1 (11/9) · **Brilliant** (tanpa nama keluarga) → TKB(2) (14/9, row setelah Jayoti).
- **Kayla Hosanna Charissa Sihombing** (TKB1) dihapus 22/8 — tidak ada di daftar resmi.
- Roster disinkronkan dari `DAFTAR MURID T.P.2026-2027 lengkap.xlsx` (folder absensi).
- User input "tkb1" utk data Quenly/Melviano/Jayoti/Celine/Shane/Jemia tgl 7/9 — semuanya ada di roster TKB(2), dimasukkan TKB(2).

> Detail tabel absensi harian (April–14 Sept): **ARSIP-ABSENSI-2026.md**. Rekap per bulan via rekap_absensi.py.

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