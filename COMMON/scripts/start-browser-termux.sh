#!/usr/bin/env bash
# start-browser.sh - Chrome Online (Xvfb + Chromium + x11vnc + noVNC + tunnel) di Termux
# Dibuat: 5 September 2026
# Pemakaian: bash start-browser.sh
# Setelah jalan, cek URL di log cloudflared-browser.log

PREFIX_DIR=/data/data/com.termux/files/usr
NOVNC="$PREFIX_DIR/share/noVNC"
DISPLAY_RES="1280x720x24"
LOGDIR="$HOME/.browser-logs"
mkdir -p "$LOGDIR"

export PATH="$PREFIX_DIR/bin:$PREFIX_DIR/share/noVNC/utils:$PATH"
export DISPLAY=:99

echo "=== START CHROME ONLINE (Termux) ==="

echo "[1/6] Xvfb (virtual display :99)..."
pkill -f "Xvfb :99" 2>/dev/null; sleep 1
( setsid Xvfb :99 -screen 0 $DISPLAY_RES -ac > "$LOGDIR/xvfb.log" 2>&1 & )

echo "[2/6] Chromium..."
pkill -f "chromium-browser" 2>/dev/null; sleep 1
( setsid env DISPLAY=:99 chromium-browser \
    --no-sandbox \
    --disable-gpu \
    --disable-dev-shm-usage \
    --disable-software-rasterizer \
    --disable-features=VizDisplayCompositor \
    --window-size=1280,720 \
    --start-maximized \
    "https://www.google.com" > "$LOGDIR/chromium.log" 2>&1 & )

echo "[3/6] x11vnc (port 5900)..."
pkill -f "x11vnc" 2>/dev/null; sleep 1
( setsid x11vnc -display :99 -forever -nopw -rfbport 5900 -shared -bg > "$LOGDIR/x11vnc.log" 2>&1 )

echo "[4/6] noVNC (port 6080)..."
pkill -f "novnc_proxy" 2>/dev/null; sleep 1
( cd "$NOVNC" && setsid ./utils/novnc_proxy --vnc localhost:5900 --listen 6080 > "$LOGDIR/novnc.log" 2>&1 & )

echo "[5/6] Cloudflare tunnel (URL acak)..."
pkill -f "cloudflared tunnel --url http://localhost:6080" 2>/dev/null; sleep 1
( setsid cloudflared tunnel --url http://localhost:6080 > "$LOGDIR/cloudflared-browser.log" 2>&1 & )

echo "[6/6] Cek status..."
sleep 6
printf "Tes Xvfb    : %s\n" "$(ps -e 2>/dev/null | grep -c Xvfb) proses"
curl -s -o /dev/null -m 8 -w "Tes noVNC    : http://localhost:6080 -> HTTP %{http_code}\n" http://localhost:6080/vnc.html || echo "noVNC belum siap"
echo "URL browser online terakhir:"
grep -o "https://[a-z0-9-]*\.trycloudflare\.com" "$LOGDIR/cloudflared-browser.log" 2>/dev/null | tail -1
echo "Log: "$LOGDIR/xvfb.log" | "$LOGDIR/chromium.log" | "$LOGDIR/x11vnc.log" | "$LOGDIR/novnc.log" | "$LOGDIR/cloudflared-browser.log""
