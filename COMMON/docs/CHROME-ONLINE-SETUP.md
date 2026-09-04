# Chrome Online - Remote Browser via noVNC

Tanggal: 4 September 2026
Status: **WORK IN PROGRESS** - Chrome jalan tapi layar hitam/kosong di noVNC

## Konsep
Chrome berjalan di server Linux, diakses dari browser mana saja via web (noVNC).
Integrasi ke domain: `methodist-11.my.id/chrome/`

## Arsitektur (via nginx reverse proxy)
```
methodist-11.my.id           → localhost:8090 (website)
methodist-11.my.id/chrome    → localhost:6080 (noVNC/Chrome)
methodist-11.my.id/terminal  → localhost:7681 (ttyd)
methodist-11.my.id/opencode  → localhost:7681 (ttyd, alias)
```

## Ports
| Service | Port | Fungsi |
|---------|------|--------|
| nginx | 81 | Reverse proxy (Cloudflare tunnel → port 81) |
| Xvfb | display :99 | Virtual display |
| x11vnc | 5900 | VNC server |
| noVNC | 6080 | Web VNC client |

## Cara Jalankan
Script: `/root/chrome-online-start.sh`

```bash
bash /root/chrome-online-start.sh
```

## Masalah yang Ditemui (4 September 2026)
1. **Layar hitam/kosong di noVNC** — Chrome jalan di server (window 1279x719) tapi noVNC显示不出来. Kemungkinan masalah x11vnc auth atau rendering.
2. **Chrome window 1x1 tanpa WM** — Tanpa window manager, Chrome cuma bikin window kecil. Perlu install **fluxbox** (sudah terinstall).
3. **Proses Chrome/fluxbox mati sendiri** — Sering crash/terminate setelah beberapa detik.
4. **Lelet** — VNC memang bandwidth-heavy (~100-500KB per frame vs ~5KB untuk website statis).

## Yang Sudah Works
- ✅ nginx reverse proxy (port 81) → website + terminal + chrome routing
- ✅ `methodist-11.my.id` → website
- ✅ `methodist-11.my.id/terminal/` dan `/opencode/` → terminal online
- ✅ `methodist-11.my.id/chrome/` → noVNC page (200)
- ✅ Cloudflare tunnel diarahkan ke nginx:81
- ✅ Quick tunnel lama sudah dimatikan

## Yang Belum Works
- ❌ Chrome display di noVNC (hitam/kosong)
- ❌ Proses Chrome stabil (sering crash)
- ❌ Performance VNC (lelet)

## Dependencies
```bash
# Sudah terinstall:
- google-chrome-stable (152.0.7977.82)
- x11vnc
- Xvfb
- fluxbox (window manager)
- noVNC (git clone ke /opt/noVNC)
- nginx (1.18.0, config: /etc/nginx/sites-available/reverse-proxy)
- cloudflared (2026.8.2)
```

## File Terkait
- `/etc/nginx/sites-available/reverse-proxy` — nginx config
- `/root/chrome-online-start.sh` — start script
- `/var/log/x11vnc.log` — log VNC
- `/var/log/novnc.log` — log noVNC

## TODO (Sesi Berikutnya)
1. Fix Chrome display — kemungkinan perlu `x11vnc -auth guess` atau setup Xauthority properly
2. Test `DISPLAY=:99 xwd -root -out /tmp/screen.xwd` → convert ke PNG → cek apakah display benar
3. Pertimbangkan alternatif: **KasmVNC** atau **Apache Guacamole** (lebih stabil untuk remote browser)
4. Cache startup script di systemd/supervisor biar auto-restart

---
*Setup oleh AI Assistant, 4 September 2026 (updated)*
