# Memory Learnings

Catatan koreksi, insight, dan pola yang terbukti membantu agar asisten berkembang lintas sesi. Versi PADAT (15/9): detail historis dipadatkan, aksi & referensi tetap.

---

## [LRN-20260916-001] pack_otak_bersih — priority: high
Untuk komputer orang lain (kepala sekolah): buat REPO private terpisah (`OPENCODE-SEKOLAH`) berisi versi bersih memory — aman dibawa ke mesin lain. Sanitasi: buang konfigurasi PC pribadi, username, kredensial (ttyd password, API key → kosongkan placeholder), daftar perangkat; absensi ditarik karena itu kerjaan user sendiri; profiling user komputer tujuan pakai USER.md template; istilah internal (contoh label dari sesi ini) dihapus dari pack — pakai istilah netral "user". Aturan yang wajib dimasukkan ke AGENTS pack: **auto-commit tiap ±3 chat** diam-diam (penerima gak paham git) + setelah task tanya "sudah pas?" lalu simpan kasus terselesaikan ke MEMORY-LEARNINGS (format MASALAH/SOLUSI/Kapan dipakai lagi) + di awal sesi baca sesi percakapan opencode sebelumnya sebagai acuan preferensi. Catatan setup (token+link+langkah) ditaruh di TXT lokal Desktop — JANGAN pernah commit file bertoken (Push Protection). #pack #privasi #auto-commit

## [LRN-20260915-001] konsolidasi_memori_hemat_context — priority: high
Ketika file ini (dan MASTER) membesar, konsolidasi berkala wajib: dedup + ringkas detail historis → sub-file/arsip; MASTER tetap jadi indeks tipis. **PENJAGAAN:** bagian yang menyentuh data Excel/absensi (mapping kolom, sistem versi, daftar murid, kasus khusus) WAJIB full-fidelity/disalin persis — jangan diparafrase (skor test 2 sub-agen baru dianggap lolos kalau 100% match buat bagian data). Verifikasi `diff == 0` sebelum commit. Hasil 15/9: context startup 45K→38K. #memory #context #optimasi #absensi

## [LRN-20260911-002] jangan_sebut_agama — priority: critical
LARANGAN KERAS user: JANGAN PERNAH menyebut/menulis/ganti ucapan agama (misal "Alhamdulillah", "syukur") di komunikasi mana pun. 100% netral. Sudah 2x ditegur keras. Cek ulang tiap pesan sebelum kirim. #komunikasi #agama #netral

## [LRN-20260911-001] word_copy_equation_hang_solusi — priority: high
Word yonat-PC hang/lelet tiap copy equation. Akar gabungan: (1) Clipboard History Windows (`HKCU\Software\Microsoft\Clipboard\EnableClipboardHistory=0`), (2) Panel Clipboard Office — begitu kebuka sekali, tracking nyala permanen → satu-satunya bersih = restart Word, lalu matikan 3 centang Options Clipboard; (3) `DisableHardwareAcceleration=1` bikin rendering equation CPU-only → hapus key. Pendukung `ShowPasteOptions=0`. #word #clipboard #equation #lelet

## [LRN-20260509-003] jangan_jalankan_ollama — priority: high
Jangan pernah jalankan Ollama (boros resource). Untuk vision pakai Tesseract OCR / API gratis. Kalau butuh vision model, tanya dulu sebelum install. #ollama #larangan

## [LRN-20260422-001] inference_from_short_prompts
Pahami instruksi singkat/implisit; gunakan konteks + memory. Bila ada contoh hasil → jadikan acuan kualitas/struktur, bukan salin mentah. #short-prompts

## [LRN-20260428-002] Launch GUI Apps di XFCE VNC — priority: high
Untuk launch GUI di VNC display :1 (linux-tablet): export DISPLAY=:1 dan XAUTHORITY=/data/data/com.termux/files/home/.Xauthority sebelum command. #vnc #xfce

