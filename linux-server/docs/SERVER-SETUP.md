# SERVER LINUX — WEBSITE SD METHODIST-11 + RECOVERY

Di-update: 22 Agustus 2026

## Status: AKTIF & LIVE
- **URL publik:** https://methodist-11.my.id (HTTP 200, dicek 22/8/2026)
- **Server:** Linux VPS lama milik user (root, sudah online >5 bulan, bisa mati kapan saja)
- **Memory:** /root/memory (clone dari GitHub)

## Komponen

| Komponen | Detail |
|----------|--------|
| File website | `/root/memory/COMMON/project-sd-methodist-11/` |
| Web server | Node `serve8090.js` port 8090 (log: /var/log/sd-website.log) |
| cloudflared | v2026.8.2 via .deb GitHub releases |
| Tunnel | ID `8f8b0f53-c70d-4bec-85d9-34e24da3c8ff`, dashboard-managed (token) |
| Token tunnel | `linux-server/scripts/start-website.sh` (variabel TOKEN) |
| DNS | CNAME `@` -> `8f8b0f53-c70d-4bec-85d9-34e24da3c8ff.cfargotunnel.com`, proxy ON |
| Public Hostname | methodist-11.my.id -> http://localhost:8090 (Zero Trust dashboard) |

## Cara nyalakan (1 perintah)

    bash ~/memory/linux-server/scripts/start-website.sh

## RECOVERY TOTAL (server mati -> pindah server baru)

1. Install git, node, python3, curl
2. Clone memory:
       git clone https://<TOKEN>@github.com/yonathan-boop/OPENCODE.git ~/memory
   (folder clone WAJIB bernama `memory` di home root, path lain tinggal sesuaikan)
3. Install cloudflared:
       curl -fsSL -o /tmp/cf.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && dpkg -i /tmp/cf.deb
4. Setup config opencode (instructions auto-load memory):
   - Buat `~/.config/opencode/opencode.json` dengan "instructions" menunjuk ke:
     VS&OPENCODE/{SOUL,USER,AGENTS}.md, COMMON/docs/{MASTER-MEMORY,MEMORY-LEARNINGS,MEMORY-ERRORS}.md, PC-06/{summary,facts}.md
   - Lalu: opencode auth login (pilih provider)
5. Jalankan: bash ~/memory/linux-server/scripts/start-website.sh
6. DNS tidak perlu diubah (tunnel ID sama, CNAME masih valid)

## Catatan penting

- TIDAK ada systemd di server ini -> proses pakai pola double-fork setsid (lihat script). Setelah reboot WAJIB jalankan script lagi.
- Error 1033/530 = DNS record tidak menunjuk ke tunnel aktif -> cek DNS CNAME & tab Public Hostname.
- Config push dari dashboard ke cloudflared butuh ~30 detik setelah disimpan.
- Tunnel-tunnel LAMA (tidak dipakai): 21b93a76 (PC Wilianto), pc-06/34a83caa, Linux HP/912a22fa.
- GitHub token classic user dipakai di remote URL (tanpa expiry) — kalau revoke, semua remote perlu token baru.
