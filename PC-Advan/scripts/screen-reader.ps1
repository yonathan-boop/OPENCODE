# screen-reader.ps1 — Windows Screen Reader
# Menggunakan: Tesseract OCR + PowerShell UIAutomation
#
# Usage:
#   .\screen-reader.ps1 -ActiveWindow     (default: screenshot active window + OCR + UI info)
#   .\screen-reader.ps1 -FullScreen        (screenshot full screen + OCR)
#   .\screen-reader.ps1 -UIInfoOnly        (only get UI info, no screenshot/OCR)
#   .\screen-reader.ps1 -FilePath "C:\path\to\image.png"  (OCR an existing image)

param(
    [switch]$ActiveWindow,
    [switch]$FullScreen,
    [switch]$UIInfoOnly,
    [string]$FilePath,
    [switch]$WithCoordinates
)

$ErrorActionPreference = "Stop"
$TesseractPath = "C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------- helper: get timestamp ----------
function Get-Timestamp {
    return (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
}

# ---------- 1. Screenshot function ----------
function Take-Screenshot {
    param([switch]$Full)
    try {
        Add-Type -AssemblyName System.Windows.Forms
        Add-Type -AssemblyName System.Drawing

        if ($Full) {
            $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
        } else {
            $hwnd = Get-ActiveWindowHandle
            $rect = Get-WindowRect -hwnd $hwnd
            $bounds = New-Object System.Drawing.Rectangle($rect.left, $rect.top, ($rect.right - $rect.left), ($rect.bottom - $rect.top))
        }

        $bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
        $gfx = [System.Drawing.Graphics]::FromImage($bmp)
        $gfx.CopyFromScreen($bounds.X, $bounds.Y, 0, 0, $bounds.Size)
        $gfx.Dispose()

        $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
        $path = [System.IO.Path]::Combine($env:TEMP, "opencode-screenreader-$timestamp.png")
        $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()
        return $path
    } catch {
        return "ERROR: Screenshot gagal: $_"
    }
}

# ---------- 2. P/Invoke for Active Window ----------
function Get-ActiveWindowHandle {
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
"@
        Add-Type -TypeDefinition $source -ReferencedAssemblies "System.Runtime.InteropServices" -ErrorAction Stop
    } catch {
        # already loaded
    }
    return [Win32]::GetForegroundWindow()
}