## [LRN-20260422-002] save_and_read_memory_diligently
Pola `load -> kerja -> catat -> save`. Memory = konteks kerja utama, bukan arsip pasif. Pola berulang → promosikan ke MASTER. #memory

## [LRN-20260509-004] wajib_pakai_sub_agent_untuk_eksekusi — priority: high
Semua task eksekusi WAJIB sub-agent (task tool): bikin/edit file, run command, commit/push, scraping, batch edit. Otak (main session) hanya: baca memori, catat memori, planning, strategi, komunikasi. Sub-agent dikasih instruksi spesifik, tak perlu konteks penuh. #sub-agent #protocol

## [LRN-20260509-005] sub_agent_path_specification — priority: high
Waktu spawn sub-agent (git/commit/push) WAJIB set `workdir` path exact — jangan biarkan menebak (pernah stage ribuan file sampah dari root). Jangan `git add -A` sebelum ls. #sub-agent #path #git

## [LRN-20260908-002] bot_timeout_vs_latensi_model — priority: high
Bot tampak "tidak menjawab" ≠ rusak: bisa jadi latensi first-token gateway ~130s (pemakaian pagi intens). Jangan bunuh/restart tanpa ukur dulu: `time timeout 200 opencode run --dir /tmp/x --auto "tes"`. Timeout ≥3x first-token normal (TIMEOUT_MS=600000). Konteks kecil = first-token cepat → reset sesi kalau membengkak. #telegram #latency #timeout

## [LRN-20260512-001] wajib_pakai_todowrite_di_setiap_sesi
TodoWrite tiap sesi (3 bagian GAGAL/BERHENTI · LAGI DIKERJAIN · BERHASIL), update real-time. BACKLOG.md saja tidak cukup. #todo

## [LRN-20260730-001] simpan_masalah_dengan_tags — priority: high
Setiap masalah+solusi dicatat ke file .txt relevan di COMMON/docs/ dengan format `#tag` di baris atas biar bisa di-grep (#eraport #tunnel #cloudflare dst). Template: MASALAH/Gejala/Penyebab/Lokasi/SOLUSI. #tags #dokumentasi

## [LRN-20260725-001] wajib_validasi_sebelum_lapor — priority: high
WAJIB `execute → verify → report`: baca ulang hasil (Excel: cek sel & tanggal terisi, nama & kelas benar) sebelum lapor selesai. Berlaku semua task beroutput file. #validasi

## [LRN-20260819-002] absensi_sistem_versi_wajib — priority: CRITICAL
SETIAP update absensi: copy versi terbaru → file BARU → update FILE_PATH → isi → validasi. DILARANG edit file lama langsung (in-place) — liat MASTER bagian SISTEM VERSI. #absensi #versi

## [LRN-20260824-001] backup_harian_tanpa_duplikasi — priority: high
Backup harian = robocopy /E /XO ke 1 folder tetap (tanpa purge; file terhapus di source DIPERTAHANKAN). Full copy hanya backup semester (manual, flag -Semester). Sebelum bikin sistem duplikasi tanya soal kebutuhan memori. #backup #robocopy

## [LRN-20260905-001] bot_harus_pesan_biasa_bukan_log — priority: high
Ke Telegram kirim jawaban ringkas, bukan dump log. Pecah jawaban ≥3800 byte via splitMessages (jangan potong tengah kalimat). Setelah edit bot.js: `node --check`, restart via start-bot.sh/stop-bot.sh (pidfile). #telegram #bot

## [LRN-20260908-001] hapus_printer_jaringan_epson — priority: high
Hapus total printer jaringan EPSON L3210 (\\192.168.136.1, shared USB006; bisa auto re-add dari server → hapus ulang kalau muncul). JANGAN stop spooler utk hapus driver. Urutan: Remove-Printer → cek port → Remove-PrinterDriver → kalau "in use": cek registry (HKLM\...\Print) & file drv → kalau bersih tinggal cache → `Restart-Service Spooler -Force` (elevated). Butuh admin → script .ps1 + `Start-Process powershell -Verb RunAs -Wait`. Brother JANGAN disentuh. #printer #epson #spooler