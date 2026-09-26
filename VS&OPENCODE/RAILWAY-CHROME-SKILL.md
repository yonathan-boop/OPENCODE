---
name: Railway Chrome Setup
description: "Instructions for Antigravity to connect to an existing Chrome browser using Playwright CDP to automate Railway noVNC without stealing physical mouse control."
---

# Railway Chrome CDP Automation Skill

## Latar Belakang & Tujuan
Skill ini dirancang agar PC di tempat kerja (atau PC mana pun) bisa langsung mengetahui cara mengendalikan tab Railway noVNC di Google Chrome tanpa mengganggu pergerakan *mouse* fisik pengguna, menghindari masalah *scaling* Windows.

## Arsitektur Wajib
- **Playwright MCP**: Digunakan khusus untuk membaca struktur web dan mengeklik elemen di dalam tab Chrome. HARUS dijalankan dalam mode CDP.
- **Windows-MCP**: Digunakan KHUSUS untuk UI asli Windows jika diperlukan (seperti dialog sistem), BUKAN untuk interaksi dalam halaman web.

## Langkah Konfigurasi (Wajib Dijalankan Pertama Kali di PC Baru)

Jika agen melihat bahwa Playwright gagal mendeteksi tab Chrome yang sudah berjalan, agen HARUS melakukan langkah-langkah ini:

### 1. Konfigurasi `mcp_config.json`
Pastikan Playwright MCP diatur di `~/.gemini/config/mcp_config.json` dengan format argumen berikut:
```json
"playwright": {
  "command": "npx",
  "args": [
    "-y",
    "@playwright/mcp@latest",
    "--cdp-endpoint=chrome"
  ]
}
```
**Perhatian:** JANGAN pernah menggunakan parameter `--extension`.

### 2. Mengaktifkan Remote Debugging di Chrome
Minta pengguna untuk melakukan ini secara manual di Chrome mereka (agen bisa membantu membuka tab baru, tetapi pengguna yang mencentang):
1. Buka URL: `chrome://inspect/#remote-debugging`
2. Centang kotak bertuliskan: **Allow remote debugging for this browser instance**

### 3. Restart Antigravity
Jika `mcp_config.json` baru saja diubah, agen harus meminta pengguna me-restart aplikasi Antigravity IDE agar pengaturan CDP termuat.

## Standar Operasional Eksekusi (Penarikan Data)
Begitu konfigurasi di atas selesai, agen WAJIB melakukan urutan ini untuk menarik data:
1. Panggil `browser_tabs` dengan argumen `{"action": "list"}` melalui Playwright MCP.
2. Cari tab yang mengandung URL `railway.app` (khususnya tab noVNC / Ubuntu).
3. Panggil `browser_tabs` dengan argumen `{"action": "select", "index": <INDEX_TAB>}`.
4. Panggil `browser_snapshot` untuk membaca DOM halaman (kamu akan melihat tombol 'Connect', dll).
5. Gunakan `browser_click` dan `browser_type` dari Playwright MCP untuk mengotomatisasi interaksi di dalam halaman tersebut (tanpa perlu repot dengan koordinat fisik).

## Pantangan / Larangan
- JANGAN gunakan `windows-mcp` (seperti `Click` atau `Type`) untuk mengeklik elemen di dalam halaman web Google Chrome. Selalu gunakan Playwright MCP agar kursor fisik pengguna tidak bergeser!
- JANGAN meminta pengguna memasukkan sandi Railway; manfaatkan sesi login Chrome (CDP) yang sudah ada.
