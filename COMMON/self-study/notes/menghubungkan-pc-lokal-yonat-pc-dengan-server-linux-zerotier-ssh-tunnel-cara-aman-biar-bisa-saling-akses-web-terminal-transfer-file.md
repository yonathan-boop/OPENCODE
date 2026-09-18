# Menghubungkan PC Lokal (yonat-PC) dengan Server Linux — ZeroTier / SSH / Tunnel

> Catatan: 2026-09-17 (klaim SERVER). Konteks: menghubungkan yonat-PC (Windows, PC utama)
> ke server Linux (/root/memory, host website) untuk akses web / terminal / transfer file.

## Ringkasan

Tiga jalur yang saling melengkapi untuk menghubungkan PC Windows ke server Linux:

1. **ZeroTier** → jaringan privat overlay (alamat 192.168.195.x). Paling pas untuk terminal (SSH),
   transfer file (SFTP/SCP), dan akses layanan lokal yang tidak mau diekspos ke internet umum.
2. **Cloudflare Tunnel** → sudah terpasang di server untuk web publik (methodist-11.my.id → 8090
   → serve8090.js) dan terminal web (ttyd port 7681, tunnel quick). Pas untuk akses dari luar
   sekolah tanpa perlu VPN.
3. **SSH/SFTP** → protokol akses & transfer file aman yang berjalan DI ATAS ZeroTier (atau internet,
   kalau port dibuka). Windows 10+ sudah punya client `ssh`, `scp`, `sftp` bawaan — tanpa instal.

Rekomendasi untuk admin sekolah: **ZeroTier untuk kerja internal (SSH + SFTP), Cloudflare Tunnel
untuk yang perlu diakses orang luar (website publik), JANGAN buka port SSH langsung ke internet.**

## Poin praktis untuk admin sekolah

### A. ZeroTier (jaringan privat — kunci utama)
- **Sisi server (sudah jalan, ON-DEMAND):** node `0f4e41072e`, network `633e31d8a2212ce2`
  ("my-first-network", PRIVATE), IP `192.168.195.60/24`. Detail & cara nyala/mati:
  `/root/SERVER-LINUX/docs/ZEROTIER.md`. Consumes RAM ~14 MB.
- **Sisi yonat-PC (yang perlu dilakukan):**
  1. Download MSI di https://zerotier.com/download (versi stabil 1.16.2). Saat install wajib
     approve driver (muncul prompt Windows).
  2. Tray icon → Join New Network → masukkan ID `633e31d8a2212ce2`.
  3. Login https://my.zerotier.com → network itu → **Authorize perangkat baru** (centang Auth?).
  4. Set IP managed yang mudah diingat (opsional), mis. `192.168.195.8` untuk yonat-PC.
  5. Tes: `ping 192.168.195.60` dari PC → harus balas.
- Setelah joined, dari PC bisa: `ssh root@192.168.195.60`, SFTP via WinSCP/FileZilla, dan akses
  layanan lokal server yang tidak dipublikasi.
- **Linux client** (mis. perangkat lain): `curl -s https://install.zerotier.com | bash` lalu
  `zerotier-cli join <NETWORK_ID>`. Di `Central` ada contoh auto-join via file kosong
  `<net-id>.conf` di `networks.d/` — berguna kalau mau auto-join saat service start.
- **Batas FREE plan (update 4 Agu 2026):** 10 device, 1 network, 1 admin; tanpa API, tanpa custom
  flow rules. Untuk 1 server + beberapa PC sekolah masih muat. Kalau >10 device → Essential $18/bln
  ($2/device tambahan). Catatan lisensi: Personal Plan untuk penggunaan non-komersial.

### B. Cloudflare Tunnel (akses web & terminal dari luar)
- Sudah produksi di server: tunnel bernama `8f8b0f53` → domain methodist-11.my.id (CNAME)
  → localhost:8090. Jangan pakai A/AAAA.
- Terminal web: ttyd port 7681 dengan auth (`admin:<password>`), tunnel quick (URL acak berubah
  tiap restart, cek `/var/log/cloudflared-terminal.log`). Berguna kalau perlu terminal tanpa
  klien SSH — tapi jangan jadi satu-satunya cara.
- Quick tunnel (`cloudflared tunnel --url localhost:PORT`) = bagus untuk demo/sementara;
  named tunnel + domain = permanen & stabil.
- Kalau butuh halaman admin terproteksi: pakai Zero Trust Access (lihat topik terkait di queue).

### C. SSH / transfer file (Window→Server) — langkah aman
- Sisi server: `apt install openssh-server` + `systemctl enable --now ssh`.
- Sisi PC (sudah ada di Windows 10/11): `ssh`, `scp`, `sftp` bawaan. GUI alternatif: **WinSCP**
  (drag-and-drop) atau FileZilla — protokol SFTP, port 22.
