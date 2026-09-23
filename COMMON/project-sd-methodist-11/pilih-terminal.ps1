$PREFIX   = 'web-'
$MAXNEW   = 2
$tmuxExe  = 'C:\Users\WILIANTO\AppData\Local\Microsoft\WinGet\Packages\arndawg.tmux-windows_Microsoft.Winget.Source_8wekyb3d8bbwe\tmux.exe'

function Get-Sessions {
    $list = & $tmuxExe ls -F '#{session_name}' 2>$null
    @($list) | Where-Object { $_ -like "$PREFIX*" }
}

function Get-WinCount($name) {
    $n = & $tmuxExe display-message -p '#{session_windows}' -t $name 2>$null
    if (-not $n) { return 1 }
    return [int]$n.Trim()
}

function Show-Menu($sessions) {
    cls
    Write-Host '============================================' -ForegroundColor Cyan
    Write-Host '  TERMINAL ONLINE SD METHODIST-11' -ForegroundColor Cyan
    Write-Host '============================================' -ForegroundColor Cyan
    if ($sessions.Count -eq 0) {
        Write-Host ''
        Write-Host '  Belum ada sesi aktif.' -ForegroundColor Yellow
    } else {
        Write-Host ''
        Write-Host '  Sesi lama (pilih nomor untuk LANJUT):' -ForegroundColor Green
        for ($i = 0; $i -lt $sessions.Count; $i++) {
            $w = Get-WinCount $sessions[$i]
            Write-Host ("  {0}. {1}  ({2} window)" -f ($i + 1), $sessions[$i], $w)
        }
    }
    Write-Host ''
    Write-Host '  b. Buka terminal BARU' -ForegroundColor Green
    Write-Host '  0. Keluar' -ForegroundColor Gray
}

function New-Session {
    param([string]$name)
    & $tmuxExe new-session -d -s $name -x 200 -y 50 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) { return $true }
    return $false
}

while ($true) {
    $sessions = Get-Sessions
    Show-Menu $sessions
    $choice = Read-Host ''
    switch ($choice.Trim().ToLower()) {
        '0' { Write-Host 'Sampai jumpa!' -ForegroundColor Gray; exit 0 }
        'b' {
            if ($sessions.Count -ge $MAXNEW) {
                Write-Host "  Max $MAXNEW sesi tercapai ($($sessions.Count) aktif)." -ForegroundColor Red
                Read-Host 'Tekan enter untuk lanjut'
                continue
            }
            $name = "$PREFIX" + ([DateTimeOffset]::Now.ToUnixTimeSeconds())
            if (New-Session $name) {
                & $tmuxExe attach-session -t $name
            } else {
                Write-Host '  Gagal membuat sesi baru.' -ForegroundColor Red
                Read-Host 'Tekan enter untuk lanjut'
            }
        }
        default {
            $n = 0
            if ([int]::TryParse($choice.Trim(), [ref]$n) -and $n -ge 1 -and $n -le $sessions.Count) {
                & $tmuxExe attach-session -t $sessions[$n - 1]
            } else {
                Write-Host '  Pilihan tidak valid.' -ForegroundColor Red
                Read-Host 'Tekan enter untuk lanjut'
            }
        }
    }
}