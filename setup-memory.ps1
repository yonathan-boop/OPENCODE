# Auto Setup Memory System
# Usage: setup-memory.ps1 "GitHub-URL" "Token"

param(
    [Parameter(Position=0)][string]$GitHubURL = "",
    [Parameter(Position=1)][string]$Token = ""
)

# If no args provided, prompt for input
if (-not $GitHubURL) {
    Write-Host "=== Auto Setup Memory System ===" -ForegroundColor Cyan
    $GitHubURL = Read-Host "GitHub Repo URL (contoh: https://github.com/yonathan-boop/OPENCODE)"
}
if (-not $Token) {
    $Token = Read-Host "GitHub Token" -AsSecureString
    $Token = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Token))
}

# Set environment
$env:GITHUB_TOKEN = $Token
$MemoryDir = $env:USERPROFILE + "\Desktop\memory"

# Create folder if not exists
if (-not (Test-Path $MemoryDir)) {
    New-Item -ItemType Directory -Path $MemoryDir -Force | Out-Null
}

# Clone or pull repo
Set-Location $MemoryDir
if (Test-Path ".git") {
    Write-Host "Updating existing repo..." -ForegroundColor Yellow
    git remote set-url origin "https://yonathan-boop:$Token@$($GitHubURL -replace 'https://', '')"
    git pull origin main --allow-unrelated-histories
} else {
    Write-Host "Cloning repo..." -ForegroundColor Yellow
    git clone "https://yonathan-boop:$Token@$($GitHubURL -replace 'https://', '')" .
}

# Detect current PC
$PCName = $env:COMPUTERNAME
Write-Host "`nDetected PC: $PCName" -ForegroundColor Cyan
Write-Host "Memory folder: $MemoryDir" -ForegroundColor Green

# Create PC folder if not exists
$PCMap = @{
    "DESKTOP-1E1LBB7" = "PC-Advan"
    "ADVAN" = "PC-Advan"
    "PC-06" = "PC-06"
    "WORK-PC" = "PC-06"
}
$PCFolder = $PCMap[$PCName]
if (-not $PCFolder) {
    $PCFolder = "PC-Advan"
    Write-Host "Unknown PC - using default: $PCFolder" -ForegroundColor Yellow
}

if (-not (Test-Path $PCFolder)) {
    New-Item -ItemType Directory -Path $PCFolder -Force | Out-Null
}
if (-not (Test-Path "Common")) {
    New-Item -ItemType Directory -Path "Common" -Force | Out-Null
}

Write-Host "`n=== Setup Selesai! ===" -ForegroundColor Green
Write-Host "PC: $PCName -> Folder: $PCFolder" -ForegroundColor Cyan
Write-Host "Token tersimpan di environment (valid untuk session ini)" -ForegroundColor Yellow

# Quick test - save something
$TestEntry = "Test setup dari $PCName - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
$TestFile = "$MemoryDir\$PCFolder\setup-test.md"
"$TestEntry" | Out-File -FilePath $TestFile -Encoding utf8
Write-Host "Test file created: $TestFile" -ForegroundColor Green

# Show folder structure
Write-Host "`nFolder structure:"
Get-ChildItem -Path $MemoryDir -Directory | ForEach-Object { Write-Host "  - $($_.Name)/" }
Write-Host "  - $($PCFolder)/ (current)" -ForegroundColor Cyan