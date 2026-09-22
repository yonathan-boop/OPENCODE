$ErrorActionPreference = 'Stop'
$nodePath = 'C:\Program Files\nodejs\node.exe'
$siteDir  = 'C:\Users\WILIANTO\memory\COMMON\project-sd-methodist-11'
$scriptFile = Join-Path $siteDir 'serve8090.js'
$logDir  = 'C:\Users\WILIANTO\AppData\Local\Temp\opencode'
$logFile = Join-Path $logDir 'serve8090-autostart.log'

function Write-Log($msg) {
    $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $msg
    try { Add-Content -LiteralPath $logFile -Value $line -Encoding utf8 } catch {}
    Write-Output $line
}

$portOpen = Get-NetTCPConnection -LocalPort 8090 -State Listen -ErrorAction SilentlyContinue

if ($portOpen) {
    Write-Log "PELUANGAN_PORT_8090: sudah ada listener (PID $($portOpen.OwningProcess)), skip start."
    exit 0
}

if (-not (Test-Path -LiteralPath $nodePath)) {
    Write-Log "ERROR: node tidak ditemukan di $nodePath"
    exit 1
}

if (-not (Test-Path -LiteralPath $scriptFile)) {
    Write-Log "ERROR: serve8090.js tidak ditemukan di $scriptFile"
    exit 1
}

try {
    $logStdout = Join-Path $logDir 'serve8090.out.log'
    $logStderr = Join-Path $logDir 'serve8090.err.log'
    $p = Start-Process -FilePath $nodePath -ArgumentList $scriptFile -WorkingDirectory $siteDir -WindowStyle Hidden -RedirectStandardOutput $logStdout -RedirectStandardError $logStderr -PassThru
    Write-Log "SUKSES_LAUNCH: node serve8090.js PID=$($p.Id)"
} catch {
    Write-Log "ERROR_LAUNCH: $($_.Exception.Message)"
    exit 1
}

$ok = $false
for ($i = 0; $i -lt 10; $i++) {
    Start-Sleep -Seconds 1
    $chk = Get-NetTCPConnection -LocalPort 8090 -State Listen -ErrorAction SilentlyContinue
    if ($chk) { $ok = $true; break }
}
if ($ok) {
    Write-Log "VERIFIKASI_PORT_8090: OK, listener aktif."
    exit 0
} else {
    Write-Log "VERIFIKASI_PORT_8090: GAGAL - port 8090 tidak mendengarkan setelah 10 detik."
    exit 1
}