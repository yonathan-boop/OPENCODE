# Keamanan Server Linux Kecil (Single VPS): Hardening Dasar, Update, Monitoring

Dicatat: 17 September 2026 (self-study). Berlaku umum untuk VPS Linux single (Debian/Ubuntu) — termasuk server SD Methodist-11. Untuk SSH praktis di konteks sekolah kaca dalam note: `menghubungkan-pc-lokal-yonat-pc-dengan-server-linux-zerotier-ssh-tunnel...md`.

## Ringkasan

Server di internet publik mulai "diketuk" bot dalam hitungan **menit** setelah IP live. Tiga celah bawaan yang paling sering dipakai attacker di VPS baru: (1) login root + password SSH terbuka, (2) tidak ada firewall (default-deny), (3) update keamanan tidak pernah jalan. Hardening dasar menutup ~99% serangan otomatis dalam 30–60 menit. Prinsip utamanya **defense-in-depth** (berlapis), bukan satu tool andalan.

## Poin praktis untuk admin sekolah

### Urutan langkah (paling penting: urutannya benar)
1. **Update dulu sebelum hardening** — `apt update && apt full-upgrade`. Image VPS sering ketinggalan patch berbulan-bulan; jangan hardening di atas lubang yang sudah diketahui.
2. **Buat user admin bernama** (bukan root): user + sudo, key SSH, lalu `PermitRootLogin no`.
3. **Firewall default-deny** — `ufw default deny incoming; ufw default allow outgoing; ufw allow OpenSSH; ufw enable`. **Allow SSH SEBELUM enable**, atau kunci diri sendiri.
4. **fail2ban** untuk brute-force.
5. **Auto-update keamanan** (`unattended-upgrades`).
6. Baru sisanya: sinkronisasi waktu, matikan service tak terpakai, backup teruji-restore, monitoring eksternal, audit Lynis.

### SSH ringkas (detail ada di note ZeroTier/SSH)
- Key-only (`PasswordAuthentication no`), `PermitRootLogin no`, `MaxAuthTries 3`, `KbdInteractiveAuthentication no`.
- Pakai drop-in `/etc/ssh/sshd_config.d/99-hardening.conf` supaya survive package upgrade (jangan edit `sshd_config` utama yang bisa ditimpa).
- Generasi key: `ssh-keygen -t ed25519`. Private key jangan pernah diupload/share.
- Ganti port SSH **opsional** — hanya memangkas noise bot, BUKAN security; jangan jadikan pengganti key+firewall.
- `sshd -t` sebelum reload → selalu, atau bisa kunci diri.
- Ubuntu 26.04: SSH socket-activated → stop/disable `ssh.socket` & enable `ssh.service` biar start saat boot.
- Workflow aman saat ubah konfigurasi: cek web console provider bisa dipakai → simpan sesi SSH lama tetap terbuka → uji dari sesi baru → baru tutup sesi lama.

### Firewall
- Aturan: **deny semua inbound → allow hanya yang perlu**. Web = 80/443 (443 aja kalau sudah force HTTPS).
- Database (3306/5432) **jangan pernah** dibuka ke internet — bind ke `127.0.0.1` atau jaringan privat, lalu allow per-subnet kalau perlu.
- `ufw limit <port>/tcp` untuk rate-limit koneksi (6/30 detik per IP) — lapisan sebelum fail2ban.
- Cek IPv6: pastikan `IPV6=yes` di `/etc/default/ufw` (attacker suka lewat alamat v6 yang lupa difilter).
- ⚠️ **Docker + UFW**: traffic ke port publish Docker mem-bypass `INPUT` chain UFW — port bisa tetap kebuka walau UFW terlihat deny. Pakai chain `DOCKER-USER`. Jangan ikut pile/disable iptables Docker.
- Jangan menumpuk UFW + nftables manual + firewalld sekaligus tanpa paham urutannya.

### Update & patch
- `unattended-upgrades` terinstall & enabled oleh default di Ubuntu — **jangan asumsi, verifikasi** (`systemctl status unattended-upgrades`, dry-run `unattended-upgrade --dry-run --debug`).
- Default hanya update keamanan (aman: tidak ubah perilaku). Kernel butuh reboot → set `Automatic-Reboot "true"` + waktu (`Automatic-Reboot-Time "02:30"`) **hanya kalau** workload aman reboot sendiri; kalau enggak, jadwalkan reboot manual di jam sepi.
- Aktivasi alternatif: Ubuntu Pro free tier (≤5 mesin) untuk Livepatch (patch kernel tanpa reboot) + ESM.
- Yang wajib dimonitor: timer/service update gagal, umur run terakhir, reboot tertahan >1 minggu, paket ter-hold.

