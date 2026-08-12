# WEBSITE SD METHODIST-11 + CLOUDFLARE TUNNEL (linux-tablet)

Di-update: 12 Agustus 2026 (restrukturisasi)

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

- **12 Agustus 2026 — RESTRUKTURISASI:** Website jadi multi-halaman. `index.html` = ringkasan terbaru (3 kartu per section: Pengumuman, Kegiatan, Galeri momen). Detail pindah halaman di `pages/` (sub folder): `pages/pengumuman/{imunisasi,obat-cacing,juara-kelas}.html`, `pages/kegiatan/{17-agustus,ibadah-rutin,pentas-seni}.html`, `pages/galeri/{17-agustus,kegiatan-kelas,outdoor}.html`. CSS dipindah ke `assets/css/style.css`. Foto galeri dikelompokkan per momen: `assets/images/galeri/17-agustus/` (6), `kegiatan-kelas/` (11), `outdoor/` (11). Commit `7f1a746`. Judul/isi masih placeholder contoh — user bakal ganti & nambah momen sendiri. Perlu `git pull` + restart website di linux-tablet.
- **12 Agustus 2026:** Tambah section "Lokasi Kami" (#lokasi) di index.html — Google Maps embed (q=3.5271,98.6891, z=16, output=embed tanpa API key) + link "Petunjuk Arah". Commit `3b9570a`.
- **DNS cache lokal tablet** sempat nyimpen NXDOMAIN lama → kalau curl 000/ga resolve, bypass dengan `--resolve methodist-11.my.id:443:104.21.87.167` atau tunggu beberapa menit.
- **Error 1033** = DNS record bukan CNAME tunnel / hostname gak di-ingress → cek tab Public Hostname di dashboard Zero Trust.
- **JANGAN pakai quick tunnel** untuk domain ini — domain sudah route ke named tunnel "Linux HP".
- Tunnel lain di PC (e-rapor) pakai domain `eraportsdmethodist11.my.id` — beda zone, jangan ketuker.
- Aku (opencode) jalan di Termux (linux-tablet), bukan Debian — pkg manager: `pkg` (apt-based).
- Web server & tunnel pakai `setsid ... </dev/null` biar survive walaupun shell ditutup.
