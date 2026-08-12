$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path

$files = Get-ChildItem -Path $Root -Recurse -Filter *.html
if (-not $files) { Write-Output "Tidak ada file HTML di $Root"; exit 1 }

$pattern = 'Versi\s+\d+\.\d{4}'
$current = $null
foreach ($f in $files) {
  $m = [regex]::Match((Get-Content -Path $f.FullName -Raw -Encoding UTF8), $pattern)
  if ($m.Success) { $current = $m.Value; break }
}
if (-not $current) { Write-Output "Versi tidak ditemukan di file HTML mana pun."; exit 1 }

$num = [regex]::Match($current, '(\d+)\.(\d{4})')
$major = [int]$num.Groups[1].Value
$minor = [int]$num.Groups[2].Value + 1
if ($minor -ge 10000) { $minor = 0; $major = $major + 1 }
$newVer = "Versi $major.$($minor.ToString('D4'))"

$done = 0
foreach ($f in $files) {
  $content = Get-Content -Path $f.FullName -Raw -Encoding UTF8
  if ($null -eq $content) { continue }
  if ($content.Contains($current)) {
    $content = $content.Replace($current, $newVer)
    Set-Content -Path $f.FullName -Value $content -Encoding UTF8 -NoNewline
    $done++
  }
}
Write-Output "$current -> $newVer (di $done dari $($files.Count) file HTML)"
