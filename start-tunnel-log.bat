@echo off
start /min "Cloudflare Tunnel" "C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:5774
exit
