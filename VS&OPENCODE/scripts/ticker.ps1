param(
    [string]$LogDir = "C:\Users\Advan\Desktop\memory\VS&OPENCODE\.ticker"
)

$logFile = Join-Path $LogDir "ticker.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Add-Content -Path $logFile -Value $timestamp

$lines = Get-Content -Path $logFile
if ($lines.Count -gt 5000) {
    $lines | Select-Object -Last 5000 | Set-Content -Path $logFile
}
