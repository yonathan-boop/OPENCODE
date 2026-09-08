# Memory Errors

Catatan error penting, tool failure, atau kegagalan workflow yang perlu diingat agar tidak terulang.

---

## [ERR-20260428-001] Kill VNC Server Saat Remote Session

**Tanggal**: 2026-04-28
**Device**: linux-tablet (Termux)
**Severity**: high

### Summary
Saat mencoba restart VNC untuk refresh desktop, saya menggunakan `pkill -9 Xvnc` yang membunuh proses VNC yang sedang digunakan untuk koneksi remote session ini sendiri.

### Action
- **JANGAN pernah** kill proses Xvnc/XFCE yang sedang digunakan untuk remote
- Untuk restart, gunakan cara yang lebih aman atau tanya user dulu
- Lebih baik start ulang VNC di display lain daripada kill yang aktif

### Catatan
- User sudah restore sendiri
- Symlink /root/Desktop -> /data/data/com.termux/files/home/Desktop sudah dibuat
- Desktop files sudah ada: Files.desktop, Firefox.desktop, Proot.desktop, Terminal.desktop, New Folder

---

## [ERR-20260819-001] Absensi_Langsung_Edit_Buat_Sistem_Versi

**Tanggal**: 2026-08-19
**Severity**: high
**Status**: fixed

### Summary
AI langsung mengedit file Excel absensi yang sudah ada tanpa membuat versi baru terlebih dahulu. Melanggar aturan sistem versi yang sudah ditetapkan sejak 4 Agustus 2026.

### Gejala
- File `Absensi 15 Agustus 2026 Saturday 10_18_23.xlsx` langsung diedit untuk menambah data18-19 Agustus
- Tidak ada proses: copy versi terbaru → file baru → isi data
- Tidak ada update FILE_PATH di absensi.py

### Penyebab
- AI tidak mengikuti prosedur sistem versi yang sudah ada di MASTER-MEMORY.md
- AI menganggap "edit in-place" sebagai cara cepat, padahal melanggar aturan utama

### Lokasi
- File: `Absensi 15 Agustus 2026 Saturday 10_18_23.xlsx`
- Script: `COMMON/scripts/absensi.py`

### SOLUSI
1. File lama di-restore via `git restore` (belum di-commit, jadi bisa dikembalikan)
2. File baru dibuat: `Absensi 19 Agustus 2026 Tuesday 08_00_00.xlsx` (isi: data13-15 + 18-19)
3. FILE_PATH di absensi.py diupdate ke file baru
4. Validasi: 17 mark18-19 ✅, 11 mark13-15 ✅

### ATURAN WAJIB (PENGINGAT)
```
SETIAP KALI UPDATE ABSENSI:
1. Copy versi terbaru → file versi baru (nama: Absensi <tgl> <bulan> <tahun> <hari> <jam>_<menit>_<detik>.xlsx)
2. Update FILE_PATH di absensi.py ke file baru
3. Isi data di file BARU (bukan file lama)
4. Validasi sebelum lapor
```

---

## [ERR-20260822-001] Sub-Agent Return Kosong Beruntun

**Tanggal**: 2026-08-22
**Severity**: medium
**Status**: workaround ditemukan

### Summary
Task tool (sub-agent) balik hasil kosong 3x berturut-turut dengan state "completed": (1) simpan memory absensi 22 Agu, (2) retry simpan memory, (3) update roster absensi v22. Pekerjaan tidak jadi/tidak tuntas tanpa pesan error apapun.

### Gejala
- `<task_result>` kosong padahal prompt instruksi lengkap & detail
- Bukti fisik menunjukkan kerjaan cuma separuh jalan (cuma explore.py dibuat di temp, file target tidak tersentuh)

