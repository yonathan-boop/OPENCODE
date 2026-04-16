@echo off
REM Auto Memory System - Load from GitHub
REM Usage: Double click atau jalankan di terminal

cd /d "%~dp0"

echo [AUTO-MEMORY] Loading latest memory from GitHub...
git pull

echo [DONE] Memory loaded!
pause