function Get-WindowText {
    param([IntPtr]$hwnd)
    $sb = New-Object System.Text.StringBuilder 256
    [Win32]::GetWindowText($hwnd, $sb, 256) | Out-Null
    return $sb.ToString()
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

# ---------- 3. Active Window Info ----------
function Get-ActiveWindowInfo {
    try {
        $hwnd = Get-ActiveWindowHandle
        if ($hwnd -eq [IntPtr]::Zero) {
            return "ERROR: Tidak ada active window"
        }
        $title = Get-WindowText -hwnd $hwnd
        $rect = Get-WindowRect -hwnd $hwnd
        $procId = Get-WindowProcessId -hwnd $hwnd
        $proc = (Get-Process -Id $procId -ErrorAction SilentlyContinue).ProcessName
        if (-not $proc) { $proc = "unknown" }

        $x = $rect.left
        $y = $rect.top
        $w = $rect.right - $rect.left
        $h = $rect.bottom - $rect.top

        return @{
            Title    = $title
            Process  = $proc
            Position = "$x,$y,$w,$h"
            X        = $x
            Y        = $y
            Width    = $w
            Height   = $h
        }
    } catch {
        return "ERROR: Gagal mendapatkan info window: $_"
    }
}

# ---------- 4. UI Automation ----------
function Get-UIElementTree {
    param([IntPtr]$hwnd, [int]$MaxDepth = 3)
    $result = @()
    try {
        Add-Type -AssemblyName UIAutomationClient -ErrorAction Stop
        $root = [System.Windows.Automation.AutomationElement]::RootElement
        if ($hwnd -eq [IntPtr]::Zero) { return $result }

        $cond = New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::NativeWindowHandleProperty,
            $hwnd.ToInt32()
        )
        $targetWindow = $root.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $cond)
        if ($targetWindow -eq $null) {
            # fallback: cari via process name
            $pid = Get-WindowProcessId -hwnd $hwnd
            $procCond = New-Object System.Windows.Automation.PropertyCondition(
                [System.Windows.Automation.AutomationElement]::ProcessIdProperty,
                $pid
            )
            $targetWindow = $root.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $procCond)
            if ($targetWindow -eq $null) { return @("(window tidak ditemukan di UI Automation tree)") }
        }

        function WalkTree {
            param($element, $depth)
            if ($depth -gt $MaxDepth) { return }
            if ($element -eq $null) { return }

            try {
                $ctrlType = "unknown"
                $name = ""
                $rect = ""
                try { $ctrlType = $element.Current.ControlType.ProgrammaticName } catch { }
                try { $name = $element.Current.Name } catch { }
                try {
                    $r = $element.Current.BoundingRectangle
                    $rect = "$($r.X),$($r.Y),$($r.Width),$($r.Height)"
                } catch { }

                if (-not [string]::IsNullOrWhiteSpace($name)) {
                    $indent = "  " * $depth
                    $result += "$indent[$ctrlType] `"$name`" ($rect)"
                }

                $children = $element.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
                if ($children -ne $null) {
                    for ($i = 0; $i -lt $children.Count; $i++) {
                        WalkTree -element $children[$i] -depth ($depth + 1)
                    }
                }
            } catch {
                # skip elements that can't be traversed
            }
        }

        WalkTree -element $targetWindow -depth 0
    } catch {
        $result = @("UI Automation error: $_")
    }
    return $result
}

# ---------- 5. OCR function ----------
function Invoke-OCR {
    param([string]$ImagePath)
    try {
        if (-not (Test-Path -LiteralPath $TesseractPath)) {
            return "ERROR: Tesseract tidak ditemukan di $TesseractPath"
        }
        if (-not (Test-Path -LiteralPath $ImagePath)) {
            return "ERROR: File gambar tidak ditemukan: $ImagePath"
        }
        $text = & $TesseractPath "$ImagePath" stdout -l eng+ind --psm 3 2>$null
        if (-not $text) { return "(tidak ada teks terdeteksi)" }
        return $text.Trim()
    } catch {
        return "ERROR: OCR gagal: $_"
    }
}

# ---------- 6. OCR with Coordinate (TSV) ----------
function Invoke-OCRWithCoordinates {
    param([string]$ImagePath)
    try {
        if (-not (Test-Path -LiteralPath $TesseractPath)) { Write-Host "DEBUG: Tesseract not found"; return @() }
        if (-not (Test-Path -LiteralPath $ImagePath)) { Write-Host "DEBUG: Image not found"; return @() }

        $tsvOutput = & $TesseractPath "$ImagePath" stdout -l eng+ind --psm 11 tsv 2>$null
        if (-not $tsvOutput) { Write-Host "DEBUG: TSV output empty"; return @() }

        $lines = $tsvOutput -split "`n" | Where-Object { $_ -ne "" }
        if ($lines.Count -lt 2) { Write-Host "DEBUG: Only $($lines.Count) lines"; return @() }
        Write-Host "DEBUG: TSV lines = $($lines.Count), first line: '$($lines[0].Substring(0, [Math]::Min(50, $lines[0].Length)))'"

        $header = $lines[0] -split "`t"
        $colIdx = @{}
        for ($i = 0; $i -lt $header.Count; $i++) { $colIdx[$header[$i].Trim()] = $i }

        $words = [System.Collections.ArrayList]@()
        for ($i = 1; $i -lt $lines.Count; $i++) {
            $cols = $lines[$i] -split "`t"
            if ($cols.Count -le $colIdx["text"]) { continue }
            if ([int]$cols[$colIdx["level"]] -ne 5) { continue }
            $conf = [double]$cols[$colIdx["conf"]]
            $text = $cols[$colIdx["text"]]
            if ($conf -le 0 -or [string]::IsNullOrWhiteSpace($text)) { continue }
            [void]$words.Add(@{
                block = [int]$cols[$colIdx["block_num"]]
                par   = [int]$cols[$colIdx["par_num"]]
                line  = [int]$cols[$colIdx["line_num"]]
                left  = [int]$cols[$colIdx["left"]]
                top   = [int]$cols[$colIdx["top"]]
                width = [int]$cols[$colIdx["width"]]
                height = [int]$cols[$colIdx["height"]]
                text  = $text.Trim()
                conf  = $conf
            })
        }
        Write-Host "DEBUG: Words parsed = $($words.Count)"
        if ($words.Count -eq 0) { Write-Host "DEBUG: No words found - checking first data row columns..."; return @() }
        $result = Merge-TSVElements -Words $words
        Write-Host "DEBUG: Merged elements = $($result.Count)"
        return $result
    } catch { Write-Host "DEBUG: Exception: $_"; return @() }
}

function Merge-TSVElements {
    param([array]$Words)
    Write-Host "DEBUG Merge-TSVElements: Words received = $($Words.Count), type = $($Words[0].GetType().Name)"
    Write-Host "DEBUG Merge-TSVElements: First word keys: $($Words[0].Keys -join ',')"
    $elements = @()
    $groups = $Words | Group-Object { "{0}.{1}.{2}" -f $_['block'], $_['par'], $_['line'] }
    Write-Host "DEBUG Merge-TSVElements: Groups = $($groups.Count)"

    $groupIdx = 0
    foreach ($group in $groups) {
        $groupIdx++
        Write-Host "DEBUG: Processing group $groupIdx, group.Group type = $($group.Group.GetType().Name), count = $(@($group.Group).Count)"
        $sorted = @($group.Group | Sort-Object { $_['left'] })
        Write-Host "DEBUG: sorted count = $($sorted.Count)"
        if ($sorted.Count -eq 0) { continue }
        $currentGroup = @($sorted[0])

        for ($i = 1; $i -lt $sorted.Count; $i++) {
            $prev = $currentGroup[-1]
            $curr = $sorted[$i]
            $pl = $prev['left']; $pw = $prev['width']; $cl = $curr['left']
            $gap = $cl - ($pl + $pw)
            if ($groupIdx -eq 2) { Write-Host "DEBUG GRP2 i=$i '$($prev['text'])'->'$($curr['text'])': cl=$cl - (pl=$pl + pw=$pw) = $gap" }
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
    $lefts = @($Words | ForEach-Object { $_['left'] })
    $tops = @($Words | ForEach-Object { $_['top'] })
    $rights = @($Words | ForEach-Object { $_['left'] + $_['width'] })
    $bottoms = @($Words | ForEach-Object { $_['top'] + $_['height'] })
    $minLeft = ($lefts | Measure-Object -Minimum).Minimum
    $minTop = ($tops | Measure-Object -Minimum).Minimum
    $maxRight = ($rights | Measure-Object -Maximum).Maximum
    $maxBottom = ($bottoms | Measure-Object -Maximum).Maximum
    $fullText = ($Words | ForEach-Object { $_['text'] }) -join " "
    return @{
        Text    = $fullText
        X       = $minLeft
        Y       = $minTop
        Width   = $maxRight - $minLeft
        Height  = $maxBottom - $minTop
        CenterX = [math]::Round(($minLeft + $maxRight) / 2)
        CenterY = [math]::Round(($minTop + $maxBottom) / 2)
    }
}

# ---------- 7. UI Element Raw Data (for type matching) ----------
function Get-UIElementRawData {
    param([IntPtr]$hwnd, [int]$MaxDepth = 3)
    $result = @()
    try {
        Add-Type -AssemblyName UIAutomationClient -ErrorAction Stop
        $root = [System.Windows.Automation.AutomationElement]::RootElement
        if ($hwnd -eq [IntPtr]::Zero) { return $result }

        $cond = New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::NativeWindowHandleProperty, $hwnd.ToInt32())
        $targetWindow = $root.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $cond)
        if ($targetWindow -eq $null) {
            $pid = Get-WindowProcessId -hwnd $hwnd
            $procCond = New-Object System.Windows.Automation.PropertyCondition(
                [System.Windows.Automation.AutomationElement]::ProcessIdProperty, $pid)
            $targetWindow = $root.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $procCond)
            if ($targetWindow -eq $null) { return $result }
        }

        function WalkTree {
            param($element, $depth)
            if ($depth -gt $MaxDepth -or $element -eq $null) { return }
            try {
                $ctrlType = "Text"
                $name = ""
                try { $ctrlType = ($element.Current.ControlType.ProgrammaticName -replace "^ControlType\.", "") } catch { }
                try { $name = $element.Current.Name } catch { }
                try {
                    $r = $element.Current.BoundingRectangle
                    if (-not [string]::IsNullOrWhiteSpace($name) -and $r.Width -gt 0 -and $r.Height -gt 0) {
                        $result += @{
                            Type   = $ctrlType
                            Text   = $name
                            X      = [int]$r.X
                            Y      = [int]$r.Y
                            Width  = [int]$r.Width
                            Height = [int]$r.Height
                        }
                    }
                } catch { }
                $children = $element.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
                if ($children -ne $null) {
                    for ($i = 0; $i -lt $children.Count; $i++) { WalkTree -element $children[$i] -depth ($depth + 1) }
                }
            } catch { }
        }
        WalkTree -element $targetWindow -depth 0
    } catch { }
    return $result
}