### SOLUSI
1. Jangan percaya laporan — cek bukti fisik: `git log`, `git status`, LastWriteTime file target, isi folder temp
2. Kalau gagal senyap berulang → otak eksekusi manual langsung (python/bash) + validasi sendiri
3. Laporan sub-agent yang sukses pun sempat korup karakter (teks Indonesia rusak) → indikasi masalah encoding pipeline output

---

---

## [ERR-20260824-001] Web Terminal Error - Path Script Pindah Repo

**Tanggal**: 2026-08-24
**Severity**: medium
**Status**: fixed

### Summary
Web terminal online (ttyd port 7681) langsung exit code 127 tiap buka sesi = command not found.

### Penyebab
- ttyd masih menjalankan `bash /root/memory/linux-server/scripts/pilih-terminal.sh` (path LAMA)
- Script sudah pindah ke repo terpisah `/root/SERVER-LINUX/scripts/pilih-terminal.sh`
- Path lama tidak ada lagi → sesi terminal mati seketika

### SOLUSI
1. Restart ttyd dengan path baru: `bash /root/SERVER-LINUX/scripts/pilih-terminal.sh`
2. Update `start-website.sh` → sekarang 4 layanan: web 8090, tunnel utama, ttyd 7681, tunnel terminal (quick)
3. Validasi: lokal 200, publik 200, auth 401 tanpa login ✅

### PELAJARAN
- **Kalau pindah file/script antar folder/repo, WAJIB cek & update semua service yang memanggil path itu**
- URL quick tunnel terminal BERUBAH tiap restart �?" cek `/var/log/cloudflared-terminal.log`
- start-website.sh sekarang print URL terminal terbaru di akhir run
#terminal #ttyd #server-linux #path-error #exit127

---

## [ERR-20260902-001] Word Lelet Akibat Ghost WINWORD COM

**Tanggal**: 2026-09-02
**Severity**: medium
**Status**: fixed

### Summary
Word terasa lambat/lelet setelah sesi edit soal ujian via Word COM automation (2 September 2026).

### Penyebab
- Script Word COM yang tidak memanggil `Quit()` atau hang saat dieksekusi meninggalkan instance WINWORD "ghost" tak-berjendela (`MainWindowTitle` kosong, `MainWindowHandle`=0) yang numpuk di memory (~160 MB per instance).
- Satu instance ghost ditemukan PID 2120 (StartTime 2:02 PM, 158.9 MB) dari sesi edit tadi malam.

### Diagnosis (penyelidikan)
- `Get-Process winword | Select Id, MainWindowTitle, MainWindowHandle` → instance dengan judul kosong + handle 0 = ghost COM, aman dibunuh. Dokumen asli user selalu punya judul (mis. "SURAT PERNYATAAN...") → JANGAN dibunuh.
- Registry `HKCU:\Software\Microsoft\Office\16.0\Word\Resiliency\DisabledItems` ada 4 entry (akibat Word crash saat COM) — harmless, bukan penyebab lelet, jangan dihapus.
- Folder cache web Word (`AppData\Roaming\Microsoft\Word\IPS%203%20...312756...`) total 22 MB — normal, bukan penyebab.
- `Normal.dotm` bersih (19 KB, bukan bloat). Tidak ada korupsi registry.

### SOLUSI
1. Pastikan script COM SELALU panggil `$word.Quit()` + `[Marshal]::ReleaseComObject()` di akhir (try/finally).
2. Setelah setiap sesi otak-atik Word, cek & bersihkan ghost: `Get-Process winword | ? MainWindowHandle -eq 0` → `Stop-Process -Force`.
3. Verifikasi: `Get-Process winword` → "CLEAN - no WINWORD running"; COM test `Version=16.0` jalan normal & clean exit.
4. Kembalikan agar tidak semrawut: kosongkan leftover AutoRecovery `.asd` doc yang tak dipakai (opsional, kecil).

### VERIFIKASI
- Ghost PID 2120 dibunuh → tidak ada WINWORD tersisa. COM test open+quit bersih tanpa ghost baru.

