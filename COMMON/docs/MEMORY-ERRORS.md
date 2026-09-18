# Memory Errors

Catatan error penting, tool failure, atau kegagalan workflow agar tidak terulang. Versi PADAT (15/9): detail panjang dipadatkan, solusi & pelajaran tetap.

---

## [ERR-20260918-003] check_visual.py Crash cp1252 di Emoji Gemini — medium, fixed
Saat Gemini balas pakai emoji (mis. ✅/💡 dalam saran perbaikan), `check_visual.py` (Windows) crash `UnicodeEncodeError: 'charmap' ... u2705` ketika `print(ans)`. Render & validasi sebenarnya sukses — hanya print balasan yang gagal. **Fix:** `sys.stdout/stderr.reconfigure(encoding="utf-8", errors="replace")` di awal `main()` (pola sama ERR-20260917-002). Pel: SEMUA script PC yang memanggil Gemini/LM harus encoding-safe terhadap emoji. #encoding #windows #gemini #check_visual

## [ERR-20260917-002] Self-Study Claim Script Crash di Windows (cp1252) — medium, fixed
`python3 COMMON/scripts/self-study-claim.py --status` dari PC Windows crash `UnicodeEncodeError: 'charmap' codec can't encode '\u2192'` di baris print (topics.md berisi `→`; console default cp1252 menolak encode). **Fix:** tambahkan `sys.stdout.reconfigure(errors="replace")` di awal `main()` (try/except AttributeError untuk Python lama); script jadi lintas-OS. Pel: script shared lintas mesin (server Linux + PC Windows) harus encoding-safe — jangan print karakter non-ASCII tanpa guard. #self-study #windows #encoding #cross-platform

## [ERR-20260428-001] Kill VNC Server Saat Remote Session — high
Pakai `pkill -9 Xvnc` saat VNC sedang dipakai remote = membunuh sesi sendiri. JANGAN kill proses Xvnc/XFCE yang aktif; start di display lain atau tanya user. VNC user restore sendiri; symlink /root/Desktop→~/Desktop + desktop files sudah dibuat. #vnc

## [ERR-20260819-001] Absensi_Langsung_Edit_Buat_Sistem_Versi — high, fixed
AI mengedit file absensi lama (Absensi 15 Agustus...) in-place utk data 18-19 — melanggar sistem versi. DI-restore via `git restore`, file baru `Absensi 19 Agustus 2026 Tuesday 08_00_00.xlsx` dibuat (validasi 17+11 mark ✅).
**ATURAN WAJIB:** copy versi terbaru → file BARU → update FILE_PATH → isi → validasi. #absensi #versi

## [ERR-20260822-001] Sub-Agent Return Kosong Beruntun — medium, workaround
Task tool balik hasil kosong 3x ("completed" tapi kerjaan separuh). Jangan percaya laporan — cek bukti fisik (`git log`, `git status`, LastWriteTime, isi folder temp). Kalau gagal senyap berulang → otak eksekusi manual langsung + validasi sendiri. #sub-agent #task-tool

## [ERR-20260824-001] Web Terminal Error - Path Script Pindah Repo — medium, fixed
ttyd port 7681 exit 127 = memanggil path LAMA `linux-server/scripts/pilih-terminal.sh` yang sudah pindah ke `/root/SERVER-LINUX/scripts/`. Solusi: restart ttyd pakai path baru; update start-website.sh (4 layanan); validasi lokal 200, publik 200, auth 401. **Pel: pindah file antar folder WAJIB cek semua service pemanggil.** URL tunnel terminal berubah tiap restart (cek /var/log/cloudflared-terminal.log). #terminal #ttyd #server-linux

## [ERR-20260902-001] Word Lelet Akibat Ghost WINWORD COM — medium, fixed
Word lelet setelah sesi edit via COM: instance WINWORD "ghost" (MainWindowTitle kosong, handle 0) numpuk ~160MB/instans. Deteksi: `Get-Process winword | Select Id,MainWindowTitle,MainWindowHandle` (judul kosong = ghost, aman dibunuh; dokumen user selalu ber-judul → JANGAN sentuh). **Solusi:** script COM WAJIB `$word.Quit()` + `[Marshal]::ReleaseComObject()` (try/finally); bersihkan ghost handle 0 setelah sesi; verifikasi "CLEAN - no WINWORD". Windows key Office Resiliency DisabledItems = harmless, jangan dihapus. #word #com #ghost

## [ERR-20260905-001] Word Lelet di Menu Page Setup/Kolom/Print — medium, fixed (nunggu konfirmasi)
Word kadang macet sampai 10 detik di dialog Page Setup/columns/print di yonat-PC. Bukan ghost COM (sudah beres), RAM aman, jaringan 0ms. Penyebab potensial: 2 printer network Point-and-Print dari \\192.168.136.1 (query spooler remote tiap buka dialog Print) + autosave & lock sesaat oleh OneDrive+Defender. **Solusi diterapkan:** `DisableHardwareAcceleration=1` (HKCU\Software\Microsoft\Office\16.0\Word\Options) — perlu restart Word. Cadangan: exclude Defender folder kerja, keluar dari OneDrive. #word #lelet #printer #onedrive

## [ERR-20260908-001] Bot Telegram Gagal Jawab: Disk Penuh + Latensi Gateway — high, fixed (2 fase)
**Fase 1 — Disk penuh:** bot berhenti balas karena `/` (overlay fly-upper-layer) 100%. Penyebab: cache V8 opencode di /tmp `.XXXX-00000000.so` (~13.7MB/warna) menumpuk sejak 22/8 → 794 file ~4.3GB + chrome.deb 141MB + npm cache 1.3GB. `du -x /` menipu (78M) — ukuran asli di `du -x -d1 /.fly-upper-layer`. **Solusi:** hapus cache /tmp, npm cache clean; cron `55 23 * * *` bersihkan `/tmp /var/tmp *00000000*`; restart bot via start-bot.sh. Hardening bot: `proc.on('error')` + flag done, dedupe update_id global Set(1000), offset disimpan sebelum eksekusi, polling TIDAK await eksekusi (execQueue serial). **Pel: kalau bot error → cek disk dulu.** 
**Fase 2 — Latensi gateway:** setelah disk beres bot tetap diam: first-token gateway free-anonymous melonjak ~2s→130s (throttle koneksi baru; sesi interactive tetap lolos). `opencode run` hang = 0 byte output walau DEBUG — tapi AKHIRNYA exit 0 (bukan mati, LAMBAT). **Solusi:** TIMEOUT_MS 180s→600s; reset sesi bot (workspace kosong = konteks kecil → first-token cepat); start-bot redirect stdout benar (nohup node bot.js 2>>LOG >/dev/null). Balasan ±130s per pesan normal saat gateway lemot. Ukur latensi: `time timeout 200 opencode run --dir /tmp/x --auto "tes"`. #telegram-bot #disk-full #opencode #server-linux #bot