function Get-MatchingUIType {
    param([string]$Text, [int]$X, [int]$Y, [int]$Width, [int]$Height, [array]$UIElements)
    $ocrCx = $X + $Width / 2
    $ocrCy = $Y + $Height / 2
    $textLower = $Text.ToLower()
    foreach ($ui in $UIElements) {
        $inX = ($ocrCx -ge ($ui.X - 10)) -and ($ocrCx -le ($ui.X + $ui.Width + 10))
        $inY = ($ocrCy -ge ($ui.Y - 10)) -and ($ocrCy -le ($ui.Y + $ui.Height + 10))
        if ($inX -and $inY) {
            $uiTextLower = $ui.Text.ToLower()
            if ($uiTextLower -eq $textLower -or $uiTextLower -like "*$textLower*" -or $textLower -like "*$uiTextLower*") {
                return $ui.Type
            }
        }
    }
    return "Text"
}

# ========== MAIN ==========
$output = @"

=== SCREEN READER ===
Timestamp: $(Get-Timestamp)

"@

# --- Determine mode ---
if ($UIInfoOnly) {
    $mode = "UIInfoOnly"
} elseif ($FullScreen) {
    $mode = "FullScreen"
} elseif ($FilePath) {
    $mode = "FilePath"
} else {
    $mode = "ActiveWindow"
}

