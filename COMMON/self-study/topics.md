# Self-Study Queue

Daftar topik yang dipelajari AI secara mandiri. Runner: `SERVER-LINUX/scripts/self-study.sh`
(dijadwalkan via cron, mingguan). Hasil riset disimpan ke `notes/` dan topik ditandai selesai.

Aturan:
- Baris topik = `- [ ] <topik>`. Selesai → ganti `[ ]` jadi `[x]`.
- Topik diambil urut dari atas (yang belum selesai).
- Tambah topik baru kapan saja — langsung diproses giliran berikutnya.

- [x] Dapodik & E-Rapor: jadwal sinkronisasi 2026, masalah umum (server down, NSM/NPSN, pdsp) dan solusinya (catatan: notes/dapodik-erapor-2026.md, 17/9)
- [s] Menghubungkan PC lokal (yonat-PC) dengan server Linux (ZeroTier/SSH/tunnel): cara aman, biar bisa saling akses web/terminal/transfer file [klaim 2026-09-17 14:33 SERVER]
- [ ] Kurikulum Deep Learning 2026: apa perubahannya dari Kurikulum Merdeka, istilah kunci, implikasi ke RPP & admin sekolah
- [p] Otomatisasi laporan sekolah dengan Excel/Python (openpyxl): pola aman, hemat memori, validasi sebelum lapor [klaim 2026-09-17 14:40 PC]
- [ ] Mail merge & narasi rapor di Word: batch dari Excel, masalah umum & solusinya
- [ ] Cloudflare Tunnel: zero-trust Access untuk halaman admin, beda cloudflared config vs quick tunnel
- [ ] Backup 3-2-1 untuk data sekolah: strategi murah, efektif, dan cara tes restore
- [ ] OCR untuk pekerjaan guru: dokumen scan → teks/Excel rapi (Tesseract & alternatif gratis)
- [ ] Gemini API: kuota, harga, rate limit, best practice untuk GENERATOR-RPP
- [ ] Google Workspace for Education: fitur admin yang berguna untuk sekolah kecil
- [ ] Keamanan server Linux kecil (single VPS): hardening dasar, update, monitoring
