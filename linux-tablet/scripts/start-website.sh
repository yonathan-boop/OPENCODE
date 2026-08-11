#!/data/data/com.termux/files/usr/bin/bash

WEB_DIR="/data/data/com.termux/files/home/OPENCODE/COMMON/project-sd-methodist-11"
PORT=8090
TUNNEL_LOG="/data/data/com.termux/files/home/OPENCODE/linux-tablet/docs/tunnel.log"
TOKEN="eyJhIjoiZmZkYjFjNDNiZmIxY2M0ZmFhYjdlMzIzNmJkYzNiOTUiLCJ0IjoiOTEyYTIyZmEtMDUxYS00ODkxLTg5N2EtZjJmZjIwZjJkNWYyIiwicyI6IllqUXlNMkptTVdVdE0yTmpOUzAwTlRoaExXRTRPVEF0WldFM1lXSXpObVl3WW1KayJ9"

echo "=== HIDUPKAN WEBSITE SD METHODIST-11 ==="

pkill -f "http.server $PORT" 2>/dev/null
pkill -f "cloudflared tunnel run" 2>/dev/null
sleep 1

echo "[1/2] Menyalakan web server di port $PORT..."
setsid python3 -m http.server $PORT --directory "$WEB_DIR" >/dev/null 2>&1 </dev/null &

echo "[2/2] Menyalakan Cloudflare Tunnel (methodist-11.my.id)..."
setsid cloudflared tunnel run --token "$TOKEN" > "$TUNNEL_LOG" 2>&1 </dev/null &

sleep 8

curl -s -o /dev/null -w "web lokal localhost:$PORT -> HTTP %{http_code}\n" --max-time 5 "http://localhost:$PORT/"

curl -s -o /dev/null -w "domain methodist-11.my.id -> HTTP %{http_code}\n" --max-time 25 --resolve methodist-11.my.id:443:104.21.87.167 "https://methodist-11.my.id/"

echo "Selesai. Website: https://methodist-11.my.id"