- Transfer contoh: `scp file.xlsx root@192.168.195.60:/root/memory/...` atau GUI WinSCP.
- **Hardening wajib sebelum dipakai lebih jauh:**
  - Buat kunci **Ed25519**: `ssh-keygen -t ed25519` (Windows: `ssh-keygen -t ed25519` di CMD/PS).
  - Pasang public key: `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server` (atau manual ke
    `~/.ssh/authorized_keys`, pastikan `chmod 700 ~/.ssh` & `chmod 600` file-nya).
  - Di `/etc/ssh/sshd_config`: `PermitRootLogin no`, `PasswordAuthentication no`,
    `ChallengeResponseAuthentication no`, `UsePAM no`, `PermitEmptyPasswords no`,
    `MaxAuthTries 3`, `AllowAgentForwarding no`. Lalu `sshd -t` + `systemctl restart ssh`.
  - **Urutan WAJIB:** tes login pakai key DULU, baru matikan password — kalau tidak, risiko
    terkunci dari server (kecuali ada console akses).
- Karena SSH hanya dibuka di jaringan ZeroTier (bukan internet), SSH tetap aman walau hardening
  belum sempurna — belapis-lapis.

## Jebakan / error umum

- **ZeroTier server nggak mau join network** → tanpa `chmod 666 /dev/net/tun`, daemon ONLINE tapi
  `listnetworks` kosong. Ini sudah jadi quirk server ini — selalu chmod dulu.
- **ZeroTier di Windows**: install minta admin; kalau antivirus/Windows Defender "Internet
  Security" ekstra aktif, bisa blokir install/service. Kalau tray app "System Service Not
  Reachable" → service zerotier-one berhenti / token authtoken tidak ter-copy ke user.
- **Lupa authorize di Central** → device join tapi tidak dapat IP (managed IP kosong).
- **Free plan berubah** — dari 25 device → 10 device, 1 network (per 4 Agu 2026). Beda doc
  lama-menulis 1 vs 3 network; pakai angka resmi terbaru.
- **SSH lockout** — mengubah `PasswordAuthentication no` sebelum memastikan key login jalan =
  risiko terkunci. Selalu tes di sesi terpisah lebih dulu.
- **Kapasitas/kecepatan transfer**: SFTP lebih aman dari FTP lama; jangan buka FTP/SMB ke
  internet. Linimasa SCP pakai `-P <port>` (kapital) kalau port bukan 22.
- **OneDrive di yonat-PC** bisa bikin file "hilang" sesaat saat sync — sebelum transfer file
  penting, pastikan file ada (Test-Path) dulu.
- **Jangan buka port 22/SSH ke internet publik** — bot scanner akan terus brute-force. Simpan SSH
  hanya di ZeroTier, atau bungkus dengan Cloudflare Access / fail2ban kalau terpaksa.
- **Konsistensi memory lintas mesin**: cara paling andal untuk sinkron file memory tetap
  **git pull/push** (bukan SMB/FTP) — sudah jadi standar kerja.

## Hasil di yonat-PC (18/9) — KONEK
- ZeroTier di yonat-PC: service Running, node `230f8f42a4`, **joined** network `633e31d8a2212ce2`
  (via `zerotier-cli join`, butuh admin/UAC; jalur `C:\Program Files (x86)\ZeroTier\One\zerotier-cli.bat`,
  jangan pakai `$env:ProgramFiles(x86)` di PS — salah parse jadi `C:\Program Files(x86)` [tanpa spasi]!).
- IP managed otomatis: **192.168.195.150/24** (persis saran awal, sudah authorized di Central).
- Verifikasi hidup: `ping 192.168.195.60` ~18ms · ttyd `http://192.168.195.60:7681/` → 401 (auth wall) ·
  SSH `192.168.195.60:2222` → banner `SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.14`.
- Server side sudah ALWAYS-ON (start-zerotier.sh + cron @reboot + guardian 15 mnt, 17/9).
- Calatan: sebelum server di-bikin permanen, peer server `0f4e41072e` muncul tanpa path (paths kosong)
  → gejala khas daemon ZT server mati/offline; cek ulang setelah server nyalakan/tidak on-demand.

## Sumber

- ZeroTier Docs — Getting Started & Create a Network: https://docs.zerotier.com/start/
- ZeroTier Docs — Client Configuration (Windows config paths, auto-join, token):
  https://docs.zerotier.com/config
- ZeroTier Docs — Enterprise Deployment Guide (auto-join `<net-id>.conf`):
  https://docs.zerotier.com/enterprise-deployment
- ZeroTier Docs — Windows FAQ & Troubleshooting (driver/antivirus/RDP):
  https://docs.zerotier.com/faq-windows
- ZeroTier Pricing (4 Agu 2026): https://www.zerotier.com/pricing
- Microsoft Learn — OpenSSH for Windows overview:
  https://learn.microsoft.com/en-us/windows-server/administration/OpenSSH/openssh-overview
- Microsoft Learn — Troubleshoot common SFTP issues (Windows OpenSSH):
  https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-sftp-issues-using-openssh
- OpenSSH Security hardening — Mozilla Infosec:
  https://infosec.mozilla.org/guidelines/openssh
- SSH hardening step-by-step (NOC.org, 2026): https://noc.org/learn/securing-ssh
- Resmi tentang SCP/SFTP: man7.org `sftp(1)` & Red Hat blog "How to use SCP and SFTP"
- Konteks internal (sisi server): `/root/SERVER-LINUX/docs/ZEROTIER.md` &
  `memory/COMMON/docs/CATATAN-TUNNEL.txt` (#zerotier #tunnel #sftp #ssh #cloudflare)