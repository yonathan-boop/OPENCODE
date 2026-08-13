$disabled = [byte[]](3,0,0,0,0,0,0,0,0,0,0,0)
$enabled = [byte[]](2,0,0,0,0,0,0,0,0,0,0,0)
$run = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
$startupFolder = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder"

$blockedStartup = @(
    "OneDrive",
    "EPLTarget\P0000000000000000",
    "EPLTarget\P0000000000000001",
    "Adobe Acrobat Synchronizer",
    "GoogleChromeAutoLaunch_9D4A046E5DB6BEDFFABE8E5C45AF14F3",
    "MicrosoftEdgeAutoLaunch_0ECE03778CAA0CACE4400C381DF1EA4D",
    "EPPCCMON"
)

foreach ($item in $blockedStartup) {
    New-ItemProperty -Path $run -Name $item -PropertyType Binary -Value $disabled -Force -ErrorAction SilentlyContinue
}
New-ItemProperty -Path $run -Name "ZeroTierUI" -PropertyType Binary -Value $enabled -Force -ErrorAction SilentlyContinue
New-ItemProperty -Path $startupFolder -Name "L.bat" -PropertyType Binary -Value $enabled -Force -ErrorAction SilentlyContinue

$blockedServices = @("chromoting", "isaHelperSvc", "MyEpson Portal Service")
Get-Service -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "GoogleUpdater*" } | ForEach-Object { $blockedServices += $_.Name }
foreach ($service in $blockedServices) {
    Set-Service -Name $service -StartupType Disabled -ErrorAction SilentlyContinue
    Stop-Service -Name $service -Force -ErrorAction SilentlyContinue
}

Set-Service -Name "VeyonService" -StartupType Manual -ErrorAction SilentlyContinue
Stop-Service -Name "VeyonService" -Force -ErrorAction SilentlyContinue

New-Item -Path "HKLM:\Software\Policies\Google\Chrome" -Force | Out-Null
Set-ItemProperty -Path "HKLM:\Software\Policies\Google\Chrome" -Name "BackgroundModeEnabled" -Value 0 -Type DWord -Force
New-Item -Path "HKLM:\Software\Policies\Microsoft\Edge" -Force | Out-Null
Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Edge" -Name "StartupBoostEnabled" -Value 0 -Type DWord -Force
Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Edge" -Name "BackgroundModeEnabled" -Value 0 -Type DWord -Force

Get-Process -Name "msedge" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Get-Process -Name "msedgewebview2" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Get-Process -Name "SearchHost" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Get-Process -Name "SnippingTool" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Get-Process -Name "TiWorker" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Get-Process -Name "WidgetService" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue

New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Dsh" -Force | Out-Null
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Dsh" -Name "AllowNewsAndInterests" -Value 0 -Type DWord -Force

$extraOff = @("wuauserv", "WSearch")
foreach ($svc in $extraOff) {
    Set-Service -Name $svc -StartupType Disabled -ErrorAction SilentlyContinue
    Stop-Service -Name $svc -Force -ErrorAction SilentlyContinue
}
