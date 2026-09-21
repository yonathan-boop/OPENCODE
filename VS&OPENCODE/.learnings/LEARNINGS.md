# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## [LRN-20260921-001] gotty_menu_pilih_terminal_tmux

**Logged**: 2026-09-21
**Priority**: high
**Status**: active
**Area**: website-infra

### Summary
Terminal online methodist-11.my.id/opencode sekarang buka menu `pilih-terminal.sh` — user pilih mau berapa terminal (1/2/dst), dibuat via tmux windows, dan bisa tambah lagi belakangan (Ctrl-b lalu c).

### Details
- gotty service jalankan: `gotty -w -p 7681 -m /opencode <path>/pilih-terminal.sh` (bukan `bash -l` langsung).
- Script: `OPENCODE/linux-tablet/scripts/pilih-terminal.sh` (tmux 3.7c Termux OK — session unik per bukaan `web-<epoch>`, max 6 window, validasi input, `Ctrl-b` = prefix: `c`=tambah terminal, `<n>`=pindah, `w`=daftar, `exit`=tutup satu).
- Service runit lebih stabil untuk layanan yang harus selalu hidup: gotty/nginx/cloudflared. File `down` di service dir harus dihapus biar auto-start saat boot.
- **Jebakan:** `start-website.sh` lama spawn gotty lewat `setsid` → bentrok 2 instance dengan runit. Sekarang start script pakai `sv up`.

### Metadata
- Source: user_feedback
- Related Files: OPENCODE/linux-tablet/scripts/pilih-terminal.sh, /data/data/com.termux/files/usr/var/service/gotty/run
- Tags: gotty, tmux, terminal, methodist-11

## [LRN-20260921-002] gotty_resume_session_lama

**Logged**: 2026-09-21
**Priority**: high
**Status**: active
**Area**: website-infra

### Summary
Tab web terminal ditutup tidak sengaja → session tmux tetap hidup. `pilih-terminal.sh` diubah: buka lagi → daftar session lama muncul, tinggal pilih nomor buat LANJUT (bukan buka dari awal).

### Details
- Masalah lama: script selalu `tmux new-session -s web-$(date +%s)` → tiap buka halaman = session baru, riwayat hilang.
- Fix: di awal script cek `tmux ls | grep -E '^web-'`. Kalau ada session lama → tampilkan daftar + jumlah window, user ketik nomor untuk `tmux attach-session`. Ketik `b` untuk buat baru, `0` keluar.
- Max terminal baru dikurangi 6 → **2** (`TERM_TOTAL=2`).
- Lambat di tablet bukan karena tablet, tapi karena 2 instance opencode jalan bersamaan (CPU 80% + 23%). Opencode = proses berat (Bun runtime).
- Session yang masih hidup bisa numpuk → cek & kill dengan `tmux kill-session -t web-<epoch>`.

### Metadata
- Source: user_feedback
- Related Files: OPENCODE/linux-tablet/scripts/pilih-terminal.sh
- Tags: gotty, tmux, terminal, session, resume

## [LRN-20260921-003] termux_wakelock_runit

**Logged**: 2026-09-21
**Priority**: high
**Status**: active
**Area**: website-infra

### Summary
Termux harus tetap hidup di latar belakang (server gotty/nginx/cloudflared). Ditambahkan `termux-wake-lock` agar CPU tidak tidur saat app di-minimize.

### Details
- Service runit `wakelock` sudah ada tapi run-nya cuma `sleep 86400` (tidak memegang wakelock).
- Diubah run script jadi `termux-wake-lock; exec sleep 86400` — wake-lock di-aquire tiap service start.
- `termux-wake-lock` itu command one-shot (bukan daemon) → aman dipanggil berulang, Android pegang wakelock selama dipanggil.
- **Batasan Android:** swipe/close dari recent apps tetap matikan proses. Minimize (tombol Home) + wake-lock = jalan terus di background.
- Disarankan juga nonaktifkan battery optimization untuk Termux di pengaturan Android.

### Metadata
- Source: user_feedback
- Related Files: /data/data/com.termux/files/usr/var/service/wakelock/run
- Tags: termux, wakelock, runit, android, background

---
**Logged**: 2026-08-11
**Priority**: high
**Status**: active
**Area**: website-infra

### Summary
Website SD Methodist-11 live via Cloudflare NAMED tunnel (token), bukan quick tunnel. Domain methodist-11.my.id → localhost:8090.

### Details
- Install: `pkg install cloudflared` (Termux, v2026.7.3)
- Jalankan: `cloudflared tunnel run --token <TOKEN>` (tunnelID 912a22fa-...)
- Dashboard ingress: methodist-11.my.id → http://localhost:8090, config auto ke-push (cloudflared polling)
- Error 1033 = DNS record bukan CNAME tunnel / hostname tidak ter-ingress
- DNS cache lokal bisa nyimpen NXDOMAIN lama → bypass dengan `--resolve` atau tunggu
- Script trigger: `bash linux-tablet/scripts/start-website.sh` (kata kunci user: "hidupkan website")

