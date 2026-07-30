Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c ""C:\Program Files (x86)\cloudflared\cloudflared.exe"" tunnel --url http://localhost:5774 > ""C:\Users\Digitalisasi\Desktop\tunnel-log.txt"" 2>&1", 0, False
