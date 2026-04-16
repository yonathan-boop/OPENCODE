# Auto Save Memory + Push
# Usage: save-memory.ps1 "isi pesan"

param(
    [Parameter(ValueFromRemainingArguments=$true)][string]$Content
)

if (-not $Content) {
    Write-Host "Usage: save-memory.ps1 ""isi pesan""" -ForegroundColor Yellow
    exit 1
}

$MemoryDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PCName = $env:COMPUTERNAME

$PCMap = @{
    "DESKTOP-1E1LBB7" = "PC-Advan"
    "ADVAN" = "PC-Advan"
    "PC-06" = "PC-06"
    "WORK-PC" = "PC-06"
}

$PCFolder = $PCMap[$PCName]
if (-not $PCFolder) { $PCFolder = "PC-Advan" }

$Today = Get-Date -Format "yyyy-MM-dd"
$FilePath = "$MemoryDir\$PCFolder\$Today.md"
$Timestamp = Get-Date -Format "HH:mm"

# Create folder if needed
if (-not (Test-Path "$MemoryDir\$PCFolder")) {
    New-Item -ItemType Directory -Path "$MemoryDir\$PCFolder" -Force | Out-Null
}

# Save
"$Timestamp | $Content" | Out-File -FilePath $FilePath -Append -Encoding utf8
Write-Host "Saved to: $PCFolder/$Today.md" -ForegroundColor Green

# Also update MASTER-MEMORY
"$Timestamp [$PCFolder] $Content" | Out-File -FilePath "$MemoryDir\MASTER-MEMORY.md" -Append -Encoding utf8

# Auto-push
& "$MemoryDir\push-memory.ps1"