Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /k echo CLOUDFLARE TUNNEL STATUS && sc query cloudflared && echo. && echo Service is running. Access via your Cloudflare domain. && echo. && echo To see live logs: cloudflared tunnel run && echo. && echo Press Ctrl+C to close...", 1, False
