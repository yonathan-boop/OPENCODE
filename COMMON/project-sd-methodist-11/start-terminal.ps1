$ErrorActionPreference = 'Stop'
$ttydExe = Join-Path $env:LOCALAPPDATA 'opencode\tools\ttyd\ttyd.exe'
$logDir  = Join-Path $env:LOCALAPPDATA 'Temp\opencode'
$logFile = Join-Path $logDir 'ttyd-autostart.log'

function Write-Log($msg) {
    $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $msg
    try { Add-Content -LiteralPath $logFile -Value $line -Encoding utf8 } catch {}
    Write-Output $line
}

$portOpen = Get-NetTCPConnection -LocalPort 7681 -State Listen -ErrorAction SilentlyContinue
if ($portOpen) {
    Write-Log "PELUANGAN_PORT_7681: sudah ada listener (PID $($portOpen.OwningProcess)), skip start."
    exit 0
}

if (-not (Test-Path -LiteralPath $ttydExe)) {
    Write-Log "ERROR: ttyd tidak ditemukan di $ttydExe"
    exit 1
}

try {
    $logOut = Join-Path $logDir 'ttyd.out.log'
    $logErr = Join-Path $logDir 'ttyd.err.log'
    $p = Start-Process -FilePath $ttydExe -ArgumentList '-p','7681','-W','-b','/opencode','cmd.exe' -WorkingDirectory $env:USERPROFILE -WindowStyle Hidden -RedirectStandardOutput $logOut -RedirectStandardError $logErr -PassThru
    Write-Log "SUKSES_LAUNCH: ttyd PID=$($p.Id) port 7681 path /opencode"
} catch {
    Write-Log "ERROR_LAUNCH: $($_.Exception.Message)"
    exit 1
}

$ok = $false
for ($i = 0; $i -lt 10; $i++) {
    Start-Sleep -Seconds 1
    $chk = Get-NetTCPConnection -LocalPort 7681 -State Listen -ErrorAction SilentlyContinue
    if ($chk) { $ok = $true; break }
}
if ($ok) {
    Write-Log "VERIFIKASI_PORT_7681: OK, listener aktif."
    exit 0
} else {
    Write-Log "VERIFIKASI_PORT_7681: GAGAL - port 7681 tidak mendengarkan setelah 10 detik."
    exit 1
}