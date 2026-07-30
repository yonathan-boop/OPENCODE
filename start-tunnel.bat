@echo off
start "Cloudflare Tunnel" /min "C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:5774
