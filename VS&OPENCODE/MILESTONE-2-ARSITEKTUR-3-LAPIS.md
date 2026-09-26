# MILESTONE 2: Arsitektur 3 Lapis (Three-Tier Architecture)

## Pencapaian
Keberhasilan kedua: Sistem sekarang memiliki 3 indra/lapisan kontrol yang spesifik dan stabil, tanpa mengandalkan tebakan koordinat mouse fisik.

## 1. Playwright MCP (Web & Chrome)
*   Menggunakan mode Chrome CDP.
*   Digunakan untuk elemen DOM, situs web, dan ekstensi.

## 2. FlaUI-MCP (Windows Native)
*   Berhasil diinstal dari starpia-forge/FlaUI-MCP versi *self-contained*.
*   Digunakan untuk aplikasi Windows asli (File Explorer, Notepad, Calculator, UI Setting).
*   Berhasil mengendalikan UI Windows murni secara *semantic* (InvokePattern, ValuePattern, WindowPattern) tanpa membajak mouse fisik sama sekali.

## 3. Windows-MCP (Fallback Visual)
*   Sistem cadangan (fallback) terakhir.
*   Hanya digunakan untuk area abu-abu (VNC Canvas, Game, antarmuka berbasis piksel).

## Tool Priority Policy
Sistem sekarang diatur untuk **selalu** mendahulukan kontrol *semantic/native* (Playwright dan FlaUI) sebelum turun menggunakan manipulasi *mouse* fisik dari Windows-MCP. Aturan ini sudah dikukuhkan sebagai kebijakan global agen Antigravity di komputer ini.