#word #com #ghost #lemot #winword #automation

---

## [ERR-20260905-001] Word Lelet di Menu Page Setup/Kolom/Print

**Tanggal**: 2026-09-05
**Severity**: medium
**Status**: fixed (menunggu konfirmasi user)

### Summary
Di yonat-PC, Microsoft Word kadang macet/lelet sampai 10 detik saat buka menu Page Setup, kolom, dan menu Print (kadang ~3x lipat dalam 10 detik). Bukan kata lain, hanya Word.

### Penyelidikan
- Tidak ada ghost WINWORD COM (hanya 1 instance dokumen user, RAM 300MB, normal) — kasus ERR-20260902-001 sudah beres.
- RAM aman (60% used), jaringan ke server 192.168.136.1 = 0ms, Defender real-time normal, Spooler running.
- 2 printer jaringan Point-and-Print dari \\192.168.136.1 (EPSON L3210 + Brother HL-L2360D, keduanya dipakai user) → setiap buka dialog Print Windows query ke spooler remote.
- File kerja di folder Desktop OneDrive → autosave bisa kena lock sesaat oleh OneDrive+Defender sync.
- Tidak ada add-in Office pihak ketiga.
- 25 proses msedgewebview2 (boros tapi umum).

### SOLUSI yang diterapkan
1. Disable Hardware Graphics Acceleration = 1 (registry `HKCU\Software\Microsoft\Office\16.0\Word\Options\DisableHardwareAcceleration`) → mematikan GPU acceleration di Word, langkah paling umum utk fix lag rendering Page Setup/columns/print. Perlu restart Word biar aktif.
2. Printer dua-duanya tetap, default tetap Brother (keputusan user).

### Cadangan kalau masih lelet (belum dieksekusi)
- Exclude Defender utk folder kerja + temp Office.
- Pindahkan folder kerja ke luar OneDrive.

#word #lelet #gpuacceleration #printer #onedrive #defender

---

## [ERR-20260908-001] Bot Telegram Gagal Jawab Akibat Disk Penuh 100%

**Tanggal**: 2026-09-08
**Device**: Server Linux (/root)
**Severity**: high
**Status**: fixed

### Summary
Bot Telegram `@Qksusb_bot` berhenti menjawab ("masih error tidak ada jawaban"). Penyebab utamanya bukan logika bot, tapi **disk `/` (overlay fly-upper-layer) penuh 100%** → opencode keluar `exit=1 err=92` tiap dipanggil, lalu proses bot mati (monitor: "Telegram bot masih down").

### Akar penyebab (ini bikin disk 100%)
- Setiap eksekusi `opencode` bikin **file cache V8 di /tmp** (pola `.9adb...-00000000.so` ~13.7MB & `.node`), namanya beda tiap run → tidak pernah tertimpa, menumpuk tanpa batas.
- Ditemukan **794 file × ~4.3GB** di `/tmp` sejak 22 Agustus + `chrome.deb` 141MB + npm cache 1.3GB di `/root/.npm/_cacache`.
- `du -x /` dari root menipu (hanya 78M): upper layer overlay (`/.fly-upper-layer`, mount /dev/vdb) tidak terlihat — pakai `du -x -d1 /.fly-upper-layer` atau `find` untuk ukuran sebenarnya.

