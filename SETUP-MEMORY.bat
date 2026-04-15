@echo off
echo === Memory System Setup ===
echo.
echo Masukkan GitHub Repo URL dan Token
echo Contoh: https://github.com/yonathan-boop/OPENCODE
echo.
powershell -NoExit -Command "& { . '%~dp0setup-memory.ps1' }"