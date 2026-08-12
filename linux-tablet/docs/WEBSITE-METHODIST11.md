# WEBSITE SD METHODIST-11 + CLOUDFLARE TUNNEL (linux-tablet)

Di-update: 12 Agustus 2026 (r4: judul hero rapi, gambar kartu bisa diklik)

## Status: AKTIF & LIVE

- **URL publik:** https://methodist-11.my.id
- **Web server lokal:** http://localhost:8090
- **Tunnel:** Cloudflare Tunnel named "Linux HP" (token-based, BUKAN quick tunnel acak)

## Komponen

| Komponen | Lokasi / Perintah |
|----------|-------------------|
| File website | `OPENCODE/COMMON/project-sd-methodist-11/index.html` + `assets/` |
| Web server | `python3 -m http.server 8090 --directory <WEB_DIR>` |
| Tunnel | `cloudflared tunnel run --token <TOKEN>` |
| Token tunnel | Di `linux-tablet/scripts/start-website.sh` (variable TOKEN) |
| Log tunnel | `linux-tablet/docs/tunnel.log` |
| Script satu-klik | `linux-tablet/scripts/start-website.sh` |

## Perintah Trigger User

- **"hidupkan website"** → jalankan: `bash OPENCODE/linux-tablet/scripts/start-website.sh`
- Script otomatis: matikan proses lama → nyalakan web server → nyalakan tunnel → tes lokal + tes domain.

## Setup yang SUDAH dilakukan (11 Agustus 2026)

1. `pkg install cloudflared` → v2026.7.3
2. Quick tunnel sempat dicoba (`trycloudflare.com`) → GANTI dengan named tunnel token.
3. Named tunnel connect: `cloudflared tunnel run --token <TOKEN>` → tunnelID `912a22fa-051a-4891-897a-f2ff20f2d5f2`.
4. Dashboard ingress: `methodist-11.my.id` → `http://localhost:8090` (config auto ke-push ke cloudflared, versi 4).
5. DNS `methodist-11.my.id`: A record proxied (104.21.87.167 / 172.67.144.176), NS Cloudflare (trevor/bristol).

## Catatan Penting

