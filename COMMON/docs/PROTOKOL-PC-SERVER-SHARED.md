# PROTOKOL Komunikasi PC-Server (tmux shared + handoff)

Disepakati 18/9/2026 (PC yonat <-> Server Linux via sesi tmux `shared`).

## Cara akses sesi shared
- Dari PC: `ssh -p 2222 root@192.168.195.60` lalu `tmux attach -t shared`
- Kirim pesan ke server dari PC (non-interaktif): via ssh + tmux send-keys
- Baca balasan server: `tmux capture-pane -t shared -p -S -60` (pakai scrollback supaya tidak terpotong; JANGAN pakai -e/escape)

## Aturan komunikasi
1. **Prefiks wajib**: PC → `[ADMIN] <instruksi>`. Server → `[DONE] <ringkasan 1 baris hasil>`
   untuk sukses, `[FAIL] <alasan>` untuk gagal.
2. Server hanya menanggapi pesan berprefiks dari PC. Output/sendirinya server sendiri
   (tanpa prefiks, yang muncul setelah tag Thought/Writing) = BUKAN input, diabaikan.
3. **Satu tugas dulu selesai** sebelum lanjut tugas berikutnya (anti tabrakan).
4. **Hasil/output panjang** (rangkuman, log, daftar) ditulis server ke file handoff,
   bukan ke terminal: `/root/memory/COMMON/handoff.md` — format APPEND + timestamp
   (bukan rewrite), biar riwayat terbaca. PC baca via SSH `cat`.
5. Instruksi singkat (yang bisa selesai 1-3 baris) cukup lewat tmux shared langsung.

## Alur kerja contoh (update website)
1. Admin bilang ke PC: "update website"
2. PC kerjakan di sisi PC, commit + push
3. PC kirim `[ADMIN] server, git pull` via shared
4. Server pull, website ke-update
5. Server balas `[DONE] pulled OK`
6. PC kabari admin selesai

## Catatan
- SSH key PC (`admin@Methodist-11`, ed25519) sudah terpasang di authorized_keys server
  (port 2222, pubkey only). ZeroTier net `633e31d8a2212ce2`, server 192.168.195.60.
- Jangan kirim pesan berulang/auto-loop; tunggu balasan sebelum meneruskan.