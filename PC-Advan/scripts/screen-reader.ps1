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
    [string]$FilePath
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
