# Memory Summary (PC-06)

Terakhir diupdate: 23 September 2026 (versi PADAT — detail sesi historis di-ringkas; MASTER & ARSIP-ABSENSI pegang detail)

## User Info
- **Nama**: Digitalisasi (PC baru) / Advan (pc-rumah) / Admin (pc-06 kantor, lama) / yonat-PC (PC utama sekarang)
- **Bahasa**: Indonesia
- **OS**: Windows 10 (Digitalisasi-PC) / Windows (yonat-PC, install ulang)
- **Repo GitHub**: https://github.com/yonathan-boop/OPENCODE (memori di-sync di tiap PC)
- Suka instruksi singkat, hasil clean & modern. Kerja: absensi, dokumen ujian, coding.

## Project Aktif
1. **Memory System** — SOLESAI (29/7). Pola: baca sebelum kerja, simpan setelah kerja, sync via GitHub.
2. **Cloudflare Tunnel** — ekspose localhost ke internet via trycloudflare.com (quick tunnel).
3. **Website SD Methodist-11** — methodist-11.my.id (Cloudflare) via tunnel `8f8b0f53` → server Linux (/root/memory) → localhost:8090. LIVE sejak 22/8 (pindah dari PC Wilianto/tunnel 21b93a76 yang tidak dipakai lagi).

## Progress & Catatan Sesi Terpenting (ringkas)
- **11/4** setup memory system · **16/4** sinkron GitHub · **ca April–Mei** absensi bulanan (TKB2/TKB1/TKa/PG) + konsolidasi file master.
- **11/7** migrasi absensi ke TA 2026-2027 (folder `Absensi T.P 2026-2027`, master `ABSENSI Juli.xlsx`, roster dari DAFTAR MURID T.P.2026-2027 lengkap).
- **18/7** restore memory Windows.old + setup agent system · **25/7** sistem VALIDASI WAJIB (tanggal sering tak terisi).
- **Agu** sistem versi file absensi (wajib 1 file/hari, update FILE_PATH; ERR-20260819-001); game nama mapping; murid keluar/baru (Kimita 10/8; **21/8** murid baru Shane/Damian/Coryn/Erick; **22/8** roster disinkronkan, Kayla dihapus; website pindah ke server Linux; **24/8** redesign backup Methodist + mapping kolom Agustus).
- **Septa:** file September kosong (1/9); murid keluar Dareen & Axelle Sean (5/9); Generation (TKB1, 11/9) & Brilliant (TKB(2), 14/9) murid baru; tool rekap `rekap_absensi.py` (6/9); Telegram bot dihapus total → log-only (11/9); absensi 21/9 (9 mark), 22/9 (7 mark), & 23/9 (5 mark: Clarissa Jovanka TKB2, Giovan/Shon TKa, Kayyvant/Lucas TKB1); Antigravity: config `autoExecutionPolicy` diset ke `CASCADE_COMMANDS_AUTO_EXECUTION_AUTO` (Always Allow); **KSP 26-27 SD (22/9):** setup template BPMP Dokumen 1 di `C:\RaporServer\KOSP KURMER\Edit pc\`, selesai isi Cover, Identitas, Rekomendasi, Pengesahan, Kata Pengantar, Daftar Isi presisi, dan BAB I PENDAHULUAN lengkap (Profil, SWOT Johor, Tabel Murid 369 siswa, Tabel 19 PTK, Kemitraan, 19 Landasan Hukum 2025/2026). **23/9:** aplikasi **Phone Link (Microsoft.YourPhone)** dihapus di yonat-PC; **Perbandingan KSP 26-27 SD:** verifikasi 4 dokumen di `FIX\`, buat file salinan Track Changes resmi (Cover, Bagian Depan, Bab I-VI, & Dokumen Lengkap) persis visual screenshot user, dan tetapkan sistem Word/WPS COM `compare_docx.py` + audit placeholder sebagai standar permanen.

## Total Sessions: 14 (Apr–Sep 2026)
Detail kronologi sesi lengkap ada di git history repo ini. Sesi terakhir terekam di MASTER-MEMORY / ARSIP-ABSENSI-2026.

## Lingkungan yang digunakan
- PC-06 lama: Windows 10, C:\Users\Admin\.work, model lama minimax-m2.5-free, Tesseract 5.5.0 + image_tools_mcp.
- Digitalisasi-PC (= laptop SD Dapodik): Windows 10, opencode terinstall, cloudflared, tunnel Dapodik 5774 & E-Rapor 8535.
- PC-Advan: Windows, Git Portable, PyAutoGUI; Ollama DILARANG.
- yonat-PC (utama): lihat MASTER-MEMORY (model permanen big-pickle, 4 skill dokumen, Word COM tips).