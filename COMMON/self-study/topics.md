# Self-Study Queue

Daftar topik yang dipelajari AI secara mandiri. Runner: `SERVER-LINUX/scripts/self-study.sh`
(dijadwalkan via cron, mingguan). Hasil riset disimpan ke `notes/` dan topik ditandai selesai.

Aturan:
- Baris topik = `- [ ] <topik>`. Selesai → ganti `[ ]` jadi `[x]`.
- Topik diambil urut dari atas (yang belum selesai).
- Tambah topik baru kapan saja — langsung diproses giliran berikutnya.

- [x] Dapodik & E-Rapor: jadwal sinkronisasi 2026, masalah umum (server down, NSM/NPSN, pdsp) dan solusinya (catatan: notes/dapodik-erapor-2026.md, 17/9)
- [x] Menghubungkan PC lokal (yonat-PC) dengan server Linux (ZeroTier/SSH/tunnel): cara aman, biar bisa saling akses web/terminal/transfer file (selesai 2026-09-17, catatan: menghubungkan-pc-lokal-yonat-pc-dengan-server-linux-zerotier-ssh-tunnel-cara-aman-biar-bisa-saling-akses-web-terminal-transfer-file.md)
- [x] Kurikulum Deep Learning 2026: apa perubahannya dari Kurikulum Merdeka, istilah kunci, implikasi ke RPP & admin sekolah (selesai 2026-09-17, catatan: kurikulum-deep-learning-2026-apa-perubahannya-dari-kurikulum-merdeka-istilah-kunci-implikasi-ke-rpp-admin-sekolah.md)
- [x] Otomatisasi laporan sekolah dengan Excel/Python (openpyxl): pola aman, hemat memori, validasi sebelum lapor (catatan: notes/excel-automation-openpyxl.md, 17/9 PC)
- [x] Mail merge & narasi rapor di Word: batch dari Excel, masalah umum & solusinya (selesai 2026-09-17, catatan: mail-merge-narasi-rapor-di-word-batch-dari-excel-masalah-umum-solusinya.md)
- [x] Cloudflare Tunnel: zero-trust Access untuk halaman admin, beda cloudflared config vs quick tunnel (selesai 2026-09-17, catatan: cloudflare-tunnel-zero-trust-access-untuk-halaman-admin-beda-cloudflared-config-vs-quick-tunnel.md)
- [x] Backup 3-2-1 untuk data sekolah: strategi murah, efektif, dan cara tes restore (selesai 2026-09-17, catatan: backup-3-2-1-untuk-data-sekolah-strategi-murah-efektif-dan-cara-tes-restore.md)
- [s] OCR untuk pekerjaan guru: dokumen scan → teks/Excel rapi (Tesseract & alternatif gratis) [klaim 2026-09-17 16:07 SERVER]
- [ ] Gemini API: kuota, harga, rate limit, best practice untuk GENERATOR-RPP
- [ ] Google Workspace for Education: fitur admin yang berguna untuk sekolah kecil
- [ ] Keamanan server Linux kecil (single VPS): hardening dasar, update, monitoring
