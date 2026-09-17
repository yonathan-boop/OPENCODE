# Dapodik & E-Rapor 2026 — Jadwal, Masalah Umum, dan Solusi

## Ringkasan
Sinkronisasi Dapodik digelar 2x per tahun ajaran (semester ganjil & genap), tiap kali rilis versi aplikasi baru (installer/patch). Bagi SD, pengenalnya adalah **NPSN 8 digit** (bukan NSM — NSM khusus madrasah di bawah Kemenag). Sinkron wajib lewat akun kepala sekolah setelah validasi pasar (data ikon merah = blokir sinkron). Sistem paling rawan "server busy" menjelang cut-off. Aplikasi 2026.c dipakai semester genap 2025/2026; sejak 18 Juli 2026 rilis **Dapodik 2027** (patch 2027.a 13/8, 2027.b 28/8) untuk semester ganjil 2026/2027.

## Poin praktis untuk admin sekolah
- **Identitas sekolah:** NPSN 8 digit, unik, 1 sekolah 1 NPSN. Jangan diubah lewat Dapodik — perubahan nama/NPSN/alokasi hanya via **Verval SP** (disetujui dinas). Cek di `dapo.kemendikdasmen.go.id` → Pencarian, atau `referensi.data.kemendikdasmen.go.id`.
- **Jadwal sinkron ideal:** tiap rilis versi → 1) unduh installer/patch dari `dapo.kemendikdasmen.go.id/unduhan`, 2) registrasi (boleh luring pakai **prefill terbaru**), 3) Tarik Data, 4) input/validasi, 5) sinkronisasi pakai akun kepala sekolah. Hindari 2-3 hari terakhir sebelum cut-off.
- **Cek versi:** beranda aplikasi menampilkan nomor versi; habis update tekan **Ctrl+F5**. Untuk cek pembaruan: Pengaturan → Cek Pembaruan.
- **Backup sebelum sinkron:** cadangkan folder data lokal aplikasi (dan database) sebelum instal installer/patch baru — metode installer dapat **menghilangkan data yang belum di-sinkron**. Sinkron dulu di versi lama sebelum upgrade.
- **Cut-off yang tercatat 2025-2026:** 31/8/2025 (Dapodik 2026); genap 2025/2026 dipercepat **7/3/2026** (TPG triwulan I); cut-off PIP edaran awal Jan 2026. Selalu cek berita di laman resmi karena bisa berubah mendadak.
- **E-Rapor SD (2025.1):** sumber data dari Dapodik → login sekolah → **Ambil Data Dapodik** → pilih semester → Proses → logout → Ctrl+F5. Ganti semester ganjil→genap cukup lewat menu ini, tidak perlu reinstal.

## Jebakan / error umum + solusi
- **Server busy / gagal log in mendekati cut-off:** traffic nasional (43rb+ sekolah, rata-rata ±60rb sinkron/hari, puncak 133rb). → Sinkron di luar jam kerja (malam) atau setelah cut-off rame pertama (pagi).
- **"Batas sinkron dipercepat" mendadak (mis. 7/3/2026, TPG):** → Pantau Info GTK & berita Dapodik tiap awal bulan; jangan tunggu deadline.
- **Residu Verval (TPG tidak cair):** NIK/NISN salah tulis, nama beda dgn KK, siswa dobel sekolah (>75% residu wajib dibersihkan). Solusi: perbaiki via **Verval PD/PTK** (validasi Dukcapil real-time, persetujuan ±2x24 jam), bukan sekadar edit lokal.
- **Instal gagal "setup file are corrupted":** file installer tidak utuh. → Cek ukuran file (installer Dapodik 2026 ≈ 93,7 MB; kalau 2-60-70 MB berarti rusak), unduh ulang dari situs resmi.
- **Data lokal hilang setelah upgrade versi:** belum sinkron di versi lama. → Selalu sinkron kunjungan selesai input, baru ganti versi.
- **Tombol sinkron mati/blokir:** ada data invalid (ikon merah). → Validasi dulu, perbaiki semua data merah, lalu akun kepala sekolah untuk sinkron.
- **E-Rapor localhost:2689 error "Database error: cannot prepare statement":** → Clear cache browser, tutup & buka ulang.
- **E-Rapor nilai akhir/deskripsi tidak muncul:** nilai KKM belum terisi / KKM mapel kosong (import KKM via Data Referensi Lokal), atau deskripsi belum ditekan **Simpan**; KD dicentang minimal 2.
- **E-Rapor "Whoops" tidak berjalan:** copy `icudt71.dll, icuin71.dll, icuio71.dll, icuuc71.dll` dari folder aplikasi ke `C:\Windows\System32`, restart laptop.

## Sumber
- https://dapo.kemendikdasmen.go.id/berita (rilis versi 2026.c / 2027 / cut-off PIP)
- https://dapo.kemendikdasmen.go.id/unduh-aplikasi & /unduhan (installer, patch, prefill)
- https://helpdesk.pauddasmen.id (Sinkronisasi, Data Sekolah/Verval SP)
- https://referensi.data.kemendikdasmen.go.id/residu/informasi (NPSN, NISN, NUPTK, residu)
- https://bbpmpjateng.kemendikdasmen.go.id/permasalahan-yang-sering-muncul-di-erapor-jenjang-sd
- https://s.id/erapor-sd-ditsd (e-Rapor SD 2025.1, cara ganti semester, error Whoops)
- https://infopendidikan.bic.id/batas-sinkronisasi-dapodik-2026 (cut-off 7/3/2026, Verval PTK)
- https://beritabogor24jam.com/teknologi/gagal-instal-dapodik-2026-jangan-panik-begini-solusi-tanpa-error (ukuran installer, registrasi offline)