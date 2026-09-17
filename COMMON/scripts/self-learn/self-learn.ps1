# self-learn.ps1 - Daemon belajar mandiri untuk PC (Windows)
# Jalan terus-menerus selama PC hidup, dengan guard RAM (budget ~1GB),
# single instance, dan auto commit/push ke repo memory.
#
# Cara pasang autostart (Task Scheduler, login user):
#   schtasks /Create /TN "opencode-self-learn" /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File \"<path>self-learn.ps1\"" /SC ONLOGON /RL LIMITED /F
#
# Kustomisasi via env:
#   SELFLEARN_INTERVAL_MIN  - menit tidur antar siklus (default 75)
#   SELFLEARN_RAM_GB        - budget RAM maks untuk opencode (default 3.0)
#   SELFLEARN_DIR           - lokasi repo memory (default: lewat param -Repo)
#   SELFLEARN_LOG           - path log (default: %TEMP%\opencode\self-learn.log)

[CmdletBinding()]
param(
    [string]$Repo = "C:\Users\yonat\OneDrive\Desktop\memory",
    [string]$PromptFile = ""
)

# ------- utilitas log -------
$script:LogPath = $env:SELFLEARN_LOG
if (-not $script:LogPath) { $script:LogPath = Join-Path $env:TEMP "opencode\self-learn.log" }
$logDir = Split-Path -Parent $script:LogPath
if ($logDir -and -not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

function Write-Log {
    param([string]$Msg)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Msg
    try { Add-Content -Path $script:LogPath -Value $line -Encoding UTF8 } catch {}
    Write-Host $line
}

# ------- single instance guard -------
$mutexName = "opencode-self-learn-$($env:USERNAME)"
$mutex = New-Object System.Threading.Mutex($false, $mutexName)
if (-not $mutex.WaitOne(0)) {
    Write-Log "Instance lain sudah berjalan. Keluar."
    exit 0
}

# ------- baca konfigurasi -------
$intervalMin = 75
if ($env:SELFLEARN_INTERVAL_MIN) { $intervalMin = [int]$env:SELFLEARN_INTERVAL_MIN }
$ramBudgetGB = 3.0
if ($env:SELFLEARN_RAM_GB) { $ramBudgetGB = [double]$env:SELFLEARN_RAM_GB }

if (-not $PromptFile) { $PromptFile = Join-Path $Repo "COMMON\scripts\self-learn\self-learn-prompt.md" }
if (-not (Test-Path $PromptFile)) {
    Write-Log "EROR: Prompt file tidak ditemukan: $PromptFile"
    exit 1
}

Write-Log "= self-learn dimulai. Repo=$Repo interval=${intervalMin}m budgetRAM=${ramBudgetGB}GB"

function Get-FreeRAMGB {
    try {
        $os = Get-CimInstance Win32_OperatingSystem
        return [math]::Round(($os.FreePhysicalMemory / 1MB), 2)
    } catch { return 99 }
}

# ------- jalankan SATU siklus opencode (blokir synchronously) -------
function Run-One-Cycle {
    param([string]$FreeBefore)
    Write-Log "Siklus baru dimulai. FreeRAM sebelum=$FreeBefore GB"
    $git = Get-Command git -ErrorAction SilentlyContinue
    if (-not $git) { Write-Log "EROR: git tidak ditemukan."; return }

    # 1) pull memory dulu (supaya tidak konflik dengan server)
    Write-Log "git pull (memory)..."
    Push-Location $Repo
    git pull --no-edit 2>&1 | ForEach-Object { Write-Log "  pull> $_" }
    Pop-Location

    # 2) siapkan command
    $prompt = Get-Content -Path $PromptFile -Raw -Encoding UTF8
    $argsRun = @("run", "--dir", $Repo, "--auto", $prompt)

    # jalankan opencode dalam proses terpisah + pantau RAM
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = (Get-Command opencode -ErrorAction SilentlyContinue).Source
    if (-not $psi.FileName) { $psi.FileName = "opencode" }
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.CreateNoWindow = $true
    $psi.WorkingDirectory = $Repo

    # quote argumen untuk ProcessStartInfo.Arguments (aturan Windows command line):
    # - bungkus tiap argumen dengan tanda kutip ganda
    # - flatten newline (multiline prompt tetap satu argumen valid)
    # - escape kutip ganda di dalam nilai dengan backslash
    $argStr = ($argsRun | ForEach-Object {
        $v = ($_ -replace "[\r\n]+", " ")
        '"{0}"' -f ($v -replace '"', '\"')
    }) -join " "
    $psi.Arguments = $argStr

    $proc = New-Object System.Diagnostics.Process
    $proc.StartInfo = $psi
    $proc.OutputDataReceived = {
        param($s, $e)
        if ($e.Data) { Write-Log "  > $($e.Data)" }
    }
    $proc.ErrorDataReceived = {
        param($s, $e)
        if ($e.Data) { Write-Log "  ERR> $($e.Data)" }
    }

    try {
        $proc.Start() | Out-Null
        $proc.BeginOutputReadLine()
        $proc.BeginErrorReadLine()
    } catch {
        Write-Log "EROR: gagal start opencode: $_"
        return
    }

    # pantau proses: batasi RAM budget & jangan biarkan lelet karena RAM
    $startTick = Get-Date
    $ramWarned = $false
    $killForRAM = $false
    while (-not $proc.HasExited) {
        Start-Sleep -Seconds 3
        $freeNow = Get-FreeRAMGB
        $proc.Refresh()
        $procGB = [math]::Round($proc.WorkingSet64 / 1GB, 2)

        # Aturan budget RAM: kalau free RAM sedang "kosong banyak" (>=2x budget) boleh melewati budget sesaat,
        # jika tidak dan proc > budget -> warning dulu, kalau masih tinggi 30 detik berikutnya -> terminate.
        if ($procGB -gt $ramBudgetGB) {
            if ($freeNow -lt ($ramBudgetGB * 2)) {
                if (-not $ramWarned) {
                    Write-Log "  WARN: opencode pakai ${procGB}GB > budget ${ramBudgetGB}GB dan RAM sedang dipakai (free=${freeNow}GB)."
                    $ramWarned = $true
                }
                if ($ramWarned -and ((Get-Date) - $startTick).TotalSeconds -gt 30) {
                    Write-Log "  KILL: opencode tetap di atas budget setelah 30s. Terminate."
                    $killForRAM = $true
                    break
                }
            } else {
                if ($ramWarned) { Write-Log "  OK: free RAM ${freeNow}GB cukup, biarkan lewat budget sesaat."; $ramWarned = $false; $startTick = Get-Date }
            }
        } else {
            $ramWarned = $false
            $startTick = Get-Date
        }
    }

    if ($killForRAM) {
        try { $proc.Kill() | Out-Null; $proc.WaitForExit() } catch {}
        Write-Log "opencode di-terminate karena RAM melebihi budget."
    } else {
        $proc.WaitForExit()
        Write-Log "opencode selesai. Exit code: $($proc.ExitCode)"
    }

    # 3) commit + push hasil belajar (kalau ada perubahan)
    Push-Location $Repo
    $status = git status --porcelain 2>&1
    if ($status) {
        Write-Log "Ada perubahan: commit + push..."
        git add -A 2>&1 | ForEach-Object { Write-Log "  add> $_" }
        git commit -m "self-learn (PC): belajar mandiri $(Get-Date -Format 'yyyy-MM-dd HH:mm')" 2>&1 | ForEach-Object { Write-Log "  commit> $_" }
        # pull dengan rebase supaya tidak konflik dengan server yang juga push
        git pull --rebase --autostash 2>&1 | ForEach-Object { Write-Log "  pull-rebase> $_" }
        git push 2>&1 | ForEach-Object { Write-Log "  push> $_" }
    } else {
        Write-Log "Tidak ada perubahan, skip commit."
    }
    Pop-Location
}

# ------- loop utama -------
$cycle = 0
while ($true) {
    $cycle++
    $freeNow = Get-FreeRAMGB
    # syarat jalan: free RAM harus minimal budget + 1.5GB (biar PC tidak lelet)
    if ($freeNow -lt ($ramBudgetGB + 1.5)) {
        Write-Log "Free RAM ${freeNow}GB terlalu rendah untuk belajar (< $($ramBudgetGB + 1.5)GB). Skip siklus $cycle, tunggu ${intervalMin} menit."
        Start-Sleep -Seconds ($intervalMin * 60)
        continue
    }

    Write-Log "--- Siklus #$cycle ---"
    Run-One-Cycle -FreeBefore $freeNow

    # tidur antar siklus (sleep dalam blok kecil agar mudah di-stop)
    $sleepSec = $intervalMin * 60
    Write-Log "Tidur ${intervalMin} menit sebelum siklus berikutnya..."
    $slept = 0
    while ($slept -lt $sleepSec) {
        Start-Sleep -Seconds 30
        $slept += 30
    }
}

# (tidak akan sampai sini; mutex dibiarkan sampai proses mati)
$mutex.ReleaseMutex()