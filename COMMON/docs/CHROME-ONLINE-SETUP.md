# Chrome Online - Remote Browser via noVNC

Tanggal: 4 September 2026
Status: AKTIF

## Konsep
Chrome berjalan di server Linux (headless), diakses dari browser mana saja via web (noVNC). 
Seperti "browser online" - buka link, langsung bisa pakai Chrome yang jalan di server.

## Teknologi
- **Google Chrome 152** (headless mode di virtual display)
- **Xvfb** (virtual framebuffer - display :99)
- **x11vnc** (VNC server, port 5900)
- **noVNC** (web-based VNC client, port 6080)
- **Cloudflare Quick Tunnel** (expose port 6080 ke internet)

## Ports
| Service | Port | Fungsi |
|---------|------|--------|
| Xvfb | display :99 | Virtual display |
| x11vnc | 5900 | VNC server |
| noVNC | 6080 | Web VNC client |
| Cloudflare | random | Tunnel ke internet |

## Cara Jalankan

### 1. Start Xvfb (Virtual Display)
```bash
setsid Xvfb :99 -screen 0 1280x720x24 -ac > /dev/null 2>&1 &
```

### 2. Start Chrome
```bash
setsid env DISPLAY=:99 google-chrome \
  --no-sandbox \
  --disable-gpu \
  --disable-dev-shm-usage \
  --disable-software-rasterizer \
  --window-size=1280,720 \
  --start-maximized \
  "https://www.google.com" > /dev/null 2>&1 &
```

### 3. Start x11vnc
```bash
setsid x11vnc -display :99 -forever -nopw -rfbport 5900 -shared -bg > /var/log/x11vnc.log 2>&1
```

### 4. Start noVNC
```bash
setsid /opt/noVNC/utils/novnc_proxy --vnc localhost:5900 --listen 6080 > /var/log/novnc.log 2>&1 &
```

### 5. Start Cloudflare Tunnel
```bash
setsid cloudflared tunnel --url http://localhost:6080 > /var/log/cloudflared-browser.log 2>&1 &
# URL akan muncul di log:
cat /var/log/cloudflared-browser.log | grep 'trycloudflare.com'
```

## Stop Semua
```bash
pkill -f "Xvfb :99"
pkill -f "google-chrome"
pkill -f "x11vnc"
pkill -f "websockify"
pkill -f "cloudflared tunnel --url http://localhost:6080"
```

## Limitasi
1. **1 device only** - Kalau buka di 2 device, yang kedua di-kick (tergantung session share)
2. **Download ke server** - File download nyimpan di `/root/Downloads`, bukan di PC user
3. **Quick tunnel URL berubah** tiap restart - cek log untuk URL baru
4. **RAM usage** - Chrome ~100-200MB, total server tetap aman

## Kegunaan
- Remote browser untuk akses akun premium (via Session Share extension)
- Bisa diakses dari PC/HP/manapun tanpa install apapun
- Cocok untuk user dengan banyak PC yang mau 1 Chrome bersama

## Dependencies
```bash
# Sudah terinstall di server:
- google-chrome-stable (152.0.7977.82)
- x11vnc
- Xvfb
- noVNC (git clone ke /opt/noVNC)
- cloudflared (2026.8.2)
```

## File Terkait
- `/var/log/x11vnc.log` - log VNC
- `/var/log/novnc.log` - log noVNC
- `/var/log/cloudflared-browser.log` - log tunnel (cek URL di sini)
- `/root/Downloads/` - folder download Chrome

---
*Setup oleh AI Assistant, 4 September 2026*
