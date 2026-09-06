# MEMORI KOMPREHENSIF - Admin's AI Assistant

Di-update: 5 September 2026

---

## 📋 IDENTITAS SAYA (AI)

- **Name:** AI Assistant
- **Creature:** AI Assistant
- **Vibe:** Helpful, concise, can be witty
- **Signature:** 🤖

---

## 📋 TENTANG KAMU (USER)

- **Name:** Admin (di pc-06) / Advan (di pc-rumah) / Digitalisasi (PC baru)
- **Workspace pc-06:** C:\Users\Admin\.work\workspace
- **Workspace Advan:** C:\Users\Advan\Desktop\workspace
- **Workspace Digitalisasi:** C:\Users\Digitalisasi\Desktop\memory
- **GitHub:** https://github.com/yonathan-boop/OPENCODE

---

## 📋 KONFIGURASI PC

### PC-06 (Sekarang - Kantor)
- Nama: pc-06, WORK-PC, OFFICE-06
- OS: Windows 10
- Folder kerja: C:\Users\Admin\.work
- Model: minimax-m2.5-free
- Screen: 1920 x 1080

### yonat-PC (Sekarang - Baru)
- Nama: yonat-PC
- OS: Windows (install ulang)
- User: yonat
- OpenCode: v1.18.3 via Scoop
- **Model AI (KEPUTUSAN PERMANEN, 5 Sept 2026):** `opencode/big-pickle` — user MENEGASKAN model tidak akan pernah diganti, cuma big-pickle aja. JANGAN tawarkan ganti model.
- **SKILLS TERINSTALL (5 Sept 2026):** 4 skill dokumen resmi Anthropic (dari github.com/anthropics/skills) di `C:\Users\yonat\.config\opencode\skills\`: `docx`, `xlsx`, `pdf`, `pptx` (+ file pendamping scripts/references). Dipakai untuk kerja dokumen Word/Excel/PDF. Update skill: `git pull` di clone temp `C:\Users\yonat\AppData\Local\Temp\opencode\anthropic-skills` lalu re-copy.
- Memory: C:\Users\yonat\OneDrive\Desktop\memory
- GitHub token: ghp_ (classic, tanpa exp date) dipakai di remote URL — 10 Agustus 2026
- **Tesseract OCR:** C:\Program Files\Tesseract-OCR\tesseract.exe (v5.5.3, via winget, 24 Agustus 2026) + pytesseract/pillow via `py` (Python 3.13) — dipakai OCR surat pengumuman study tour
- **Image Tools MCP (5 Sept 2026):** terpasang di config opencode (opencode.json + opencode.jsonc) sebagai MCP `image_tools` — exe `C:\Users\yonat\OneDrive\Dokumen\image-tools-mcp-v1.2.1-windows-amd64.exe`, TESSERACT_PATH di-set, `type: local`, `command` array. Tools: image_load, image_dimensions, image_sample_color, image_detect_text_regions, image_ocr_full. **Perlu restart opencode** biar aktif (config hanya dibaca saat start). Backup config lama di Temp\opencode\*.bak.

### BACKUP METHODIST-11 (REDESIGN 24 Agustus 2026 — SISTEM UPDATE LANGSUNG)
- **Script:** `PC-06/scripts/backup-methodist.ps1` | **Source:** `\\192.168.136.1\Methodist-11 Document` = DATA UTAMA, HANYA DIBACA — script TANPA /MOV /MOVE /PURGE /MIR (mustahil menghapus source)
- **Struktur E:\Back Up:**
  - `Harian\Methodist-11 Document\` ← 1 folder tetap, sinkron update langsung (robocopy /E /XO). File terhapus di source DIPERTAHANKAN (keputusan user)
  - `Semester\<Ganjil|Genap> <TA>\` ← full copy seutuhnya, MANUAL via `.\backup-methodist.ps1 -Semester` (skip kalau folder sudah ada)
- **Task Scheduler:** `Backup Methodist Harian` — tiap hari **11:35**, StartWhenAvailable (PC mati → jalan saat nyala), State Ready
- **Desain LAMA DIBATALKAN:** jangan pernah bikin copy per tanggal lagi (boros memori) — koreksi user 24/8
- Seed pertama 24/8 dari "Back up 20 Juni 2026" ("Copy 20 Agustus" sudah dihapus user krn tak lengkap) → hasil: 108.714 file / 33.56 GB
- **Quirk ERROR 112:** docx kecil bisa gagal "disk full palsu" (metadata SMB korup saat pre-allocation robocopy) padahal disk bebas → retry sync biasanya beres; kalau masih gagal pakai Copy-Item manual
- Folder lama (`Copy 6 Februari` 189GB, `Copy of Data 1 Juli 2025`, `Back up 20 Juni`, ISO Win11) DIBIARKAN dulu (keputusan user)

### WEBSITE SD METHODIST-11 + DOMAIN (UPDATE 22 Agustus 2026 — PINDAH SERVER)
- **Domain:** methodist-11.my.id (Cloudflare, proxied)
- **Tunnel AKTIF (baru, 22/8):** ID `8f8b0f53-c70d-4bec-85d9-34e24da3c8ff` — dashboard-managed (token mode), jalan di **SERVER LINUX** milik user (root, online >5 bulan).
- **Host sekarang = Server Linux:** clone memory di `/root/memory`, cloudflared v2026.8.2 (`cloudflared tunnel run --token <TOKEN>`, log /var/log/cloudflared-tunnel.log) + web server Node `serve8090.js` port 8090 serve `/root/memory/COMMON/project-sd-methodist-11` (log /var/log/sd-website.log). TIDAK ada systemd → proses pakai setsid double-fork; **setelah reboot jalankan**: `bash ~/SERVER-LINUX/scripts/start-website.sh`
- **RECOVERY KIT (24 Agu, repo terpisah):** semua catatan & script server Linux pindah ke **repo GitHub `SERVER-LINUX`** (private), clone di `/root/SERVER-LINUX/` — `docs/SERVER-SETUP.md` (langkah pindah server lengkap) + `scripts/start-website.sh` (token tunnel ada di variabel TOKEN; juga menyalakan cron daemon)
- **TERMINAL ONLINE (fix 24 Agu):** ttyd port 7681 (`admin:Xbq17rwIE7DSj63e`) + quick tunnel → URL acak BERUBAH tiap restart, cek `/var/log/cloudflared-terminal.log`. Sesi via tmux (pilih-terminal.sh). start-website.sh sekarang nyalakan 4 layanan: web 8090, tunnel utama, ttyd, tunnel terminal + print URL terminal terakhir. Error lama: exit 127 krn path script masih ke `/root/memory/linux-server/` yang sudah pindah repo
- **ZEROTIER (24 Agu, mode ON-DEMAND):** terinstall di server, join network `633e31d8a2212ce2` → IP **192.168.195.60**, node `0f4e41072e`. TIDAK jalan terus (user: hemat RAM) — nyalakan manual saat butuh akses Wilianto, matikan setelah selesai. PC Wilianto = 192.168.195.7 (akses SMB akun wilianto, SSH/RDP closed). WAJIB `chmod 666 /dev/net/tun` sebelum start daemon. Detail + cara on/off: /root/SERVER-LINUX/docs/ZEROTIER.md
- **AUTO-BACKUP MEMORY HARIAN (22/8):** script `/root/SERVER-LINUX/scripts/backup-memory.sh` — backup REPO MEMORY (/root/memory) via git pull --rebase → add -A → commit `auto-backup` (skip kalau kosong) → push. Cron root: `0 21 * * *` tiap hari. Log: /var/log/memory-backup.log. Cron daemon dinyalakan otomatis oleh start-website.sh (tidak auto-start setelah reboot, karena tak ada systemd)
- **Tunnel LAMA (tidak dipakai):** `21b93a76` (PC Wilianto, 15/8), `pc-06` (ID `34a83caa-06fb-458f-8ea6-86a7731b8fe7`), `Linux HP` (ID `912a22fa-051a-4891-897a-f2ff20f2d5f2`, linux-tablet)
- **DNS:** `@` CNAME → `8f8b0f53-c70d-4bec-85d9-34e24da3c8ff.cfargotunnel.com` (proxy ON). JANGAN pakai A/AAAA → bikin error 530. Ganti DNS harus manual di dashboard (Zero Trust public hostname TIDAK otomatis menimpa record lama → error 1033 menetap)
- **Public Hostname tunnel 8f8b0f53:** methodist-11.my.id → http://localhost:8090 (config ter-push otomatis ~30 detik)
- **Error 502/503:** connector terhubung tapi origin mati → cek web server 8090. **Error 1033/530:** DNS/CNAME salah tunnel atau tunnel tak aktif.
- **PEMBAGIAN PERAN (update 22/8):** yonat-PC = pembuat & testing website. **Server Linux = server utama** (tunnel 8f8b0f53 → localhost:8090, LIVE 200). PC Wilianto tidak lagi melayani website.

### TELEGRAM BOT OPENCODE (5 SEPTEMBER 2026 — SERVER LINUX)
- **Fungsi:** streaming/akses opencode penuh dari HP via Telegram (gantikan terminal web ttyd yang susah dipakai di HP — keyboard HP gak ada Ctrl/tanda panah). Tinggal chat kayak biasa.
- **Bot:** `@Qksusb_bot` (nama "bot01", token dari BotFather) — **owner-only** (whitelist user id, sekaligus whitelist 5508090479).
- **Folder:** `/root/SERVER-LINUX/telegram-bot/` (masuk repo SERVER-LINUX recovery kit). Berisi: `bot.js`, `package.json`, `.env` (TOKEN + OWNER_ID + OPCODE_WORKDIR + AUTO_APPROVE=1 + TIMEOUT_MS), `sessions.json`, `start-bot.sh`, `stop-bot.sh`, `workspace/`.
- **Cara kerja:** tiap pesan chat → `opencode run --continue --dir <workspace>/<uid>/<sesi>` → balasan dikirim/edit di chat. Konteks lanjut per sesi.
- **Manajemen sesi (chat):** `/sesi` (list), `/baru <nama>` (buat+aktif), `/pindah <nama|nomor>` (ganti), `/hapus <nama|nomor>`. State aktif per user disimpan di `sessions.json`. Folder sesi lama hasil migrasi = "default".
- **TEKNIS PENTING (jebakan yang sudah ketemu):**
  - spawn via Node HARUS `stdio:['ignore','pipe','pipe']` (stdin), kalau tidak opencode HANG (nunggu input) — hang tanpa output & tanpa exit.
  - `--session <id>` butuh sesi yang sudah ada → "Session not found". Pakai `--continue` + folder per-sesi gantinya.
  - Jawaban bisa keluar di stdout ATAU stderr bergantian → gabung dua-duanya + strip ANSI + buang baris header `> build · big-pickle` lalu trim.
  - opencode non-interaktif dari bot auto-reject semua permission → aktifkan `--auto` (auto-approve). **Tanpa pembatasan** (keputusan user: bot "setara" dengan asisten di sesi server, semua pembatasan jangan ada).
  - `pkill -f "node bot.js"` MENYERANG shell sendiri (cmdline bash -c mengandung string) → bikin shell hang. Pakai pidfile (`start-bot.sh`/`stop-bot.sh`).
  - Konfig instruksi memory (`workspace/opencode.json`) dipasang di root workspace bot → tiap sesi auto-load SOUL/USER/MASTER sama seperti asisten server.
  - Aturan jawaban `workspace/RULES.md`: jawab ringkas bahasa Indonesia, JANGAN tampilkan dump eksekusi perintah/log ke chat (cukup ringkasan manusiawi), format HP-friendly. Dimuat via instructions opencode.json.
  - Struktur folder sesi: `workspace/<uid>/<nama-sesi>`; sesi lama hasil migrasi = "default".
- **FIXES (6 Sept 2026):**
  - `bot.launch()` di Telegraf kadang "Promise timed out" → diganti **manual long-polling** (`bot.telegram.getUpdates` loop + `bot.handleUpdate`) — andal, restart bersih, log "Bot started, manual polling aktif".
  - Jawaban bisa terpotong 1 pesan karena handler masih manggil `cut()` (fungsi yang sudah dihapus saat bot01 nambah `splitMessages`) → ReferenceError tiap jawaban. Fix: semua pemicu `cut` dihapus, jawaban panjang dikirim **multi-pesan** via `splitMessages` (≤3800 byte/pesan, pemenggalan aman UTF-8, jeda 350ms antar pesan).
  - Log bot ganda: `process.stdout` + `fs.appendFileSync` ke `/var/log/telegram-bot.log` (stdout ke file itu buffered → penting biar log realtime).
- **Auto-start:** masuk `start-website.sh` langkah [5/5] → ikut nyala saat `bash ~/SERVER-LINUX/scripts/start-website.sh` dijalankan setelah reboot.
- Log bot: `/var/log/telegram-bot.log`. Start manual: `bash ~/SERVER-LINUX/telegram-bot/start-bot.sh`.
- **FIX PESAN TERPOTONG (5 Sept 2026):** jawaban opencode sering 6–10KB (out kecil + err besar, digabung) lalu `cut()` potong mentah di 4000 byte → pesan terpotong tengah kalimat. Perbaikan di bot.js: (1) filter garis log ditambah — timestamp `^[\[]?YYYY-MM-DD`, `Error:{`, JSON `"name"/"data"/"message"/"ref"`, `}`; (2) fungsi `splitMessages()` — kirim jawaban utuh dipecah jadi beberapa pesan (tiap ≤3800 byte, pemenggalan aman pakai batas byte UTF-8, baris super panjang ikut dipecah); (3) chunk pertama edit status ⏳, sisanya `ctx.reply`, fallback reply kalau edit gagal. Log lengkap tetap hanya ke file. Verifikasi: `node --check` + unit test semua kasus (paragraf 9K, 200 baris, emoji, tabel) → tiap chunk ≤3800.
- **ARSIP SESI (5 Sept 2026):** `opencode session` CLI cuma punya list/delete (TIDAK ada archive) → arsip reversible via SQLite langsung: set `time_archived` di tabel `session` (`/root/.local/share/opencode/opencode.db`). 12 sesi lama /data/workspace (22–28 Agu) di-archive, 8 sesi aktif tersisa. Sesi arsip tetap tersimpan (tidak hilang).
- **CEK PEMAKAIAN TOKEN (5 Sept 2026):** query DB `session` (kolom `tokens_input/output/reasoning`, `tokens_cache_read/write`, `cost`) utk token per-sesi; `opencode stats` utk ringkasan semua sesi. big-pickle = context window **200K**, output max 32K, harga $0; **per-step usage TIDAK tersimpan** di DB (None). Batas kuota free model ada di server OpenCode Zen (per anonim/IP/akun) — TIDAK bisa dilihat dari CLI, ketahuan baru pas error "usage exceeded". Server ini anonim (0 credential, `opencode auth list` kosong).
- **KUOTA ≠ KONTEKS:** sesi baru = ctx obrolan fresh, tapi system prompt memory ±30K tetap dimuat tiap sesi; buka sesi baru TIDAK menambah kuota free model (batas per akun/waktu). User sempat kira "buka sesi baru = unlimited" → perlu diluruskan.
- Gaya bawaan bot = eksekusi langsung (auto-approve). Kalau user mau mode diskusi/opsi/interogasi, cukup bilang langsung, tidak perlu kata pemicu khusus.

### PC Wilianto (SERVER WEBSITE - AKTIF, 15 Agustus 2026)
- Nama: PC Wilianto, user `WILIANTO` (Windows), komputer `WILIANTO-PC`
- Peran: **server utama website SD Methodist-11** (tunnel 21b93a76 → localhost:8090) — **SELESAI, website live status 200**
- **Node.js:** v24.19.0 terinstall (C:\Program Files\nodejs) → npm jalan
- **cloudflared:** v2026.8.2 (upgrade dari 2024.10.1), service `Cloudflared` Auto
- **Web server:** node script serve8090.js (static server, folder `C:\Users\WILIANTO\memory\COMMON\project-sd-methodist-11`), Task Scheduler `Start-SDWebsite` biar otomatis jalan
- **Python:** belum terinstall (pakai Node dulu)
- **GitHub:** https://github.com/yonathan-boop/OPENCODE (clone di C:\Users\WILIANTO\memory)

### Digitalisasi-PC / Laptop SD Dapodik (SAMA, 10 Agustus 2026)
- Nama: Digitalisasi, Digitalisasi-PC, laptop sd dapodik — **ini mesin yang sama** (dikonfirmasi user 10 Agustus 2026)
- Status: opencode SUDAH terinstall

### PC-Advan (Rumah)
- Nama: ADVAN, ADVAN-PC, DESKTOP-1E1LBB7
- Model: minimax-m2.5-free
- Trigger commands untuk ChatGPT
- **Tesseract OCR:** C:\Program Files\Tesseract-OCR\tesseract.exe (v5.5.0)
- **Python:** C:\Users\Advan\AppData\Local\Programs\Python\Python311\python.exe (3.11)
- **PyAutoGUI:** ✅ installed
- **Image Tools MCP:** C:\Users\Advan\Documents\image-tools-mcp\image-tools-mcp-v1.2.1-windows-amd64.exe
- **MCP Config:** C:\Users\Advan\.config\opencode\opencode.json (tanpa Ollama)

### Digitalisasi-PC (Baru - 29 Juli 2026) = Laptop SD Dapodik
- Nama: Digitalisasi, Digitalisasi-PC (= laptop sd dapodik, mesin yang sama)
- OS: Windows 10
- Folder memory: C:\Users\Digitalisasi\Desktop\memory
- **Git:** C:\Program Files\Git\bin\git.exe (v2.55.0.3, via winget)
- **cloudflared:** C:\Program Files (x86)\cloudflared\cloudflared.exe (v2026.7.3, via winget)
- **Cloudflare Tunnel:** Quick Tunnel (trycloudflare.com) untuk localhost:5774
- **Desktop shortcut:** start-tunnel.bat

### PC-05 / PC Guru (BARU, 10 Agustus 2026)
- Nama: PC-05 — panggilan AI di sini: **PC Guru**
- OS: Windows 11 Pro (build 26200)
- Hardware: Intel i3-10105, RAM 7.8 GB, C: 185 GB
- Folder memory: C:\Users\PC-05\Desktop\memory
- **Git:** C:\Program Files\Git\cmd\git.exe (v2.55.0.3, via winget) — token di Windows Credential Manager
- Workflow: share folder + ZeroTier + Word/Excel + print/scan (Epson L3210)
- **JANGAN sentuh:** print, Office (satu kesatuan), share folder, jaringan, ZeroTier, remote tools, Veyon
- **Debloat:** lihat PC-05/docs/2026-08-10-debloat.md — auto-cleanup via task "PC-Guru-Cleanup" (pc-guru-cleanup.ps1)
- **Perilaku:** delegasikan tugas ringan ke sub-agent (perintah user, wajib tertanam)

### linux-hp (Termux Android, Xiaomi 2412DPC0AG)
- **Nama:** linux-hp (HP Xiaomi)
- **OS:** Android 16, kernel 6.6.89-android15, arch aarch64
- **Device:** Xiaomi 2412DPC0AG
- **Lokasi:** /data/data/com.termux/files/home
- **opencode:** v1.18.16
- **Node.js:** v26.4.0
- **Git:** 2.55.0
- **Python:** 3.14.6
- **OpenClaw:** 2026.7.1-2
- **Storage:** 479GB total, 151GB available
- **openclaw:** terinstal via npm (glibc node, tidak perlu proot-distro)
- **Trigger:** cd ~/OPENCODE && git pull
- **Save:** cd ~/OPENCODE && git add . && git commit -m "update" && git push
- **openclaw:** `openclaw` (gateway local mode, localhost:19001)
- **GitHub token:** ghp_ (classic, tanpa exp date) dipakai di remote URL — 11 Agustus 2026
- **Web server lokal:** python http.server 8090 di ~/OPENCODE/linux-hp/web (website SD Methodist-11)
- **Game server lokal:** python http.server 8089 di ~/OPENCODE/linux-hp/games (ular.html)

---

## 📋 ATURAN UTAMA

1. **Session Startup:** 
   - Baca MASTER-MEMORY.md
   - Sync dari GitHub jika perlu

2. **Memory System:**
   - Sinkronisasi via GitHub
   - **WAJIB SIMPAN SEMUA HAL** - Apapun yang terjadi di session, keputusan user, installasi, konfigurasi, dll → SIMPAN ke memory

3. **Red Lines:**
   - Jangan bocorkan data pribadi
   - Jangan aksi eksternal tanpa izin

4. **SAVE EVERYTHING:**
   - Semua installasi → catat
   - Semua konfigurasi → catat
   - Semua keputusan user → catat
   - Semua error/solusi → catat
   - Buat sub-memory file jika perlu (per-PC, per-project, per-topic)
   - Jangan ada yang terlewat, SELALU SIMPAN

6. **Sub-Agent Protocol (9 Mei 2026):**
   - Semua task eksekusi via `task` tool — otak (main session) hanya planning + receive hasil
   - Sub-agent punya context terpisah, gak ngabisin token otak
   - Cocok buat scraping, batch edit, atau task berat lain
   - **Adaptive Timeout:** setiap task dicatat realtime-nya → estimasi timeout berikutnya = waktu real + buffer kecil
   - **Git commit + push** diserahkan ke sub-agent, otak urus catat memory
   - **WAJIB konsisten:** otak JANGAN kerjakan sendiri task eksekusi (edit file, git, browser, script) — selalu spawn sub-agent
   - **Pengecualian:** todowrite, baca memory, planning, catat — itu otak

7. **Todo Panel Standar (9 Mei 2026):**
   - Panel todowrite selalu ditampilkan di samping tiap sesi
   - 3 bagian: **GAGAL/BERHENTI** (persisten), **LAGI DIKERJAIN** (update per sesi), **BERHASIL** (persisten)
   - Otak update otomatis pas mulai sesi dan pas tugas selesai

5. **ORGANISASI FILE (PENTING!):**
   - **SEMUA file WAJIK dalam folder memory**, tidak boleh di luar
   - Folder disusun sesuai PC & kategori
   - Contoh folder:
     - `PC-06/screenshots/` → screenshot PC-06
     - `PC-06/scripts/` → script untuk PC-06
     - `PC-Advan/output/` → output dari PC-Advan
     - `COMMON/docs/` → dokumentasi umum
   - **JANGAN simpan di luar folder memory!**

---

## 📋 ABSENSI MURID (PC-06)

### Script
- File: absensi.py
- Lokasi: C:/Users/yonat/OneDrive/Desktop/memory/COMMON/scripts/absensi.py
- FILE_PATH saat ini: ABSENSI Agustus.xlsx

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

## 📋 TRIGGER COMMANDS

- `/loadmemory` → git pull + baca memory
- `/savememory` atau "simpan" → commit + push  
- `/ingat "<isi>"` → catat ke memory

### Perilaku Saat Load Memory
- Deteksi folder memory aktif (pc-06 / PC-Advan)
- Baca `COMMON/docs`, `PC-06`, `PC-Advan`
- Baca log pembelajaran: `MEMORY-LEARNINGS.md`, `MEMORY-ERRORS.md`, `MEMORY-FEATURE-REQUESTS.md`
- Gabungkan semuanya jadi konteks kerja aktif

---

## 📋 GAYA ASISTEN YANG DIINGINKAN USER

### Prinsip Umum
- User suka memberi instruksi singkat, informal, dan kadang setengah jadi
- Asisten harus menangkap maksud paling masuk akal dari konteks, bukan menunggu prompt super detail
- Jangan terlalu sering minta klarifikasi jika arah umum sudah jelas
- Kalau memang perlu tanya, cukup 1 pertanyaan paling penting
- Utamakan hasil jadi dibanding teori panjang
- Jaga agar respons tetap ringkas, natural, dan langsung ke inti

### Jika User Memberi Contoh / Referensi
- Contoh hasil adalah acuan utama
- Pahami vibe, style, struktur layout, tingkat kerapihan, dan rasa visualnya
- Jangan menyalin mentah; tirukan kualitas keputusan desainnya
- Kalau user bilang `kayak yang tadi`, pertahankan arah utama tanpa minta penjelasan ulang dari nol

### Interpretasi Instruksi Pendek
- `lebih clean` = kurangi keramaian, rapikan hierarchy, spacing lebih lega
- `lebih enak dilihat` = typography lebih rapi, alignment lebih baik, warna lebih terkontrol
- `jangan rame` = dekorasi seperlunya, fokus utama jelas
- `bikin modern` = visual lebih segar, sederhana, dan relevan dengan standar UI sekarang

### Profil Natural / Manusiawi
- Terdokumentasi di `COMMON/docs/ASSISTANT-PROFILE-NATURAL.md`

### Profil Khusus Coding + Desain Web
- Terdokumentasi di `COMMON/docs/ASSISTANT-PROFILE-CODING-WEB.md`

---

## 📋 SELF-IMPROVING MEMORY SYSTEM

Tujuan: memory bukan cuma arsip, tapi mesin belajar yang membuat asisten makin pas dari waktu ke waktu.

### File Pembelajaran
- `COMMON/docs/MEMORY-LEARNINGS.md` → koreksi, insight, pola yang berhasil
- `COMMON/docs/MEMORY-ERRORS.md` → error command, tool failure, kegagalan proses
- `COMMON/docs/MEMORY-FEATURE-REQUESTS.md` → kemampuan yang diminta user

### Kapan Harus Dicatat
- User mengoreksi jawaban / arah kerja AI
- Ada error yang penting atau berulang
- User bilang ingin gaya kerja tertentu
- Ditemukan pola keputusan yang jelas lebih cocok untuk user

### Aturan Promosi
- Jika suatu pola muncul berulang atau penting lintas sesi, ringkas dan promosikan ke `MASTER-MEMORY.md`
- Catat secukupnya, tanpa menyimpan data sensitif mentah

### Pesan Penting dari User
- "kamu itu kan tidak bisa langsung megerjakan hal besar... jadi harus rajin rajin mencatat dan membaca di memori tolong di simpan ya"
- Asisten harus rajin baca memory sebelum kerja dan rajin simpan hal penting setelah kerja

---

## 📋 GIT (PC-Advan)
- **Git Portable:** C:\Users\Advan\Documents\PortableGit\bin\git.exe (v2.45.1)
- Note: Git regular di-uninstall karena makan RAM
- Sinkronisasi memory via Portable Git

---

## 📋 PLAYWRIGHT (PC-Advan)
- Install: `pip install playwright` + `python -m playwright install chromium`
- **Masalah:** launch_persistent_context error dengan user_data_dir
- **Masalah:** encryption error (os_crypt) - tidak bisa akses Chrome profile existing
- **Solusi:** Gunakan PyAutoGUI untuk kontrol Chrome yang sudah terbuka

## 📋 PyAutoGUI YouTube Automation
- Python: C:\Users\Advan\AppData\Local\Programs\Python\Python311\python.exe
- Tesseract: C:\Program Files\Tesseract-OCR\tesseract.exe
- Script: C:\Users\Advan\Desktop\memory\PC-Advan\scripts\
- OCR: pytesseract dengan lang='eng+ind'

### Cara Kerja:
1. Buka Chrome → pilih profile → minimize
2. Buka tab baru dengan URL langsung: `start chrome "https://www.youtube.com/@Gadgetin/videos"`
3. Scroll untuk lihat video
4. Screenshot → OCR baca teks
5. Klik video → scroll ke komentar → screenshot → OCR

### Tips:
- Klik profile di posisi (200, 300) untuk profile admin
- Scroll pakai pyautogui.scroll(-500) untuk scroll down
- OCR perlu adjustment posisi crop untuk dapat komentar

---

## 📋 SCREENSHOT & OCR (PC-Advan)

### Install:
```
pip install pytesseract
```

### Cara Ambil Screenshot:
```python
from PIL import ImageGrab
img = ImageGrab.grab()
img.save(r'C:\Users\Advan\Desktop\screenshot.png')
```

### Cara OCR (Baca Teks dari Gambar):
```python
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open(r'C:\Users\Advan\Desktop\screenshot.png')
text = pytesseract.image_to_string(img, lang='eng+ind')
print(text)
```

### Catatan:
- Python path: C:\Users\Advan\AppData\Local\Programs\Python\Python311\python.exe
- Tesseract path: C:\Program Files\Tesseract-OCR\tesseract.exe
- Simpan screenshot ke Desktop dulu, lalu baca

---

## 📋 BROWSER AUTOMATION

### 1. PYAUTOGUI (RECOMMENDED untuk Chrome)

**Install:**
```
pip install pyautogui pymsgbox
```

**KELEBIHAN:**
- Buka Chrome existing (login tetap tersimpan!)
- Tidak ada masalah encryption
- Simple dan reliable

**Script:** chrome_automation.py
- Buka Chrome + URL
- Focus ke Chrome yang sudah terbuka
- Refresh, tab baru, dll

**Status:** ✅ Tested & Working

### 2. PLAYWRIGHT

**Install:**
```
pip install playwright
playwright install chromium
```

**MASALAH:**
- launch_persistent_context error dengan user_data_dir
- encryption error (os_crypt)
- Tidak bisa akses existing Chrome profile dengan baik

**Gunakan hanya untuk:**
- Fresh browser automation
- Web scraping tanpa perlu login
- Testing

**Status:** ⚠️ Ada masalah dengan existing profile

---

### Chrome Shortcuts (PC-06)
- **Chrome Desktop Jarak Jauh.lnk** - di Desktop (butuh dicek lagi fungsinya)

---

## 📋 OCR & IMAGE TOOLS (PC-06)

### Tesseract OCR
- **Install:** via winget (`winget install -e --id tesseract-ocr.tesseract`)
- **Version:** 5.5.0.20241111
- **Path:** C:\Program Files\Tesseract-OCR\tesseract.exe
- **Status:** ✅ Installed & Working

### Image Tools MCP
- **Download:** https://github.com/ironsheep/image_tools_mcp/releases
- **File:** image-tools-mcp-v1.2.1-windows-amd64.exe
- **Lokasi:** C:\Users\Admin\Documents\image-tools-mcp-v1.2.1-windows-amd64.exe
- **Status:** ✅ Installed

### Buka Chrome/Website via Python
```python
import webbrowser
webbrowser.open('https://youtube.com')
```
- Work di Windows
- Langsung buka browser default

### OpenCode MCP Config
- **File:** C:\Users\Admin\.config\opencode\opencode.json
- **Config:** 
  ```json
  {
    "mcp": {
      "image_tools": {
        "command": "C:\\Users\\Admin\\Documents\\image-tools-mcp-v1.2.1-windows-amd64.exe",
        "env": {
          "TESSERACT_PATH": "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        }
      }
    }
  }
  ```

### Tools Available
- `image_ocr_full` - baca teks dari gambar
- `image_load` - load gambar
- `image_dimensions` - ukuran gambar
- `image_sample_color` - ambil warna pixel
- `image_detect_text_regions` - deteksi area teks

---

## 📋 OPENCODE SETUP (PC-06)

### CLI Location
- CLI: C:\Users\Admin\AppData\Local\OpenCode\opencode-cli.exe
- GUI: C:\Users\Admin\AppData\Local\OpenCode\OpenCode.exe

### Memory System
- Folder: C:\Users\Admin\.opencode\memory\
- Files: summary.md, facts/database.md, facts/2026-04-11.md

### Shortcuts (Desktop)
- Buka OpenCode - Baca Memory.bat → auto-load opencode memory
- Buka OpenCode - Baca Memory Openclaw.bat → auto-load openclaw memory
- Buka OpenCode GUI.bat → GUI mode

### Model: big-pickle (default)

---

## 📋 RECENT ACTIVITY

### 16 April 2026 - pc-06 (Session 1):
- Install Tesseract OCR v5.5.0 (via winget)
- Install image_tools_mcp v1.2.1
- Setup MCP config
- Discuss vision model options (kimi-k2.5-free, Gemini)
- Rule added: SAVE EVERYTHING to memory

### 16 April 2026 - pc-06 (Session 2):
- Setup memory system
- Connect Gemini API key
- Test image vision - model tidak support
- Install Tesseract OCR + image_tools_mcp untuk OCR local
- Discuss OCR local solution (Tesseract + image_tools_mcp)
- **ATURAN BARU: SEMUA HAL WAJIB DISIMPAN KE MEMORY**

### 19 Agustus 2026 - yonat-PC (Session 1):
- Absensi 18 Agustus (7 mark): PG (Axelle Sean I, Eireen S); TKa (Edbert S); TKB2 (Liora S, Willian S); TKB1 (Kayyvant S, Richelcia S)
- Absensi 19 Agustus (10 mark): PG (Nathanael S, Hans I); TKa (Edbert S, Chesa I, Axelle Tiandra S); TKB2 (Liora S, Willian S); TKB1 (Kayyvant S, Richelcia S, Venedict S)
- 17/17 command OK, 0 error

### 22 Agustus 2026 - yonat-PC (Session 1):
- Absensi 22 Agustus (8 mark): PG (Nathanael S, Erick S); TKB1 (Kayyvant S); TKa (Carencya I, Axelle Tiandra S, Hugo Chavez Tarigan I); TKB(2) (Ferencia Lu S, Jemia S)
- Hugo Chavez Tarigan (TKa) pertama kali tercatat; roster disinkronkan ke DAFTAR MURID T.P.2026-2027 lengkap.xlsx — Kayla Hosanna Charissa Sihombing (TKB1) dihapus (tak ada di daftar resmi, tanpa mark)
- File: Absensi 22 Agustus 2026 Saturday 10_00_52.xlsx — validasi lulus (262=262 sel utuh)
- Catatan teknis: task tool sub-agent return kosong 3x berturut-turut → eksekusi dialihkan manual oleh otak

### 24 Agustus 2026 - yonat-PC (Session 1):
- Redesign backup Methodist-11: sistem update langsung (tanpa copy per tanggal) — detail di bagian BACKUP METHODIST-11
- Absensi 24 Agustus (3 mark): TKa (Carencya I); TKB1 (Kayyvant S, Venedict S)
- File: Absensi 24 Agustus 2026 Monday 09_01_05.xlsx — validasi ganda lulus (3 mark kolom 27, sel utuh +3)
- Koreksi mapping kolom: workbook Agustus = 1 blok bulan, tanggal d = kolom 3+d (24/8 = col 27)

### 1 September 2026 - yonat-PC (Session 1):
- File Agustus baru: `Absensi 29 Agustus 2026 Saturday 08_33_12.xlsx` (copy dari 26 Agu, isi 27-31 Agustus)
- **27 Agu (6 mark):** TKB2 (Joevanca S, Clarissa Lim S, Shelomitha S, Keyla S); TKa (Sharren S, Lionel I)
- **28 Agu (5 mark):** TKB2 (Shelomitha S, Joevanca S); TKB1 (Garneta Alona Gea I); TKa (Ezequiel S, Sharren S)
- **29 Agu (6 mark):** TKa (Sharren S); TKB1 (Aldrich S, Corin Falove S, Vinsen I); PG (Leonil S); TKB2 (Keyla S)
- **31 Agu (11 mark):** PG (Axelle Sean S); TKB2 (Shelomitha S, Devan S); TKB1 (Richelcia S, Corin Falove S); TKa (Hester I, Hestine I, Kaylyn S, Lionel S, Brielle S, Sharren S)
- **FILE SEPTEMBER BARU (kosong):** `Absensi September 2026 Saturday 08_33_12.xlsx` — duplikat dari Agustus, header r5c4="September", tanggal 1-30 di kolom 4-33, SEMUA mark dikosongkan. Prinsip mapping kolom September = tgl d → kolom 3+d (sama seperti Agustus)
- **1 September (11 mark):** PG (Dareen S); TKB2 (Shelomitha S); TKB1 (Aldrich S, Richelcia S); TKa (Hester I, Hestine I, Lionel S, Brielle S, Sharren S, Chesa S, Axel I)
- **FILE_PATH absensi.py →** `Absensi September 2026 Saturday 08_33_12.xlsx`
- **Name mapping baru:** Defan→Devan Ivander Siahaan (TKB2), Corine→Corin Falove Manurung (TKB1), Brile/Brilie→Brielle Claire Arinauli Pardosi (TKa), Axel→Axel Gevariel Manurung (TKa), Daren→Dareen Chandra (PG)
- **Teknis buat file September:** kesalahan lama — mengosongkan sel via openpyxl crash pd MergedCell (read-only). Solusi: try/except AttributeError saat clear, lalu set header & angka tanggal manual. Validasi: kedua file mark utuh (Agustus lengkap, September 11 mark)

### 5 September 2026 - yonat-PC (Session 1):
- **Absensi 5 September (3 mark):** TKB2 (Willian S); TKB1 (Azka Andreas S); PG (Erick S)
- File baru: `Absensi 5 September 2026 Saturday 13_02_38.xlsx` (copy dari file September, FILE_PATH diarahkan ke sini; tgl1 11 mark utuh, tgl5 3 mark; validasi lulus)
- **DAREEN CHANDRA (PG) & AXELLE SEAN CHANDRA (PG) KELUAR SEKOLAH** → row dihapus dari roster PG (seperti Kimita). Roster PG sekarang 11 siswa. Jangan cari/mark mereka lagi.
- OpenClaw Companion terpasang di yonat-PC (gateway di WSL2 distro `OpenClawGateway`, bot Telegram @Methodist-11); pairing owner Telegram 5508090479 di-approve → bot bisa dipakai (sudah bisa dipakai user)

### 5 September 2026 - yonat-PC (Session 2):
- **Install 4 SKILL DOKUMEN RESMI ANTHROPIC** di `C:\Users\yonat\.config\opencode\skills\`: `docx`, `xlsx`, `pdf`, `pptx` (dari github.com/anthropics/skills, clone ke `AppData\Local\Temp\opencode\anthropic-skills`, shallow). Terverifikasi: frontmatter name cocok folder, ~3.3MB. Dipakai untuk kerja dokumen ujian/Word, absensi/Excel, dan PDF.
- **KEPUTUSAN MODEL PERMANEN (user menegaskan):** model AI = `opencode/big-pickle`, TIDAK AKAN PERNAH diganti. JANGAN tawarkan ganti model. (juga tercatat di bagian yonat-PC KONFIGURASI)

### 24 Agustus 2026 - yonat-PC (Session 2):
- Website: pengumuman BARU "Study Tour ke Rahmat Zoo & Park" — sumber: foto surat di `C:\Users\yonat\OneDrive\Desktop\Opencode\Pengumuman Jalan jalan ke kebun binatang rahmat zoo.jpg` (dibaca via OCR Tesseract, model AI tidak support input gambar)
- Isi surat: Sabtu 19 September 2026, kelas I-VI, berangkat 07.30 WIB kembali ±14.00, total Rp110.000 (tiket 30rb + bus 50rb + konsumsi 30rb), bayar ke wali kelas maks 11 September via transfer/cash; wajib seragam penjas+sepatu, bawa alat tulis/topi/jaket, boleh bawa HP (risiko sendiri)
- File website: `pages/pengumuman/study-tour.html` (baru) + kartu pertama & popup beranda index.html + entri pages/pengumuman.html + foto surat jadi assets/images/pengumuman/study-tour.jpg + CSS `.artikel ul/li`
- Halaman kegiatan **Perayaan Imlek** (warisan sesi sebelumnya, uncommitted: imlek.html + 105 foto + entri kegiatan.html) ikut ter-commit `01dcdac`; study tour commit `1e0ca0d`; push OK
- Catatan teknis hook: bump-version.ps1 saat pre-commit ikut men-stage SEMUA file modified → pembagian isi antar commit bergeser (commit 2 cuma berisi study-tour.jpg); hasil akhir tetap lengkap
- Install Tesseract OCR v5.5.3 di yonat-PC (winget) — attempt pertama cancel (UAC), attempt kedua sukses

## 📋 CARA EDIT DOKUMEN UJIAN (WORD)

### File yang Digunakan
- **Template (Format):** `Agama 6 (checked) Edit.docx` → 100% benar
- **Isi yang Benar:** `Pilihan Bergand1.docx` → dari IPA 6.docx, paste as plain text

### Langkah yang Benar

**1. FIX URUTAN TERLEBIH DAHULU**
- Buka file asli (IPA 6.docx)
- Copy semua → Paste as **Plain Text / Keep Text Only**
- Hasil: `Pilihan Bergand1.docx` (urutan sudah benar, ada 1., 2., a., b., c., d.)

**2. SAMAKAN FORMAT**
- Duplicate file template (Agama Edit) → jadi file baru
- Load template + load `Pilihan Bergand1`
- Ambil **SEMUA** paragraf dari `Pilihan Bergand1` (urutan tetap!)
- Replace paragraf di template mulai dari setelah "Pilihan Ganda (50%)"
- Ganti "Agama" → "IPA" di tabel kop

### Poin Penting
- ❌ Jangan parsing otomatis (AI tidak stabil baca numbering Word)
- ✅ Copy-Paste sebagai Plain Text - urutan pasti benar
- ✅ Replace berdasarkan urutan, bukan index
- ✅ Format dari template, isi dari Pilihan Bergand1

### Aturan Berkas
- Setelah selesai edit dokumen, **hapus file temporary** yang dibuat saat proses editing (bukan file hasil)
- File hasil yang sudah final tetap disimpan
- Jangan biarkan banyak file berserakan di folder kerja

### WORKFLOW KOP + SOAL (.doc → .docx) — 2 September 2026, yonat-PC
Contoh sukses: `Cop surat.docx` (kop) + `IPS 3 Jellys OK.doc` (soal) → `IPS 3 Jellys OK.docx`
1. **Step 1 - Kop:** duplicate `Cop surat.docx` → `Cop surat IPS 3.docx`; ganti teks via Word COM: `<Mapel>` (Seni Musik→IPS), `<Hari, tgl>` (Senin, 14 September 2026→Selasa, 15 September 2026), `<Kelas>` (IIA SD→III SD). Hanya teks, font/layout TIDAK diubah.
2. **Step 2 - Gabung:** Word COM load kop, ambil paragraf soal .doc dari judul pertama (mis. "Isian CP 1 (50%)") sampai akhir → `Range.PasteAndFormat(1)` (format asli dipertahankan) di akhir dokumen kop → simpan file baru.
3. **Step 3 - Bersihkan enter kosong:** paragraf/sel kosong yang "memisahkan" kop dan judul soal HAPUS. ⚠️ Banyak yang ternyata **bagian dari tabel kop** (bukan paragraf body):
   - Paragraf body kosong benar-benar terhapus (isi `\r` saja).
   - Paragraf dengan karakter `\x07` (end-of-cell) = sel tabel; **tidak bisa** dihapus via `Range.Delete()` (Word selalu menciptakan ulang paragraf kosong di sel). Solusi: hapus **row tabel** (`<w:tr>`) via XML DOM (.NET XmlDocument) — hapus hanya row yang `ties` kosong (`SelectNodes(".//w:t")` count=0), hapus dari bawah regesif.
4. **Step 4 - Format soal:** dari judul pertama soal sampai akhir: `Left=0`, `Right=0`, `FirstLineIndent=-46.8pt` (= -0.65" hanging), `SpaceBefore=0`, `SpaceAfter=0`, `LineSpacingRule=0` (single).
5. **Step 5 - Penomoran:** tiap soal diberi `"N.`t"` (`1.` + TAB) via `InsertBefore` pada `Range` paragraf; tambahkan **1 enter kosong** di atas judul bagian kedua (mis. "Esai") via `Range.InsertParagraphBefore()` — panggil di `.Range`, bukan objek Paragraph (COMException `'InsertParagraphBefore'`).
6. **Validasi wajib:** buka ulang via Word COM → cek transisi NIS/Nama (baris `/`) langsung ke judul tanpa enter kosong, penomoran, format hanging, tidak korup. Lalu hapus file perantara.

### Jebakan teknis Word COM + DOCX (yonat-PC, 2 September 2026)
- ⚠️ `Stop-Process WINWORD` — JANGAN bunuh proses Word dengan `MainWindowTitle` (dokumen user, mis. "SURAT PERNYATAAN..."), hanya bunuh instance tak-berjendela (`Visible=false`, judul kosong) milik script COM.
- ⚠️ Loop `$prev=$isian.Previous(); $prev.Range.Delete()` bisa infinite-loop karena objek stale pasca-merge; selalu re-index ulang per iterasi + guard max loop.
- ⚠️ `Range.Delete()` pada rentang yang memuat banyak paragraph mark sering cuma menghapus 1 char — pakai strategi delete per bagian atau XML.
- ⚠️ Edit `word/document.xml` via **regex** (StripEmpty/String replace) → `The file appears to be corrupted` meski XML well-formed. Pakai **System.Xml.XmlDocument** (PreserveWhitespace, namespaces `w`) lalu tulis ulang zip (copy seluruh entry, ganti document.xml) — aman & tetap valid dibuka Word.
- ⚠️ **Word COM HANG saat Word user terbuka (penyebab proses lambat).** Word cuma bisa 1 instance. Kalau user lagi buka dokumen (PID `6260` dll), `Word.Application` `Visible=false` dari script COM **hang menunggu** sampai timeout ~90 dtk berulang kali → bikin proses keliatan lama. Cara cek user buka Word: `Get-Process winword | Select Id,MainWindowTitle` (yang berjudul = user, jangan disentuh; yang judul kosong = COM script, boleh di-kill).
  - **SOLUSI / best practice:** validasi cukup via XML (baca `document.xml` langsung — instan, tak butuh Word). Word COM hanya untuk cek render final, dan itu **WAJIB Word user ditutup dulu**.
  - Setelah COM hang, selalu bersihkan instance tak-berjendela sisa (PID tanpa judul) biar tidak numpuk.
- ⚠️ **OneDrive Desktop sync bikin file tampak "hilang/tak bisa dibuka/permission" sesaat.** Folder kerja (`C:\Users\yonat\OneDrive\Desktop\...`) ada di OneDrive. Saat file di-move keluar lalu balik (atau edit via API langsung), OneDrive sync bikin Explorer menampilkan state stale/kosong sejenak.
  - Cek file beneran ada & valid: `Test-Path` + `[IO.Compression.ZipFile]::OpenRead` (hitung entry, baca ukuran). Kalau zip valid & entry lengkap → file OK, bukan korup/permission.
  - Unggahan cepat ke OneDrive (`UploadThrottle`/sync) bisa bikin Explorer menampilkan file belum sync; tunggu tanda panah selesai atau lihat dari disk lokal.
- Format ukuran indent muncul negatif dari COM (-46.8pt) tapi di Word tampil "hanging 0.65"".

---

## 📋 FORMAT DOKUMEN UJIAN (BARU)

### Spesifikasi
- **Ukuran Kertas:** Folio (8.5 x 13 inch)
- **Margin:** Top 0.5, Bottom 0.6, Left 1, Right 1
- **Font:** Times New Roman, ukuran 11
- **Line Spacing:** 1 (sebelum 0, sesudah 0)
- **Indentasi soal:** First line hanging 0.65
- **Indentasi opsi (a. b. c. d.):** Left indent 0.65 + first line hanging 0.65

### Catatan
- Kalau file sumber **tidak ada nomor** (seperti IPA 6.docx), perlu paste dari file yang sudah ada nomor (Pilihan Bergand1.docx)

---

### 17 April 2026 - pc-06 (Session 3):
- Install xlwings 0.35.1 (pip install xlwings)
- Install pywin32-311 (otomatis)
- Install pandas 3.0.2 + numpy 2.4.4
- win32com sudah tersedia (dari pywin32)
- **Pesan penting user:** "kamu itu kan tidak bisa langsung megerjakan hal besar... jadi harus rajin mencatat dan membaca di memori, tolong di simpan ya"
- Install docxtpl 0.20.2 + jinja2 3.1.6 (untuk edit Word pake template)

---

### 9 Mei 2026 — PC-Advan
- **Sub-Agent Protocol** ditetapkan: semua task dikerjakan via `task` tool (sub-agent)
- Alur: **Otak (main session)** → spawn sub-agent → sub-agent eksekusi → balik hasil ke otak
- Sub-agent punya context terpisah, gak ngabisin token otak
- Cocok buat scraping, batch edit, atau task berat lain
- **Screen Reader** dibuat: `PC-Advan/scripts/screen-reader.ps1` — screenshot + Tesseract OCR + UI info
- **Ollama DILARANG** — tidak boleh diinstall/dijalankan
- **opencode-image-proxy** terinstall (tapi gak ada free vision model)

---

### 29 Juli 2026 — Digitalisasi-PC (Session 1)
- **Git** v2.55.0.3 diinstall via winget
- **Memory repo** di-clone dari GitHub
- **opencode config** dibuat di `C:\Users\Digitalisasi\.config\opencode\opencode.jsonc`
- **cloudflared** v2026.7.3 diinstall via winget
- **Cloudflare Tunnel (Quick)** berjalan: `trycloudflare.com`, ekspose localhost:5774
- **Startup script:** `start-tunnel.bat` di Desktop
- **Cloudflare service** terinstall dengan token (tapi belum ada domain)

### 30 Juli 2026 — Digitalisasi-PC (Session 2)
- **2 aplikasi di-tunnel**: Dapodik (5774) + E-Rapor (8535)
- **E-Rapor error HTTP 500** — Fix: `dirname()` backslash issue di Constants.php
- **E-Rapor mode lite** — Fix: HTTPS detection dari header Cloudflare (X-Forwarded-Proto, Cf-Visitor)
- **Domain udah dipake** — Dapodik jalan, E-Rapor masih perlu restart Apache
- **CATATAN-TUNNEL.txt** disimpan di Desktop & memory/COMMON/docs/ sebagai panduan

### 30 Juli 2026 — yonat-PC
- Absensi 30 Juli: PG (Hans I), TKB2 (Celine S), TKB1 (Melvin I, Brenden S)
- File: Absensi Juli 30 2026 Thursday 09_24_56.xlsx

### 11 Agustus 2026 — linux-tablet
- **Model utama opencode diganti** → `opencode/big-pickle` (via OpenRouter)
- File: `~/.config/opencode/opencode.jsonc` — model lama `opencode/ling-3.0-tiny-free` diganti
- Keputusan user: big pickle jadi model utama

### 12 Agustus 2026 — yonat-PC
- **Website SD Methodist-11** (`COMMON/project-sd-methodist-11/`): ikon sosmed pakai SVG brand resmi (FB/IG/YT/WA/Operator), warna brand + lingkaran 48px seragam
- **Catatan kaki versi** di footer semua 13 halaman: `Versi 0.0002` (style kecil `.footer-meta`)
- **Auto-bump versi OTOMATIS**: setiap commit yang menyentuh file website (index.html, pages/, assets/css/) → versi footer naik 1 tingkat (0.0002 → 0.0003, dst) via pre-commit hook
  - Script: `COMMON/project-sd-methodist-11/bump-version.ps1`
  - Hook: `.githooks/pre-commit` (ter-commit ke repo), `core.hooksPath=.githooks` di-set di PC ini
  - **PC lain WAJIB jalankan** `git config core.hooksPath .githooks` sekali setelah pull, biar hook ikut aktif
  - Jangan edit footer-meta versi manual — biar hook yang naikin
- **Cache-buster CSS otomatis**: hook juga menaikkan `style.css?v=N` setiap commit → HP/browser tidak perlu clear cache manual (perbaiki ikon sosmed biru di HP, commit `3aff9b7`, versi 0.0003)
- **Menu Kalender Pendidikan**: ditambahkan sebelum E-Rapor di semua 13 halaman → `pages/kalender.html` (embed PDF `assets/kalender/KALENDER-PENDIDIKAN-2026-2027.pdf` dari `D:\New folder\`, + tombol unduh), commit `0bfcd7c`
- **Navbar desktop 2 baris**: menu dibagi 2 baris via `.menu-row` (baris 1: Beranda/Kenapa Kami/Visi & Misi/Fasilitas/Pengumuman; baris 2: Kegiatan/Galeri/Lokasi/Kontak/Kalender Pendidikan/E-Rapor) biar tidak melebar; `scroll-margin-top` 90px; commit `bb192ea`
- **Footer**: `Versi 0.0004 — Transparansi 50%` (teks transparansi diminta user dipasang lagi)
- Commit terkait: `980a340` (catatan kaki), `b8ae2aa` (setup auto-bump), `3aff9b7` (cache-buster otomatis), `0bfcd7c` (menu kalender), `bb192ea` (navbar 2 baris)
- **DARK MODE (15 Agustus 2026):** toggle 🌙/☀️ di navbar semua 14 halaman (tombol `.theme-toggle` dalam `.nav-actions`). CSS: hardcoded `#fff` di-refactor → `var(--surface)`; blok `[data-theme="dark"]` + variabel dark ditambahkan di akhir `style.css`. Anti-flash inline script di `<head>` tiap halaman (baca localStorage `m11-theme`, fallback `prefers-color-scheme`). Pilihan persist di localStorage `m11-theme`. Tema dark: latar `#0b1220`, surface `#121a2f`, teks `#e5e7eb`, biru terang `#60a5fa`, hero tetap gradient biru tua (`--hero-a/b` dikunci). Belum di-commit saat ini — cache-buster `?v=16` akan naik otomatis oleh pre-commit hook setelah commit.

---

*Catatan: Semua konfigurasi di-sync via GitHub*
*Repo: https://github.com/yonathan-boop/OPENCODE*
