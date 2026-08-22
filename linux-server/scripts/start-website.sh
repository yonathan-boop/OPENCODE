#!/usr/bin/env bash
# Hidupkan website SD Methodist-11 di server Linux (methodist-11.my.id)
# Pemakaian: bash ~/memory/linux-server/scripts/start-website.sh
# Tunnel: 8f8b0f53-c70d-4bec-85d9-34e24da3c8ff (dashboard-managed, ingress: methodist-11.my.id -> http://localhost:8090)

WEB_DIR="$HOME/memory/COMMON/project-sd-methodist-11"
LOG_WEB="/var/log/sd-website.log"
LOG_TUNNEL="/var/log/cloudflared-tunnel.log"
TOKEN="eyJhIjoiZmZkYjFjNDNiZmIxY2M0ZmFhYjdlMzIzNmJkYzNiOTUiLCJ0IjoiOGY4YjBmNTMtYzcwZC00YmVjLTg1ZDktMzRlMjRkYTNjOGZmIiwicyI6IlltWm1PVGMxTVRndE1ETTBPQzAwTXpZMExUZzNaR1l0WWpWaE56Y3pNVEZtTldVdyJ9"

echo "=== HIDUPKAN WEBSITE SD METHODIST-11 ==="

echo "[1/2] Web server Node port 8090..."
pkill -f serve8090.js 2>/dev/null
sleep 1
( setsid node "$WEB_DIR/serve8090.js" >"$LOG_WEB" 2>&1 </dev/null & )

echo "[2/2] Cloudflare Tunnel 8f8b0f53..."
pkill -f "cloudflared tunnel" 2>/dev/null
sleep 1
( setsid cloudflared tunnel run --token "$TOKEN" >"$LOG_TUNNEL" 2>&1 </dev/null & )

sleep 5
curl -s -o /dev/null -m 10 -w "Tes lokal  : http://localhost:8090 -> HTTP %{http_code}\n" http://localhost:8090/
curl -s -o /dev/null -m 30 -w "Tes publik : https://methodist-11.my.id -> HTTP %{http_code}\n" https://methodist-11.my.id/
echo "Log: $LOG_WEB | $LOG_TUNNEL"
