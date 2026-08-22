# backup-methodist.ps1
# Incremental backup \\192.168.136.1\Methodist-11 Document -> E:\Back Up\
# Strategi: copy backup terakhir (lokal, cepat) → lalu robocopy source → new (hanya file lebih baru)

$source = "\\192.168.136.1\Methodist-11 Document"
$baseBackup = "E:\Back Up"

$months = @{
    1="Januari"; 2="Februari"; 3="Maret"; 4="April"
    5="Mei"; 6="Juni"; 7="Juli"; 8="Agustus"
    9="September"; 10="Oktober"; 11="November"; 12="Desember"
}

$today = Get-Date
$day = $today.Day
$month = $months[$today.Month]
$year = $today.Year
$dateIndonesian = "$day $month $year"

$logDir = $baseBackup
if (!(Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
$logFile = "$logDir\backup-log-$($today.ToString('yyyy-MM-dd-HHmmss')).txt"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$ts | $msg" | Tee-Object -FilePath $logFile -Append
}

# Cek akses
if (!(Test-Path $source)) {
    Log "ERROR: Source tidak dapat diakses: $source"
    exit 1
}
if (!(Test-Path $baseBackup)) {
    Log "ERROR: Drive backup tidak dapat diakses: $baseBackup"
    exit 1
}

# Cari folder backup terakhir
$lastBackup = Get-ChildItem -Path $baseBackup -Directory |
    Where-Object { $_.Name -match "^Copy\s" -or $_.Name -match "^Copy of\s" } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

$destFolder = "$baseBackup\Copy $dateIndonesian"

# Skip kalau folder hari ini sudah ada
if (Test-Path $destFolder) {
    Log "Folder backup hari ini sudah ada: $destFolder — skip."
    exit 0
}

$startTime = Get-Date

if ($lastBackup) {
    Log "=== INCREMENTAL BACKUP ==="
    Log "Source: $source"
    Log "Last backup: $($lastBackup.Name)"
    Log "Target: $destFolder"
    
    # STEP 1: Copy backup terakhir ke folder baru (lokal, cepat — tidak lewat network)
    Log "Step 1: Copy backup terakhir ke folder baru (lokal)..."
    New-Item -ItemType Directory -Path $destFolder -Force | Out-Null
    
    $robocopyLocal = & robocopy $lastBackup.FullName $destFolder /E /DCOPY:T /COPY:DAT /R:1 /W:1 /NP /NDL /NJH /NJS /XF "*.tmp" "~`$*"
    $localExit = $LASTEXITCODE
    Log "Step 1 selesai (exit: $localExit)"
    
    # STEP 2: Robocopy source → dest dengan /XO (hanya file lebih baru dari source)
    Log "Step 2: Update dari source (hanya file baru/updated)..."
    $robocopyLog = "$logDir\robocopy-$($today.ToString('yyyy-MM-dd-HHmmss')).log"
    
    & robocopy $source $destFolder /E /XO /DCOPY:T /COPY:DAT /R:3 /W:5 /NP /NDL /NJH /NJS /LOG+:$robocopyLog /XF "*.tmp" "~`$*"
    $netExit = $LASTEXITCODE
    Log "Step 2 selesai (exit: $netExit)"
    
    if ($netExit -ge 8) {
        Log "WARNING: Ada error di robocopy. Cek: $robocopyLog"
    }
    
} else {
    Log "=== FULL BACKUP (pertama kali) ==="
    Log "Source: $source"
    Log "Target: $destFolder"
    
    $robocopyLog = "$logDir\robocopy-$($today.ToString('yyyy-MM-dd-HHmmss')).log"
    & robocopy $source $destFolder /E /DCOPY:T /COPY:DAT /R:3 /W:5 /NP /NDL /NJH /NJS /LOG+:$robocopyLog /XF "*.tmp" "~`$*"
    $exitCode = $LASTEXITCODE
    Log "Full backup selesai (exit: $exitCode)"
}

$elapsed = (Get-Date) - $startTime
$elapsedMin = [math]::Round($elapsed.TotalMinutes, 1)

# Statistik
if (Test-Path $destFolder) {
    $fileCount = (Get-ChildItem -Path $destFolder -Recurse -File -ErrorAction SilentlyContinue).Count
    $folderCount = (Get-ChildItem -Path $destFolder -Recurse -Directory -ErrorAction SilentlyContinue).Count
    $totalSize = (Get-ChildItem -Path $destFolder -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum
    $sizeGB = [math]::Round($totalSize / 1GB, 2)
    
    Log "=== SELESAI ==="
    Log "Folder: $destFolder"
    Log "File: $fileCount | Folder: $folderCount | Size: $sizeGB GB"
    Log "Waktu: $elapsedMin menit"
} else {
    Log "WARNING: Folder backup tidak terbentuk"
}

Log "Log: $logFile"
