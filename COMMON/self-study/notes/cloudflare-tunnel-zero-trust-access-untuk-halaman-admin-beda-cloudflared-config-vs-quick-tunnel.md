# Cloudflare Tunnel: Zero-Trust Access untuk Halaman Admin & Beda cloudflared Config vs Quick Tunnel

## Ringkasan

Cloudflare Tunnel = konnksi **outbound saja**: server/PC membuka koneksi keluar ke edge Cloudflare, jadi **tidak perlu buka port**, tidak butuh IP publik statis, dan tidak ada DNS publik yang menunjuk ke origin. Untuk mengamankan halaman admin (panel, dashboard, ttyd, dll), tinggal tumpuk **Cloudflare Zero Trust Access** di depannya — pengunjung harus login (email OTP, Google, dll) **sebelum satu byte pun sampai ke server**. Origin bahkan tidak pernah melihat trafik yang belum terautentikasi.

Ada **2 cara menjalankan tunnel** yang sering tertukar:

| | Quick Tunnel | Named Tunnel (cloudflared config / dashboard) |
|---|---|---|
| Perintah/konfig | `cloudflared tunnel --url http://localhost:PORT` | `cloudflared tunnel create <nama>` + config.yml / token dari dashboard |
| Butuh akun Cloudflare | Tidak perlu | Wajib (domain di Cloudflare DNS) |
| URL | Random `xxx.trycloudflare.com`, **berubah tiap restart** | Subdomain permanen milik sendiri (`admin.school.my.id`) |
| Batasan | 200 concurrent request, tidak support SSE; untuk **testing/demo saja** | Untuk produksi; stabil & permanen |
| Konfig routing | Cuma 1 origin via CLI | Bisa banyak hostname → banyak service via **ingress rules** atau dashboard |
| Zero Trust Access | Tidak bisa dipasang dengan baik (URL berubah) | Bisa — hostname tetap + Access Application |

**Catatan praktis:** quick tunnel dan named tunnel **bukan** hal yang saling menimpa — keduanya bisa jalan bersamaan. Di server kita sudah pakai dua-duanya: named tunnel `8f8b0f53` → methodist-11.my.id (produksi) dan quick tunnel untuk terminal ttyd (URL acak).

## Poin praktis untuk admin sekolah

1. **Lindungi panel admin dengan Access, bukan cuma password aplikasi.** Login aplikasi = 1 lapis. Access = lapis kedua di depan, validasi identitas sebelum request sampai ke origin. Pakai **Self-hosted application** di dashboard Zero Trust (`one.dash.cloudflare.com` → Access → Applications).
2. **Paling simpel: Email OTP** — user cukup pakai email, Cloudflare kirim kode tiap login. Tidak perlu Google/Entra SSO. Gratis di plan Zero Trust Free (≤50 user).
3. **Satu `cloudflared` cukup untuk banyak layanan** (50 user/panel). Tiap panel tinggal tambah Public Hostname baru dalam tunnel yang sama. Routing bisa dikelola dari:
   - **Dashboard** (remotely-managed, `config_src: cloudflare`) — tidak ada YAML di server, semua di UI; atau
   - **Config file lokal** (`/root/.cloudflared/config.yml`, `source: local`) — versi bisa di-git, tapi wajib diisi `ingress` dengan **catch-all `http_status:404`** di akhir.
   - Untuk setup yang sudah ada (server kita), Dashboard lebih aman dari `-f` isi file + tidak perlu restart service/cloudflared.
4. **Kalau halaman admin menerima webhook eksternal** (GitHub, Telegram, callback OAuth, healthcheck): buat **Access Application Bypass** untuk path spesifik itu (`Everyone`) **sebelum** membuat catch-all yang melindungi sisanya. Urutan penting — kalau catch-all dibuat duluan, webhook malah dapat form OTP dan automasi diam-diam rusak. Evaluasi Access: dari path yang paling spesifik → paling umum.
5. **Lapisan kedua (defense in depth):** origin tetap bisa minta header khusus (mis. Cloudflare **Service Token**) supaya kalau tunnel di-bypass, request langsung ditolak. Atau set `originRequest.access.audTag + required` di config sehingga cloudflared memvalidasi JWT Access sebelum meneruskan ke origin.
6. **Pengganti port exposure:** alih-alih buka port 80/443 ke panel + reverse proxy manual, cukup tunnel → CNAME `.cfargotunnel.com` otomatis dibuat → tidak ada alamat IP origin yang terpublikasi.

## Jebakan/error umum

- **Quick tunnel dipakai produksi** → URL berubah tiap restart → bookmark/user rusak. Batasan 200 req + tidak ada SSE.
- **Catch-all dibuat sebelum Bypass** → webhook eksternal dapat halaman OTP Cloudflare → deploy/callback gagal **diam-diam** (site terlihat hidup, request sukses 200).
- **Lupa catch-all di config.yml** → `cloudflared` menolak/error validasi ingress (`cloudflared tunnel ingress validate`).
- **Lupa backend service** → `localhost:PORT` salah port/hostname (mestinya nama service Docker internal, bukan localhost) → 502/530. Di server kita: 502/503 = origin 8090 mati, 1033/530 = DNS/tunnel.
- **Header `Cf-Access-Authenticated-User-Email`** diinjeksi ke app. Beberapa app auto-login berdasarkan header ini — cek perilaku app admin sebelum mengaktifkan.
- **Validasi JWT lewat `cf-access-ip`/client IP** itu menjebak: trafik lewat IP edge Cloudflare. Pakai `cf-connecting-ip`.
- **Case-insensitive webhook:** Access mengevaluasi per path + method; request POST dari GitHub dll harus masuk sebagai Bypass, jangan digantung policy login.
- TLS/konfig change dengan downtime minimal: jalanakan **replica cloudflared** dengan config baru, tunggu jalan, baru matikan instance lama (koneksi websocket/TCP akan drop saat instance pertama berhenti).

## Sumber

- Cloudflare Docs — Tunnel: Setup & Local-management config file: https://developers.cloudflare.com/tunnel/setup/, https://developers.cloudflare.com/tunnel/advanced/local-management/configuration-file/
- Cloudflare Docs — Access: choose application type: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/choose-application-type/
- Cloudflare API — Tunnel configurations (access audTag, config_src local/cloudflare): https://developers.cloudflare.com/api/node/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/configurations/
- José Manuel Ortega (2026-04-28) — memindahkan panel admin VPS ke Tunnel + Access, urutan Bypass vs catch-all: https://josemanuelortega.me/en/cloudflare-tunnel-and-access-to-take-admin-panels-off-the-internet
- The Linux Club (2026-03-22) — Cloudflare Tunnel + Zero Trust Access di Linux VPS, 2026: https://thelinuxclub.com/cloudflare-tunnel-with-zero-trust-access-on-linux-vps-2026-setup-guide/
- bigguyonstuff.com (2026-08-20) — /admin panel jangan publik, taruh di belakang Access: https://bigguyonstuff.com/cloudflare-tunnel-self-hosted-services/

---
*Catatan self-study SERVER, 2026-09-17. #cloudflare #tunnel #zero-trust #access #admin*