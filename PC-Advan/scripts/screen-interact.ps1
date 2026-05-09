# screen-interact.ps1 — Screen Interaction Tool
# Bisa cari teks di layar lalu klik
#
# Usage:
#   .\screen-interact.ps1 -ClickText "Rekomendasi"     # cari teks, klik tengahnya
#   .\screen-interact.ps1 -ClickText "Search" -Double   # double click
#   .\screen-interact.ps1 -ClickText "Gadgetin" -Right  # right click
#   .\screen-interact.ps1 -List                         # list semua teks + koordinat + index
#   .\screen-interact.ps1 -Index 3                      # klik index ke-3 dari list
#   .\screen-interact.ps1 -Type "Rekomendasi iPhone"    # type text (kirim keystrokes)

param(
    [string]$ClickText,
    [switch]$Double,
    [switch]$Right,
    [switch]$List,
    [int]$Index = -1,
    [string]$Type
)

$ErrorActionPreference = "Stop"
$TesseractPath = "C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------- P/Invoke: Window + Mouse ----------
function Initialize-Win32 {
    try {
        $source = @"
using System;
using System.Runtime.InteropServices;
public class Win32 {
    [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr hWnd, System.Text.StringBuilder text, int count);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);
    [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint processId);
}
public struct RECT { public int left; public int top; public int right; public int bottom; }
public class Mouse {
    [DllImport("user32.dll")] public static extern void mouse_event(uint dwFlags, uint dx, uint dy, uint dwData, UIntPtr dwExtraInfo);
    [DllImport("user32.dll")] public static extern bool SetCursorPos(int X, int Y);
}
"@
        Add-Type -TypeDefinition $source -ReferencedAssemblies "System.Runtime.InteropServices" -ErrorAction Stop
    } catch { }
}

Initialize-Win32

function Get-ActiveWindowHandle {
    return [Win32]::GetForegroundWindow()
}

function Get-WindowRect {
    param([IntPtr]$hwnd)
    $rect = New-Object RECT
    [Win32]::GetWindowRect($hwnd, [ref]$rect) | Out-Null
    return $rect
}

function Get-WindowProcessId {
    param([IntPtr]$hwnd)
    $procId = 0
    [Win32]::GetWindowThreadProcessId($hwnd, [ref]$procId) | Out-Null
    return $procId
}

# ---------- Screenshot ----------
function Take-ScreenshotActiveWindow {
    try {
        Add-Type -AssemblyName System.Windows.Forms
        Add-Type -AssemblyName System.Drawing

        $hwnd = Get-ActiveWindowHandle
        $rect = Get-WindowRect -hwnd $hwnd
        $bounds = New-Object System.Drawing.Rectangle($rect.left, $rect.top, ($rect.right - $rect.left), ($rect.bottom - $rect.top))

        $bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
        $gfx = [System.Drawing.Graphics]::FromImage($bmp)
        $gfx.CopyFromScreen($bounds.X, $bounds.Y, 0, 0, $bounds.Size)
        $gfx.Dispose()

        $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
        $path = [System.IO.Path]::Combine($env:TEMP, "opencode-screeninteract-$timestamp.png")
        $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()

        return @{ Path = $path; WindowLeft = $rect.left; WindowTop = $rect.top }
    } catch {
        return $null
    }
}

# ---------- OCR + TSV Parsing ----------
function Invoke-OCRWithCoordinates {
    param([string]$ImagePath)
    try {
        if (-not (Test-Path -LiteralPath $TesseractPath)) { return @() }
        if (-not (Test-Path -LiteralPath $ImagePath)) { return @() }

        $tsvOutput = & $TesseractPath "$ImagePath" stdout -l eng+ind --psm 6 tsv 2>$null
        if (-not $tsvOutput) { return @() }

        $lines = $tsvOutput -split "`n" | Where-Object { $_ -ne "" }
        if ($lines.Count -lt 2) { return @() }

        $header = $lines[0] -split "`t"
        $colIdx = @{}
        for ($i = 0; $i -lt $header.Count; $i++) { $colIdx[$header[$i].Trim()] = $i }

        $words = @()
        for ($i = 1; $i -lt $lines.Count; $i++) {
            $cols = $lines[$i] -split "`t"
            if ($cols.Count -le $colIdx["text"]) { continue }
            if ([int]$cols[$colIdx["level"]] -ne 6) { continue }
            $conf = [double]$cols[$colIdx["conf"]]
            $text = $cols[$colIdx["text"]]
            if ($conf -le 0 -or [string]::IsNullOrWhiteSpace($text)) { continue }
            $words += @{
                block  = [int]$cols[$colIdx["block_num"]]
                par    = [int]$cols[$colIdx["par_num"]]
                line   = [int]$cols[$colIdx["line_num"]]
                left   = [int]$cols[$colIdx["left"]]
                top    = [int]$cols[$colIdx["top"]]
                width  = [int]$cols[$colIdx["width"]]
                height = [int]$cols[$colIdx["height"]]
                text   = $text.Trim()
                conf   = $conf
            }
        }
        if ($words.Count -eq 0) { return @() }
        return Merge-TSVElements -Words $words
    } catch { return @() }
}