- **12 Agustus 2026 - R6 (semua gambar klik -> layar penuh / lightbox):** Semua gambar konten kini dibuka di lightbox: overlay layar penuh backdrop gelap, gambar besar, counter `n / total`, panah prev/next, tombol tutup x, tutup via klik luar / Escape, navigasi tombol panah kiri/kanan. Pakai ulang sistem lightbox yang sudah ada di halaman detail/galeri (`.lightbox` + JS inline `openLightbox`/`closeLightbox`/`lbNav`/`galeriItems`). Yang DISAMBUNGKAN ke lightbox: `index.html` (2 foto feature + 2 pengumuman + 4 kegiatan + 2 galeri), `pages/kegiatan.html` (6), `pages/galeri.html` (2), `pages/pengumuman/imunisasi.html` & `obat-cacing.html` (1 masing-masing). Gambar yang berada di dalam `<a>` (kartu index/galeri, list-item arsip) memakai `onclick="event.preventDefault();openLightbox(this.src)"` supaya klik gambar = buka lightbox, TIDAK pindah halaman; judul/tombol tetap navigasi ke detail. `galeriItems()`: index = `.kartu img, .feature img`; arsip kegiatan/galeri = `.list-item img`; detail pengumuman = `.artikel img`. CSS tambahan: `.kartu img, .feature img, .list-item img, .artikel img { cursor: zoom-in; }`. Semua link CSS diberi `?v=10` (index naik dari `?v=9`) agar cache browser refresh. Terverifikasi headless Chrome: klik gambar imunisasi -> lightbox terbuka tanpa navigasi, counter `3 / 10`, tombol next -> gambar berikutnya (`4 / 10`); kegiatan.html -> counter `1 / 6`.
- **12 Agustus 2026 — R5 (pop-up Pengumuman Terbaru):** di `index.html` tambah modal pop-up (`.popup-overlay` z-index 9999 + kartu `.popup`) berisi ringkasan pengumuman terbaru (Imunisasi, 12 Agustus 2026). Muncul otomatis saat index pertama kali dimuat via IIFE. Klik isi pop-up / tombol "Lihat Selengkapnya" → tutup + `scrollIntoView` smooth ke `#pengumuman` (plus `scroll-margin-top: 80px` biar gak ketutup header sticky). Tombol ✕ kanan-atas menutup tanpa navigasi. Pakai `sessionStorage` key `m11-popup-pengumuman` → hanya muncul SATU KALI per sesi tab. Escape juga menutup. CSS di-append di akhir style.css (baris 191+).
- **12 Agustus 2026 — R4 (user feedback):**
  - **Judul hero "lewat batas":** penyebab = `html { font-size: 20px }` menaikkan `.hero h1` (2.3rem→46px desktop, 1.7rem→34px HP) sehingga di HP teks panjang jadi kebesaran/penuh. Fix: `.hero h1` desktop → `1.85rem` (≈37px), HP → `1.35rem` (≈27px), plus `overflow-wrap: anywhere; text-wrap: balance;` supaya wrap rapi & kata panjang tak pernah overflow. Terverifikasi render: judul pas di container, tanpa horizontal scroll.
  - **Gambar kartu Pengumuman & Kegiatan kini bisa diklik** (sama seperti judul): `<img>` di dalam kartu index dibungkus `<a href="...">` menuju halaman detail — imunisasi, obat-cacing (pengumuman), 17-agustus, ibadah-rutin, harkdiknas, kunjungan-milo (kegiatan). CSS baru: `.kartu > a { display: block; }` + `.kartu > a:hover img { transform: scale(1.03); }`. Kartu galeri sudah full-clickable sebelumnya.
- **12 Agustus 2026 — Navbar E-Rapor:** Semua halaman dapat item navbar `📍 E-Rapor` (href `https://eraportsdmethodist11.my.id/`, target _blank) setelah link Kontak. Domain e-rapor beda zone dari methodist-11.my.id.
- **12 Agustus 2026 — Momen galeri "Kegiatan Kelas" DIHAPUS** (user: belum ada ide): `pages/galeri/kegiatan-kelas.html` + folder `assets/images/galeri/kegiatan-kelas/` (galeri-01..11) + kartu di index #galeri + item/nota di arsip galeri. Galeri momen sekarang tinggal 2: `17-agustus` & `outdoor`.
- **12 Agustus 2026 — R3 (layout HP + nama):**
  - Nama 2 baris di logo/hero/footer: `Yayasan Pendidikan Kristen Methodist Titus`<br>`TK-SD-SMP Swasta Methodist-11` (pake `<br>` sebelum TK; jangan taruh `<br>` di `<title>`/atribut/paragraf).
  - **Pengumuman ikut scroll ke samping** (`.kartu-grid` → `.scroll-row`), sama kayak Kegiatan & Galeri.
  - Font kartu kegiatan & pengumuman dikecilkan lagi (`.kartu .tgl` 13px, `h3` 18px, `p` 14px, `.btn-sm` 14px) karena kelihatan jelek di HP saat font global 20px.
  - Tombol "Lihat ... Lainnya" dibuat full-width di mobile (`.more-wrap .btn` di media query) biar nampak jelas di HP.
  - **Di HP: kartu Pengumuman & Kegiatan full-width (muat 1 per layar)** via `#kegiatan .scroll-row .kartu, #pengumuman .scroll-row .kartu { flex: 0 0 100%; scroll-snap-align: center; }` — tetap bisa geser ke samping; kartu galeri tetap 260px.
  - Foto obat cacing di-copy ulang (user ganti file) → `assets/images/pengumuman/obat-cacing.jpg` (954×739).
  - Semua foto asli di-resize ≤1280px, JPEG q82 (<300KB). Sumber foto: `C:\Users\yonat\OneDrive\Desktop\New folder`.