### Monitoring & logging
- Skala kecil cukup: **uptime check eksternal gratis** (UptimeRobot / Healthchecks.io) — kirim email kalau mati. Ini satu-satunya cara tahu server mati padahal "di dalam sepertinya baik-baik saja".
- Resouce: `htop`, `df -h`, `journalctl -p err -b`, `ss -tulpn` (audit port). Di server sekolah sudah ada `monitor-server.sh` (health.json) + crontab — gunakan itu.
- Log: simpan bounded di lokal (`SystemMaxUse`, rotasi) + **kirim off-host** (attacker yang jadi root bisa hapus log lokal). Timeline butuh jam sinkron (`timedatectl` → `System clock synchronized: yes`).
- Alert minimal yang berguna: kegagalan SSH auth di atas ambang, pemakaian sudo, backup gagal (kegagalan crontab senyap = gap klasik), TLS cert expire <21 hari.
- Audit berkala: `lynis audit system` → skor 70-an sudah solid untuk single server; jangan kejar 100 (poin terakhir = compliance server besar). Jalankan ulang setelah perubahan besar.

### Lain-lain bernilai tinggi
- **Backup = security control** (ransomware & human error). Yang diuji-restore = yang benar. Lihat note `backup-3-2-1-...`.
- **systemd sandboxing** unit service (ProtectSystem, NoNewPrivileges, PrivateTmp) = kurangi blast radius tanpa container.
- Sebelum ubah firewall/SSH: verifikasi web console/rescue provider berfungsi. Rollback SSH: console → revert config → `sshd -t` → restart. Recovery nft: `nft flush ruleset`. UFW: `ufw disable`.
- Snapshot provider sebelum hardening besar + sesudah = restore-ready baseline.
- Cek service yang terbuka: `ss -tulpn`, matikan yang tak dipakai (cups, bluetooth, avahi, postfix bila tak kirim mail).

## Jebakan / error umum
- **Terkunci keluar**: enable UFW tanpa allow SSH dulu, atau reload sshd tanpa `sshd -t`. Solusi: web console provider.
- **Ubuntu 26.04 SSH tidak start setelah reboot** karena socket activation (`ssh.socket` disabled, `ssh.service` disabled by default).
- **fail2ban "No file(s) found for sshd"**: distro modern baca journal bukan `/var/log/auth.log` → set `backend = systemd` di jail override.
- **UFW "Operation not permitted"**: firewall lain (container runtime / iptables-nft conflict) mengklaim tables → `ufw --force reset` lalu enable ulang.
- **Docker port tetap kebuka walau UFW deny** → pakai chain `DOCKER-USER`.
- **Ubah config di `sshd_config` utama** → ditimpa saat package upgrade; pakai drop-in `.d/`.
- **Jangan copy seluruh `jail.conf` ke `jail.local`** (mengunci default lama yang sudah diperbaiki) — cukup override di `jail.d/`.
- **Hanya andalkan local log** untuk monitoring — server mati total tidak akan lapor; butuh probe eksternal.
- **API key / secret pernah masuk git** pernah kena blokir (LRN-20260917-001) — secret jangan pernah di repo; pakai env file di luar git (contoh: `~/.config/gemini-api-key`).

## Sumber
- HostMyCode — Linux VPS hardening checklist 2026 (SSH, firewall, updates, audit-ready): hostmycode.com/blog/linux-vps-hardening-checklist-2026
- OuiHeberg — Secure a Linux VPS 2026 (Debian/Ubuntu), level batters & jebakan Docker: ouiheberg.com/en/documentation/article/secure-a-linux-vps-the-complete-checklist
- StackHarden — Pre-launch VPS Security Checklist: stackharden.com/checklist/vps-launch-security
- itrpoka — Secure a New VPS: The First-Hour Checklist (2026): itrpoka.com/blog/secure-new-vps-checklist
- ComputingForgeeks — Harden Ubuntu 26.04 LTS (OpenSSH 10.2/socket-activated, UFW limit, fail2ban systemd backend): computingforgeeks.com/harden-ubuntu-2604-server
- ZeriFlow — VPS Security Hardening Complete Checklist 2026: zeriflow.com/blog/vps-server-security-hardening-guide
- kennyvn — How to Secure a Linux Server: hardeningguide.com 2026: kennyvn.com/linux-server-hardening
- hostingdiscounts.org — How to Secure a VPS: Ubuntu Hardening Checklist: hostingdiscounts.org/how-to-secure-a-vps

Referensi internal: MASTER-MEMORY (bagian SERVER LINUX), note ZeroTier/SSH, backup-3-2-1.