function Merge-TSVElements {
    param([array]$Words)
    $elements = @()
    $groups = $Words | Group-Object { "$($_.block).$($_.par).$($_.line)" }

    foreach ($group in $groups) {
        $sorted = $group.Group | Sort-Object left
        $currentGroup = @($sorted[0])

        for ($i = 1; $i -lt $sorted.Count; $i++) {
            $prev = $currentGroup[-1]
            $curr = $sorted[$i]
            $gap = $curr.left - ($prev.left + $prev.width)
            if ($gap -le 5) {
                $currentGroup += $curr
            } else {
                $elements += New-MergedElement -Words $currentGroup
                $currentGroup = @($curr)
            }
        }
        if ($currentGroup.Count -gt 0) {
            $elements += New-MergedElement -Words $currentGroup
        }
    }
    return $elements
}

function New-MergedElement {
    param([array]$Words)
    $minLeft = ($Words | Measure-Object left -Minimum).Minimum
    $minTop = ($Words | Measure-Object top -Minimum).Minimum
    $maxRight = ($Words | ForEach-Object { $_.left + $_.width } | Measure-Object -Maximum).Maximum
    $maxBottom = ($Words | ForEach-Object { $_.top + $_.height } | Measure-Object -Maximum).Maximum
    $fullText = ($Words | ForEach-Object { $_.text }) -join " "
    return @{
        Text   = $fullText
        X      = $minLeft
        Y      = $minTop
        Width  = $maxRight - $minLeft
        Height = $maxBottom - $minTop
    }
}

# ---------- ScanScreen ----------
function ScanScreen {
    try {
        $ss = Take-ScreenshotActiveWindow
        if (-not $ss) {
            Write-Error "Screenshot gagal"
            return @()
        }

        $elements = Invoke-OCRWithCoordinates -ImagePath $ss.Path

        # Convert to absolute screen coordinates + add CenterX/CenterY
        $result = @()
        for ($i = 0; $i -lt $elements.Count; $i++) {
            $el = $elements[$i]
            $absX = $ss.WindowLeft + $el.X
            $absY = $ss.WindowTop + $el.Y
            $result += @{
                Index   = $i
                Text    = $el.Text
                X       = $absX
                Y       = $absY
                Width   = $el.Width
                Height  = $el.Height
                CenterX = $absX + $el.Width / 2
                CenterY = $absY + $el.Height / 2
            }
        }

        # Cleanup
        if (Test-Path -LiteralPath $ss.Path) {
            Remove-Item -LiteralPath $ss.Path -Force -ErrorAction SilentlyContinue
        }

        return $result
    } catch {
        Write-Error "ScanScreen error: $_"
        return @()
    }
}

# ---------- FindText ----------
function FindText {
    param([string]$Text, [array]$Elements)
    $lower = $Text.ToLower()
    foreach ($el in $Elements) {
        if ($el.Text.ToLower() -like "*$lower*") {
            return $el
        }
    }
    return $null
}

# ---------- ClickAt ----------
function ClickAt {
    param([int]$X, [int]$Y, [string]$ClickType = "left")
    try {
        [Mouse]::SetCursorPos($X, $Y)
        Start-Sleep -Milliseconds 100

        switch ($ClickType) {
            "left" {
                [Mouse]::mouse_event(0x02, 0, 0, 0, [UIntPtr]::Zero)
                Start-Sleep -Milliseconds 50
                [Mouse]::mouse_event(0x04, 0, 0, 0, [UIntPtr]::Zero)
            }
            "double" {
                [Mouse]::mouse_event(0x02, 0, 0, 0, [UIntPtr]::Zero)
                Start-Sleep -Milliseconds 50
                [Mouse]::mouse_event(0x04, 0, 0, 0, [UIntPtr]::Zero)
                Start-Sleep -Milliseconds 100
                [Mouse]::mouse_event(0x02, 0, 0, 0, [UIntPtr]::Zero)
                Start-Sleep -Milliseconds 50
                [Mouse]::mouse_event(0x04, 0, 0, 0, [UIntPtr]::Zero)
            }
            "right" {
                [Mouse]::mouse_event(0x08, 0, 0, 0, [UIntPtr]::Zero)
                Start-Sleep -Milliseconds 50
                [Mouse]::mouse_event(0x10, 0, 0, 0, [UIntPtr]::Zero)
            }
        }
    } catch {
        Write-Error "Click error: $_"
    }
}

