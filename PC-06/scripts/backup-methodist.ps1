# backup-methodist.ps1
# Backup Methodist-11 - SISTEM UPDATE LANGSUNG (bukan duplikat per tanggal)
#
# ATURAN KEAMANAN SOURCE (WAJIB):
#   - Source \\192.168.136.1\Methodist-11 Document adalah data utama, HANYA DIBACA.
#   - TIDAK ADA flag /MOV /MOVE /PURGE /MIR di script ini -> mustahil menghapus isi source.
#   - File yang terhapus/di-rename di source TETAP tersimpan di backup (tanpa purge).
#
# Pemakaian:
#   .\backup-methodist.ps1            -> BACKUP HARIAN: sinkron 1 folder tetap
#                                        E:\Back Up\Harian\Methodist-11 Document
#   .\backup-methodist.ps1 -Semester  -> BACKUP SEMESTER (manual): full copy seutuhnya ke
#                                        E:\Back Up\Semester\<Ganjil|Genap> <T.A>\

param([switch]$Semester)

$source     = "\\192.168.136.1\Methodist-11 Document"
$baseBackup = "E:\Back Up"
$months     = @{ 1="Januari"; 2="Februari"; 3="Maret"; 4="April"; 5="Mei"; 6="Juni"; 7="Juli"; 8="Agustus"; 9="September"; 10="Oktober"; 11="November"; 12="Desember" }
$today      = Get-Date

function Write-Log {
    param($LogPath, $Msg)
    "{0} | {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Msg | Tee-Object -FilePath $LogPath -Append
}

function Show-Stats {
    param($Dest, $LogPath, $StartedAt)
    $files = Get-ChildItem -LiteralPath $Dest -Recurse -File -ErrorAction SilentlyContinue
    $sizeGB = [math]::Round((($files | Measure-Object Length -Sum).Sum) / 1GB, 2)
    $mins = [math]::Round(((Get-Date) - $StartedAt).TotalMinutes, 1)
    Write-Log $LogPath ("Statistik: File {0} | Folder {1} | Total {2} GB | Durasi {3} menit" -f $files.Count, (Get-ChildItem -LiteralPath $Dest -Recurse -Directory -ErrorAction SilentlyContinue).Count, $sizeGB, $mins)
}

# ==== Cek akses ====
if (!(Test-Path -LiteralPath $source)) {
    Write-Host "ERROR: Source tidak dapat diakses: $source"
    exit 1
}
if (!(Test-Path -LiteralPath $baseBackup)) {
    Write-Host "ERROR: Drive backup tidak dapat diakses: $baseBackup"
    exit 1
}

$startTime = Get-Date

if ($Semester) {
    # ================= MODE SEMESTER (manual, full copy seutuhnya) =================
    $y = $today.Year; $m = $today.Month
    if ($m -ge 7) { $label = "Ganjil $y-$($y + 1)" } else { $label = "Genap $($y - 1)-$y" }

    $dest   = Join-Path $baseBackup "Semester\$label\Methodist-11 Document"
    $logDir = Join-Path $baseBackup "Semester\logs"
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    $logFile = Join-Path $logDir ("semester-{0}.txt" -f $today.ToString("yyyy-MM-dd-HHmmss"))

    if (Test-Path -LiteralPath $dest) {
        Write-Log $logFile "Folder semester '$label' sudah ada - SKIP (tidak menimpa backup lama)."
        exit 0
    }

    Write-Log $logFile "=== BACKUP SEMESTER '$label' - FULL COPY ==="
    Write-Log $logFile "Source: $source"
    Write-Log $logFile "Target: $dest"

    $rcLog = Join-Path $logDir ("robocopy-{0}.log" -f $today.ToString("yyyy-MM-dd-HHmmss"))
    & robocopy $source $dest /E /COPY:DAT /DCOPY:T /R:3 /W:5 /NP /NDL /NJH /NJS /LOG+:$rcLog /XF "*.tmp" "~`$*"
    $code = $LASTEXITCODE
    Write-Log $logFile "Robocopy selesai (exit: $code)"
    if ($code -ge 8) { Write-Log $logFile "WARNING: ada error robocopy - cek detail: $rcLog" }

    Show-Stats -Dest $dest -LogPath $logFile -StartedAt $startTime
    Write-Log $logFile "Log detail robocopy: $rcLog"
}
else {
    # ================= MODE HARIAN (default): 1 folder tetap, update langsung =================
    $dest   = Join-Path $baseBackup "Harian\Methodist-11 Document"
    $logDir = Join-Path $baseBackup "Harian\logs"
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    $logFile = Join-Path $logDir ("harian-{0}.txt" -f $today.ToString("yyyy-MM-dd"))

    Write-Log $logFile "=== BACKUP HARIAN - UPDATE LANGSUNG (copy saja, tanpa purge) ==="
    Write-Log $logFile "Source: $source"
    Write-Log $logFile "Target: $dest"

    # /E  : semua subfolder termasuk kosong
    # /XO : lewati file yang versinya di backup sudah lebih baru dari source
    # Tanpa /PURGE /MIR /MOV /MOVE -> tidak ada penghapusan di kedua sisi
    $rcLog = Join-Path $logDir ("robocopy-{0}.log" -f $today.ToString("yyyy-MM-dd-HHmmss"))
    & robocopy $source $dest /E /XO /COPY:DAT /DCOPY:T /R:3 /W:5 /NP /NDL /NJH /NJS /LOG+:$rcLog /XF "*.tmp" "~`$*"
    $code = $LASTEXITCODE
    Write-Log $logFile "Sinkron selesai (exit: $code)"
    if ($code -ge 8) { Write-Log $logFile "WARNING: ada error robocopy - cek detail: $rcLog" }

    Show-Stats -Dest $dest -LogPath $logFile -StartedAt $startTime
    Write-Log $logFile "Log detail robocopy: $rcLog"
}