### Action
- Simpan token + prosedur di `linux-tablet/docs/WEBSITE-METHODIST11.md`
- JANGAN pakai quick tunnel untuk domain ini

### Metadata
- Source: user_feedback
- Related Files: linux-tablet/docs/WEBSITE-METHODIST11.md, linux-tablet/scripts/start-website.sh
- Tags: cloudflare, tunnel, website, methodist-11

---

## [LRN-20260509-004] heartbeat_skip_saat_kosong

**Logged**: 2026-05-09
**Priority**: high
**Status**: active
**Area**: config

### Summary
HEARTBEAT.md yang kosong menyebabkan heartbeat API call skip. Isi dengan task checklist biar heartbeat aktif.

### Details
- File HEARTBEAT.md ada komentar: "Keep this file empty to skip heartbeat API calls"
- Awalnya kosong → heartbeat gak pernah dikirim
- User kira aku cuma reaktif padahal heartbeat cuma perlu diaktifkan

### Action
- HEARTBEAT.md harus selalu berisi task checklist
- Jangan dikosongin kalau mau heartbeat aktif
- Tetap perlu cek tanggal di setiap chat karena bisa beda hari

### Metadata
- Source: user_feedback
- Tags: heartbeat, config

---
**Logged**: 2026-05-09
**Priority**: high
**Status**: promoted
**Area**: config

### Summary
User ingin asisten yang paham instruksi singkat tanpa perlu dijelaskan panjang.

### Details
- Jangan tunggu prompt detail kalau arah umum sudah jelas
- Gunakan konteks memory untuk ambil keputusan
- Saat ada contoh hasil, jadikan acuan gaya dan kualitas

### Action
- Cek memory sebelum kerja besar
- Saat instruksi pendek, tafsirkan dengan percaya diri

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md, SOUL.md
- Tags: communication, workflow

---

## [LRN-20260509-002] save_and_read_memory_diligently

**Logged**: 2026-05-09
**Priority**: high
**Status**: promoted
**Area**: config

### Summary
Asisten harus rajin baca memory di awal sesi dan rajin simpan hal penting.

### Details
- User menegaskan AI tidak kuat langsung tangani hal besar tanpa memory disiplin
- Memory adalah konteks kerja utama, bukan arsip pasif

### Action
- Jalankan pola load -> kerja -> catat -> save
- Promosikan pola berulang ke MASTER-MEMORY.md

### Metadata
- Source: user_feedback
- Related Files: MEMORY.md, AGENTS.md
- Tags: workflow, memory

---

## [LRN-20260509-003] boundary_readonly_by_default

**Logged**: 2026-05-09
**Priority**: high
**Status**: active
**Area**: config

### Summary
User mengubah aturan: file di luar VS&OPENCODE/ bersifat read-only default, jika ingin diedit harus minta izin dulu.

### Details
- Awalnya: hanya boleh edit VS&OPENCODE/, jangan sentuh folder lain
- Sekarang: read-only default, kalau disuruh user → minta izin dulu baru kerja

### Action
- Sudah diupdate di SOUL.md dan AGENTS.md root + shared

### Metadata
- Source: user_feedback
- Related Files: SOUL.md, AGENTS.md
- Tags: boundary, config

---

## [LRN-20260812-001] selalu_fetch_sebelum_pull_website

**Logged**: 2026-08-12
**Priority**: high
**Status**: active
**Area**: website-infra

### Summary
Saat user minta "tarik/pull data website", WAJIB verifikasi source remote benar-benar terbaru — jangan percaya ref lokal `origin/main` yang bisa stale.

### Details
- Ref lokal `origin/main` bisa ketinggalan dari remote meskipun sudah pernah pull.
- Cara cek: `git fetch origin` dulu, lalu bandingkan `git rev-parse main origin/main` atau cek `git ls-remote origin` (HEAD/refs/heads/main).
- Kasus nyata: remote di `00de43e`, lokal masih `980a340` — 4 commit belum masuk karena aku pakai ref lama.
- Setelah `git fetch`, gunakan `git merge origin/main` (fast-forward) untuk ambil yang baru.

### Action
- Setiap "coba tarik lagi / ambil data terbaru" → jalankan `git fetch origin` + cek `git rev-parse main origin/main` SEBELUM pull/merge.
- Jangan skip fetch dan langsung pull yang mengandalkan ref lokal.

### Metadata
- Source: user_feedback
- Related Files: COMMON/project-sd-methodist-11/, WEBSITE-METHODIST11.md
- Tags: git, pull, fetch, website