$output += "Mode: $mode`n"
$output += "`n"

# --- Get active window info (always if not FilePath mode) ---
$winInfo = $null
if ($mode -ne "FilePath") {
    $winInfo = Get-ActiveWindowInfo
    if ($winInfo -is [hashtable]) {
        $output += "--- ACTIVE WINDOW ---`n"
        $output += "Title: $($winInfo.Title)`n"
        $output += "Process: $($winInfo.Process)`n"
        $output += "Position: $($winInfo.Position)`n"
        $output += "`n"
    } else {
        $output += "--- ACTIVE WINDOW ---`n"
        $output += "$winInfo`n`n"
    }
}

# --- Screenshot + OCR ---
$imagePath = $null
if ($mode -eq "FullScreen") {
    $imagePath = Take-Screenshot -Full
} elseif ($mode -eq "ActiveWindow" -or $mode -eq "FilePath") {
    if ($mode -eq "FilePath") {
        $imagePath = $FilePath
    } else {
        $imagePath = Take-Screenshot
    }
}

if ($imagePath -and $imagePath -notlike "ERROR:*") {
    $output += "--- OCR TEXT ---`n"
    $ocrText = Invoke-OCR -ImagePath $imagePath
    $output += "$ocrText`n`n"

    # --- OCR Text (With Coordinates) ---
    if ($WithCoordinates) {
        Write-Host "DEBUG: WithCoordinates = true"
        $ocrElements = Invoke-OCRWithCoordinates -ImagePath $imagePath
        Write-Host "DEBUG: ocrElements count = $($ocrElements.Count)"
        $uiRawData = @()
        if ($mode -ne "FilePath") {
            $hwnd_coord = Get-ActiveWindowHandle
            $uiRawData = Get-UIElementRawData -hwnd $hwnd_coord
        }
        $output += "--- OCR TEXT (WITH COORDINATES) ---`n"
        if ($ocrElements.Count -gt 0) {
            foreach ($el in $ocrElements) {
                $type = "Text"
                if ($uiRawData.Count -gt 0) {
                    $matched = Get-MatchingUIType -Text $el.Text -X $el.X -Y $el.Y -Width $el.Width -Height $el.Height -UIElements $uiRawData
                    if ($matched) { $type = $matched }
                }
                $output += "[$type] `"$($el.Text)`" → ($($el.X), $($el.Y), $($el.Width), $($el.Height))`n"
            }
        } else {
            $output += "(tidak ada teks terdeteksi)`n"
        }
        $output += "`n"
    }

    # Cleanup temp file
    if ($mode -ne "FilePath" -and (Test-Path -LiteralPath $imagePath)) {
        Remove-Item -LiteralPath $imagePath -Force -ErrorAction SilentlyContinue
    }
} elseif ($imagePath -and $imagePath -like "ERROR:*") {
    $output += "--- OCR TEXT ---`n"
    $output += "$imagePath`n`n"
}

# --- UI Elements ---
if ($mode -ne "FilePath" -and $mode -ne "FullScreen") {
    $hwnd = Get-ActiveWindowHandle
    $elements = Get-UIElementTree -hwnd $hwnd -MaxDepth 3
    $output += "--- UI ELEMENTS ---`n"
    if ($elements.Count -gt 0) {
        foreach ($el in $elements) {
            $output += "$el`n"
        }
    } else {
        $output += "(tidak ada UI elements terdeteksi)`n"
    }
    $output += "`n"
}

# --- Output ---
Write-Output $output.TrimEnd()
