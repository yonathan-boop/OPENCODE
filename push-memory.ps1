# Memory Auto-Push Script with PC Detection
# Set token via: $env:GITHUB_TOKEN = "your-token"

$Token = $env:GITHUB_TOKEN
if (-not $Token) {
    Write-Host "Error: Set `$env:GITHUB_TOKEN first" -ForegroundColor Red
    exit 1
}

$MemoryDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RemoteUrl = "https://yonathan-boop:$Token@github.com/yonathan-boop/OPENCODE.git"

# Detect PC
$PCName = $env:COMPUTERNAME
$PCMap = @{
    "DESKTOP-1E1LBB7" = "PC-Advan"
    "ADVAN" = "PC-Advan"
    "PC-06" = "PC-06"
    "WORK-PC" = "PC-06"
}
$CurrentPC = $PCMap[$PCName]
if (-not $CurrentPC) { $CurrentPC = "PC-Advan" }

Write-Host "PC: $PCName -> Folder: $CurrentPC" -ForegroundColor Cyan

Set-Location $MemoryDir
git remote set-url origin $RemoteUrl
git pull origin main --allow-unrelated-histories 2>$null

$HasChanges = $false

# Common folder
if (Test-Path "Common") {
    Set-Location "Common"
    git add . 2>$null
    if (git status --porcelain) {
        git commit -m "Shared update - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        $HasChanges = $true
    }
    Set-Location $MemoryDir
}

# Current PC folder
if (Test-Path $CurrentPC) {
    Set-Location $CurrentPC
    git add . 2>$null
    if (git status --porcelain) {
        git commit -m "Update from $PCName - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        $HasChanges = $true
    }
    Set-Location $MemoryDir
}

if ($HasChanges) {
    git push origin main
    Write-Host "Pushed!" -ForegroundColor Green
} else {
    Write-Host "No changes" -ForegroundColor Yellow
}