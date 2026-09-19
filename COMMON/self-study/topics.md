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
- [x] OCR untuk pekerjaan guru: dokumen scan → teks/Excel rapi (Tesseract & alternatif gratis) (selesai 2026-09-17, catatan: ocr-untuk-pekerjaan-guru-dokumen-scan-teks-excel-rapi-tesseract-alternatif-gratis.md)
- [x] Gemini API: kuota, harga, rate limit, best practice untuk GENERATOR-RPP (selesai 2026-09-17, catatan: gemini-api-kuota-harga-rate-limit-best-practice-untuk-generator-rpp.md)
- [x] Google Workspace for Education: fitur admin yang berguna untuk sekolah kecil (selesai 2026-09-17, catatan: google-workspace-for-education-fitur-admin-yang-berguna-untuk-sekolah-kecil.md)
- [x] Keamanan server Linux kecil (single VPS): hardening dasar, update, monitoring (selesai 2026-09-17, catatan: keamanan-server-linux-kecil-single-vps-hardening-dasar-update-monitoring.md)

## Topik baru (ditambah 18/9)
- [x] Format soal Pilihan Ganda (a-d) & isian/essay di Word dari sumber campuran (.doc/.docx/.txt): indentasi-tab konsisten, gambar/equation di dalam soal, batas python-docx vs Word COM (terkait ujian_builder.py; selesai 2026-09-18, catatan: notes/format-soal-ujian-word-ujian-builder.md)
- [x] Dokumen ujian multi-halaman: kop berulang tiap halaman, section breaks, header/footer berbeda, keep-with-next agar soal+opsi tidak terpisah halaman (selesai 2026-09-18, PC; catatan: notes/kop-berulang-tiap-halaman-keep-with-next.md + LRN-20260918-009)
- [s] Batch proses puluhan mapel ujian per UTS: penamaan konsisten "... OK Edit P", tracking selesai/backlog dari @backup guru, cek list putus di tengah jalan [klaim 2026-09-20 01:55 SERVER]
