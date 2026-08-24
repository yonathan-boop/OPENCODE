# ZeroTier di Server Linux

==========================
#zerotier #network #vlan #smb #wilianto #tunnel
=========================

Di-install: 24 Agustus 2026 (server Linux root, Ubuntu 22.04 container)

## Info ZeroTier
- Versi: zerotier-one 1.16.2 (install via curl -s https://install.zerotier.com | bash)
- Node address server ini: **0f4e41072e**
- Network joined: **633e31d8a2212ce2** ("my-first-network", PRIVATE) — status OK
- IP ZeroTier server ini: **192.168.195.60/24** (interface ztxoobb5ca)

## PENTING: Cara Start Manual (server TIDAK punya systemd aktif)
Setelah reboot container, jalankan:
```bash
chmod 666 /dev/net/tun        # WAJIB — default permission 600 (root only), daemon jalan sebagai user zerotier-one
setsid zerotier-one -d < /dev/null > /var/log/zerotier-startup.log 2>&1 &
```
- Tanpa `chmod 666 /dev/net/tun`, daemon ONLINE tapi network GAK mau nempel (error TUN/TAP saat join).
- Gejala tanpa chmod: `join OK` tapi `listnetworks` kosong padahal peers ke-list.
- Pertimbangkan: masukkan ke start-website.sh supaya auto jalan setelah reboot.

## Perangkat Lain di Network ZeroTier
| Device | IP ZeroTier | Keterangan |
|--------|-------------|------------|
| Server Linux (ini) | 192.168.195.60 | node 0f4e41072e |
| PC Wilianto | **192.168.195.7** | ping OK ~30ms |

## PC Wilianto via ZeroTier (hasil scan 24 Agu 2026)
- Port OPEN: 445/139 (SMB), 8090 (web server lama serve8090.js masih hidup!)
- Port CLOSED: 22 (SSH), 3389 (RDP), 5985 (WinRM), 80 (HTTP)
- Akses file: SMB via smbclient, akun `wilianto` (password = sama dengan username)
- Contoh baca (READ-ONLY):
  ```
  smbclient //192.168.195.7/Users -U 'wilianto%wilianto' -c 'ls'
  smbclient //192.168.195.7/Users -U 'wilianto%wilianto' -c 'cd WILIANTO\memory; ls'
  smbclient //192.168.195.7/Desktop -U 'wilianto%wilianto' -c 'ls'
  ```
- Share tersedia: C$, D$, Data_B, Desktop, Downloads, Users, Methodist-11 Document Disk, Methodist-11 File Disk
- **Share rusak:** `Methodist-11 Document Disk` & `Methodist-11 File Disk` → NT_STATUS_BAD_NETWORK_NAME (folder tujuan sudah tidak ada/di-rename di PC Wilianto)
- **Memory clone di Wilianto STALE:** terakhir sync 15 Agustus 2026 (tertinggal 9 hari dari repo)

## Aturan User
- Di PC Wilianto (atau mesin lain via ZeroTier): LIHAT SAJA, jangan otak-atik apapun tanpa izin.