- **12 Agustus 2026 — R2 (user feedback):**
  - Nama sekolah di semua halaman → **Yayasan Pendidikan Kristen Methodist Titus TK-SD-SMP Swasta Methodist-11**.
  - Font diperbesar ~25% (`html { font-size: 20px; }`); logo navbar kecil biar muat nama panjang.
  - Foto ASLI di-copy & di-resize dari `C:\Users\yonat\OneDrive\Desktop\New folder` → `assets/images/pengumuman/{imunisasi,obat-cacing}.jpg` & `assets/images/kegiatan/{ibadah-1,harkdiknas-1..3,milo-1..4}.jpg`. Juara Kelas tetap TANPA gambar.
  - Kegiatan: `pentas-seni.html` DIHAPUS → ganti `harkdiknas.html` + baru `kunjungan-milo.html`. Index `#kegiatan` jadi 4 kartu (scroll horizontal).
  - **Fix lightbox:** di semua halaman galeri/kegiatan, `galeriItems()` pakai `return i.src;` (bukan `getAttribute('src')`) — dulu klik foto selalu tampil foto pertama.
  - Layout index: pengumuman = 3 kartu (imunisasi & obat-cacing ada foto, juara-kelas tidak) + tombol "Lihat Pengumuman Lainnya"; kegiatan & galeri = strip scroll ke samping + tombol "Lihat ... Lainnya" → halaman arsip `pages/{pengumuman,kegiatan,galeri}.html` (daftar lama, scroll ke bawah).
  - Foto kegiatan dari folder lama: "Kegiatan 17 Agustus 2024" KOSONG (foto 17-agustus.html masih pakai galeri existing); folder "Kegiatan Acara luar Ruangan TK" berisi HEIC/MP4 → belum dipakai.
- **12 Agustus 2026 — RESTRUKTURISASI:** Website jadi multi-halaman. `index.html` = ringkasan terbaru (3 kartu per section: Pengumuman, Kegiatan, Galeri momen). Detail pindah halaman di `pages/` (sub folder): `pages/pengumuman/{imunisasi,obat-cacing,juara-kelas}.html`, `pages/kegiatan/{17-agustus,ibadah-rutin,pentas-seni}.html`, `pages/galeri/{17-agustus,kegiatan-kelas,outdoor}.html`. CSS dipindah ke `assets/css/style.css`. Foto galeri dikelompokkan per momen: `assets/images/galeri/17-agustus/` (6), `kegiatan-kelas/` (11), `outdoor/` (11). Commit `7f1a746`. Judul/isi masih placeholder contoh — user bakal ganti & nambah momen sendiri. Perlu `git pull` + restart website di linux-tablet.
- **12 Agustus 2026:** Tambah section "Lokasi Kami" (#lokasi) di index.html — Google Maps embed (q=3.5271,98.6891, z=16, output=embed tanpa API key) + link "Petunjuk Arah". Commit `3b9570a`.
- **DNS cache lokal tablet** sempat nyimpen NXDOMAIN lama → kalau curl 000/ga resolve, bypass dengan `--resolve methodist-11.my.id:443:104.21.87.167` atau tunggu beberapa menit.
- **Error 1033** = DNS record bukan CNAME tunnel / hostname gak di-ingress → cek tab Public Hostname di dashboard Zero Trust.
- **JANGAN pakai quick tunnel** untuk domain ini — domain sudah route ke named tunnel "Linux HP".
- Tunnel lain di PC (e-rapor) pakai domain `eraportsdmethodist11.my.id` — beda zone, jangan ketuker.
- Aku (opencode) jalan di Termux (linux-tablet), bukan Debian — pkg manager: `pkg` (apt-based).
- Web server & tunnel pakai `setsid ... </dev/null` biar survive walaupun shell ditutup.
