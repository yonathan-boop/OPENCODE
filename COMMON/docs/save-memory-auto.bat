@echo off
REM Auto Memory System - Save to GitHub
REM Usage: Double click atau jalankan di terminal

cd /d "%~dp0"

echo [AUTO-MEMORY] Saving changes to GitHub...
git add -A
git commit -m "Auto-save: %date% %time%" 2>nul
git pull
git push

echo [DONE] Memory saved to GitHub!
pause