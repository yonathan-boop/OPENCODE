#!/data/data/com.termux/files/usr/bin/bash

TUNNEL_LOG="/data/data/com.termux/files/home/OPENCODE/linux-tablet/docs/tunnel.log"
TOKEN="eyJhIjoiZmZkYjFjNDNiZmIxY2M0ZmFhYjdlMzIzNmJkYzNiOTUiLCJ0IjoiMjhkMTQyNTUtZDMyMS00ZDU1LWFhM2UtOTJjNjhlZDllN2QxIiwicyI6Ik5UQXpOV1kyTlRNdE1UVmhPUzAwTTJRd0xUa3lZemN0Wm1Nd1lXSTVZMlE0WW1RNCJ9"

echo "=== HIDUPKAN WEBSITE + TERMINAL ONLINE (methodist-11) ==="

pkill -f "http.server 8090" 2>/dev/null
pkill -f "cloudflared tunnel run" 2>/dev/null
pkill -f "nginx" 2>/dev/null
pkill -f "gotty" 2>/dev/null
sleep 1

echo "[1/4] Web server website (port 8090)..."
setsid python3 -m http.server 8090 --directory "/data/data/com.termux/files/home/OPENCODE/COMMON/project-sd-methodist-11" >/dev/null 2>&1 </dev/null &

echo "[2/4] Terminal online (gotty port 7681, /opencode)..."
SVDIR=/data/data/com.termux/files/usr/var/service sv up gotty >/dev/null 2>&1 &

echo "[3/4] Reverse proxy nginx (port 8081) -> website + terminal..."
SVDIR=/data/data/com.termux/files/usr/var/service sv up nginx >/dev/null 2>&1 &

echo "[4/4] Cloudflare Tunnel..."
setsid cloudflared tunnel run --token "$TOKEN" > "$TUNNEL_LOG" 2>&1 </dev/null &

sleep 8

curl -s -o /dev/null -w "web localhost:8090       -> HTTP %{http_code}\n" --max-time 5 "http://localhost:8090/"
curl -s -o /dev/null -w "nginx localhost:8081       -> HTTP %{http_code}\n" --max-time 5 "http://localhost:8081/"
curl -s -o /dev/null -w "terminal localhost:8081/opencode -> HTTP %{http_code}\n" --max-time 5 "http://localhost:8081/opencode/"
curl -s -o /dev/null -w "domain methodist-11.my.id -> HTTP %{http_code}\n" --max-time 25 "https://methodist-11.my.id/"
curl -s -o /dev/null -w "domain methodist-11.my.id/opencode -> HTTP %{http_code}\n" --max-time 25 "https://methodist-11.my.id/opencode/"

echo "Selesai. Website: https://methodist-11.my.id | Terminal: https://methodist-11.my.id/opencode"