# ---------- SendKeys ----------
function SendKeys {
    param([string]$Text)
    try {
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.SendKeys]::SendWait($Text)
    } catch {
        Write-Error "SendKeys error: $_"
    }
}

# ========== MAIN ==========
try {
    if ($List) {
        Write-Host "`nScanning screen...`n" -ForegroundColor Cyan
        $elements = ScanScreen
        if ($elements.Count -eq 0) {
            Write-Host "Tidak ada teks terdeteksi di layar." -ForegroundColor Yellow
            exit 0
        }
        Write-Host ("{0,-6} {1,-40} {2,-25}" -f "INDEX", "TEXT", "COORDINATES") -ForegroundColor Green
        Write-Host ("{0,-6} {1,-40} {2,-25}" -f "-----", "----", "-----------") -ForegroundColor Green
        foreach ($el in $elements) {
            $coord = "($($el.X), $($el.Y), $($el.Width), $($el.Height))"
            $text = if ($el.Text.Length -gt 38) { $el.Text.Substring(0, 35) + "..." } else { $el.Text }
            Write-Host ("{0,-6} {1,-40} {2,-25}" -f $el.Index, ("`"" + $text + "`""), $coord)
        }
        Write-Host "`nTotal: $($elements.Count) elements found`n" -ForegroundColor Cyan
    }
    elseif ($ClickText) {
        Write-Host "Scanning screen for '$ClickText'..." -ForegroundColor Cyan
        $elements = ScanScreen
        $found = FindText -Text $ClickText -Elements $elements
        if ($found) {
            $clickType = "left"
            if ($Right) { $clickType = "right" }
            elseif ($Double) { $clickType = "double" }
            Write-Host "Found: '$($found.Text)' → ($($found.CenterX), $($found.CenterY))" -ForegroundColor Green
            ClickAt -X $found.CenterX -Y $found.CenterY -ClickType $clickType
            Write-Host "Clicked." -ForegroundColor Green
        } else {
            Write-Host "Teks '$ClickText' tidak ditemukan di layar." -ForegroundColor Red
            if ($elements.Count -gt 0) {
                Write-Host "`nTeks yang tersedia di layar:" -ForegroundColor Yellow
                foreach ($el in $elements) {
                    Write-Host "  - `"$($el.Text)`""
                }
            } else {
                Write-Host "Tidak ada teks terdeteksi sama sekali." -ForegroundColor Yellow
            }
        }
    }
    elseif ($Index -ge 0) {
        Write-Host "Scanning screen for index $Index..." -ForegroundColor Cyan
        $elements = ScanScreen
        if ($Index -lt $elements.Count) {
            $el = $elements[$Index]
            $clickType = "left"
            if ($Right) { $clickType = "right" }
            elseif ($Double) { $clickType = "double" }
            Write-Host "Found: '$($el.Text)' → ($($el.CenterX), $($el.CenterY))" -ForegroundColor Green
            ClickAt -X $el.CenterX -Y $el.CenterY -ClickType $clickType
            Write-Host "Clicked." -ForegroundColor Green
        } else {
            Write-Host "Index $Index tidak valid. Hanya ada $($elements.Count) elements." -ForegroundColor Red
            if ($elements.Count -gt 0) {
                Write-Host "Gunakan -List untuk melihat semua index yang tersedia." -ForegroundColor Yellow
            } else {
                Write-Host "Tidak ada teks terdeteksi di layar." -ForegroundColor Yellow
            }
        }
    }
    elseif ($Type) {
        Write-Host "Sending keys: '$Type'" -ForegroundColor Cyan
        SendKeys -Text $Type
        Write-Host "Done." -ForegroundColor Green
    }
    else {
        Write-Host @"
Usage:
  .\screen-interact.ps1 -ClickText "Rekomendasi"     cari teks, klik tengahnya
  .\screen-interact.ps1 -ClickText "Search" -Double   double click
  .\screen-interact.ps1 -ClickText "Gadgetin" -Right  right click
  .\screen-interact.ps1 -List                         list semua teks + koordinat + index
  .\screen-interact.ps1 -Index 3                      klik index ke-3 dari list
  .\screen-interact.ps1 -Type "Rekomendasi iPhone"    type text (kirim keystrokes)
"@ -ForegroundColor Yellow
    }
} catch {
    Write-Host "ERROR: $_" -ForegroundColor Red
    exit 1
}