### SOLUSI
1. `find /.fly-upper-layer/tmp -maxdepth 1 -type f -name '*00000000*' -delete` → bebaskan 4.3GB.
2. `rm /tmp/chrome.deb` (141MB) + `npm cache clean --force` (1.3GB).
3. Disk: 100% → 85% (1.2GB avail). Cron pembersih: `55 23 * * * find /tmp /var/tmp -maxdepth 1 -type f -name '*00000000*' -mtime +1 -delete`.
4. Restart bot via `bash start-bot.sh` (pakai pidfile, jangan `pkill -f "node bot.js"`).
5. Hardening `bot.js` (2 lapis keamanan): (a) `proc.on('error')` di `runOpencode` + flag `done` biar timeout SIGKILL dan event close tidak dobel-settle; (b) dedupe `update_id` pakai **global `processedUpdates` Set** (bounded 1000) + **offset disimpan SEBELUM eksekusi**, dan polling **TIDAK boleh `await` eksekusi opencode** — eksekusi dilempar ke `execQueue` (rantai promise serial, satu opencode pada satu waktu). Ini mencegah loop spam: kalau opencode hang 180s dan di-kill paksa, loop polling tetap maju & Telegram tidak mengirim ulang pesan lama.
6. Flush backlog (kalau antrean nyangkut): matikan bot lalu `curl -s "https://api.telegram.org/bot<TOKEN>/getUpdates?offset=-1"` → set `poll-offset.txt` ke update_id terakhir+1. Verifikasi antrean bersih: `getUpdates?offset=<tersimpan>` harus `pending: 0` (sudah dicek saat perbaikan: bersih).

### VERIFIKASI
- Tiap pesan user → `exit=0` + balasan normal.
- Log tiap pesan tercatat 1x (duplikat di terminal = artifact buffering tail, cek via `grep MESSAGE | sort -u`).

### PELAJARAN
- Kalau bot "error tanpa balasan", CEK DISK DULU (`df -h /`), bukan langsung nuduh logika bot.
- Cache `/tmp` hasil eksekusi opencode harus dibersihkan berkala (sudah ada cron).

---

### FASE 2 (08-09-2026 ~05:00–12:00 WIB) — disk beres tapi bot TETAP tidak menjawab

**Gejala:** setelah disk dibersihkan & bot di-restart, bot tetap tidak pernah mengirim balasan. Penyebab BUKAN logika bot, tapi **latensi gateway free-anonymous opencode (Zen) melonjak**: first-token dari ~2 detik (04:33) menjadi **~130+ detik** (05:30+), kadang flaky (ujian XDG berbeda sempat exit 0 lalu hang lagi). `opencode run` yang digantung menghasilkan **0 byte output walau `--log-level DEBUG --print-logs`**; log hanya sampai `message=stream providerID=opencode modelID=big-pickle` (request ke model) tanpa data balik. Sesi interactive (koneksi ESTAB via IPv6 Cloudflare) tetap berfungsi.

**Akar:** throttle/antrean di sisi gateway untuk koneksi baru (pemakaian pagi: banyak run konteks 85K token + sesi saya). Bukan error quota keras; respon AKHIRNYA datang (bg run 131s → exit=0 + jawaban benar) → bukan hang mati, tapi LAMBAT.

**SOLUSI bot:**
1. `TIMEOUT_MS` default 180000 → **600000** (env `TIMEOUT_MS` tetap bisa override) — 180s selalu kepotong sebelum balasan lahir.
2. **Reset sesi bot**: move dir `workspace/5508090479/default` → `_archive-<ts>`, buat `default` kosong — konteks kecil = first-token lebih cepat (via `newSession`/BOT_TEST, tanpa restart).
3. `start-bot.sh`: `nohup node bot.js 2>>"$LOG" >/dev/null </dev/null` — hapus baris ganda di log (sebelumnya stdout juga diarahkan ke file yang sama dengan `log()` appendFileSync). Sekarang log ditulis tunggal.

**Hasil:** balasan normal butuh ±130 detik per pesan (sesi kosong); antrean `execQueue` serial → tiap pesan ~2 menit berurutan. Pelajaran: kalau bot "pernah jalan cepat" lalu "selalu timeout", cek LATENSI MODEL bukan hanya kode (ukur `opencode run` manual + `time timeout 200 opencode run --dir /tmp/x --auto "tes"`). Saat latensi tinggi, besar timeout & kecilkan konteks, bukan bunuh proses.

#telegram-bot #disk-full #opencode #temp-cache #server-linux #bot
