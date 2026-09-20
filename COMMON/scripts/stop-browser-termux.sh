#!/usr/bin/env bash
# stop-browser-termux.sh - Matikan semua Chrome Online di Termux
pkill -f "Xvfb :99" 2>/dev/null
pkill -f "chromium-browser" 2>/dev/null
pkill -f "x11vnc" 2>/dev/null
pkill -f "novnc_proxy" 2>/dev/null
pkill -f "cloudflared tunnel --url http://localhost:6080" 2>/dev/null
echo "Semua proses Chrome Online dimatikan."
