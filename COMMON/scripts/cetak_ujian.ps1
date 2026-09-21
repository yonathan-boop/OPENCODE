param(
    [string]$Folder = (Get-Location),
    [string]$Printer = "Brother HL-L2360D series",
    [string]$Settings = "fit,monochrome",
    [switch]$Recurse
)

$ErrorActionPreference = "Stop"
$output = New-Object System.Collections.Generic.List[string]
$fail = New-Object System.Collections.Generic.List[string]

$candidates = @(
    "$env:LOCALAPPDATA\SumatraPDF\SumatraPDF.exe",
    "$env:ProgramFiles\SumatraPDF\SumatraPDF.exe",
    "${env:ProgramFiles(x86)}\SumatraPDF\SumatraPDF.exe"
)
$sumatra = $null
foreach ($c in $candidates) {
    if (Test-Path -LiteralPath $c) { $sumatra = $c; break }
}
if (-not $sumatra) {
    $fromPath = (Get-Command SumatraPDF.exe -ErrorAction SilentlyContinue).Source
    if ($fromPath) { $sumatra = $fromPath }
}
if (-not $sumatra) {
    Write-Host "SumatraPDF belum terpasang. Install dulu:"
    Write-Host "  winget install -e --id SumatraPDF.SumatraPDF"
    exit 1
}

$printerExists = @(Get-Printer -ErrorAction SilentlyContinue | Where-Object { $_.Name -eq $Printer }).Count -gt 0
if (-not $printerExists) {
    Write-Host "Printer '$Printer' tidak ditemukan. Daftar printer tersedia:"
    Get-Printer | Select-Object -ExpandProperty Name
    exit 1
}

$filter = if ($Recurse) { "*.pdf" } else { "*.pdf" }
$pdfs = Get-ChildItem -LiteralPath $Folder -Filter $filter -Recurse:$Recurse | Sort-Object Name
if ($pdfs.Count -eq 0) {
    Write-Host "Tidak ada file PDF di '$Folder'."
    exit 1
}

Write-Host "Cetak $($pdfs.Count) file -> '$Printer' (settings: '$Settings')"
foreach ($pdf in $pdfs) {
    & $sumatra -print-to $Printer -print-settings $Settings -silent $pdf.FullName | Out-Null
    $code = $LASTEXITCODE
    if ($code -eq 0) {
        $output.Add($pdf.Name)
        Write-Host "[OK] $($pdf.Name)"
    } else {
        $fail.Add("$($pdf.Name) (exit $code)")
        Write-Host "[FAIL] $($pdf.Name) (exit $code)"
    }
}

Write-Host ""
Write-Host "==== Ringkasan ===="
Write-Host "Sukses  : $($output.Count) file"
Write-Host "Gagal   : $($fail.Count) file"
if ($fail.Count -gt 0) {
    Write-Host "File gagal:"
    $fail | ForEach-Object { Write-Host "  - $_" }
    Write-Host "Tips: exit 5 = cek kertas/offline/antrian printer; exit 4 = nama printer salah."
}