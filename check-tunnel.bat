@echo off
echo ===== CLOUDFLARE TUNNEL STATUS =====
echo.
sc query cloudflared | findstr /i "STATE"
echo.
echo Press any key to open live log...
pause >nul
sc start cloudflared
"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel run
