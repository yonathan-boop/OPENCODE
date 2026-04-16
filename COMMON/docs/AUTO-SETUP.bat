@echo off
REM === AUTO MEMORY SETUP ===
echo.
echo Masukkan data berikut:
echo.
set /p URL="GitHub URL: https://github.com/yonathan-boop/OPENCODE
set /p TOKEN="GitHub Token: "

set GITHUB_TOKEN=%TOKEN%
set MEMDIR=%USERPROFILE%\Desktop\memory

if not exist "%MEMDIR%" mkdir "%MEMDIR%"
cd /d "%MEMDIR%"

echo.
echo Downloading from GitHub...
git clone https://yonathan-boop:%TOKEN%@github.com/yonathan-boop/OPENCODE.git . 2>nul
git pull origin main --allow-unrelated-histories 2>nul

echo.
echo === SELESAI ===
echo PC: %COMPUTERNAME%
pause