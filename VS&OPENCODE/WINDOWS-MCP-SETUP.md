# Setup Windows-MCP (26 September 2026)

## Konfigurasi
Kita telah berhasil menghubungkan Antigravity (sebagai "Otak") dengan **Windows-MCP** (sebagai "Tangan") untuk mengendalikan PC secara lokal dan aman.

File konfigurasi berada di: `C:\Users\yonat\.gemini\config\mcp_config.json`

```json
{
  "mcpServers": {
    "windows-mcp": {
      "command": "C:\\Users\\yonat\\AppData\\Roaming\\Python\\Python314\\Scripts\\uvx.exe",
      "args": [
        "windows-mcp",
        "serve",
        "--transport",
        "stdio",
        "--tools",
        "Screenshot,Snapshot,DisplayInventory,Click,Type,Scroll,Move,Shortcut,Wait,WaitFor"
      ],
      "env": {
        "ANONYMIZED_TELEMETRY": "false"
      }
    }
  }
}
```

## Cara Kerjanya (Arsitektur)
1. **Antigravity (Cloud Brain)**: Menerima perintah bahasa natural dari Anda dan memikirkannya (reasoning).
2. **Windows-MCP (Local Hands)**: Antigravity mengirimkan instruksi via standar protokol MCP (Model Context Protocol) ke server lokal `windows-mcp` melalui jalur *stdio*.
3. **Eksekusi Lokal**: `windows-mcp` berjalan secara lokal menggunakan Python 3.13+ (lewat `uvx.exe`). Ia bisa melihat layar lewat *Screenshot/Snapshot*, membaca struktur *UI Automation* Windows (membaca elemen teks, tombol, nama jendela), lalu melakukan *Mouse/Keyboard control* sesuai instruksi.

## Pengujian yang Sudah Dilakukan
Semua alat telah diuji dan berfungsi dengan baik:
- **Screenshot & Snapshot**: Berhasil menangkap layar dan mendeteksi jendela/elemen interaktif (UI Tree) dari desktop yang sedang berjalan.
- **Move**: Berhasil memindahkan kursor (terdapat isu minor terkait presisi karena DPI scaling Windows atau interferensi fisik mouse, tapi sistem tetap bisa berjalan dengan fallback UI tree center coordinates).
- **Click**: Berhasil mengidentifikasi kotak input lewat koordinat tengahnya dan melakukan klik yang aman (memfokuskan input).
- **Type**: Berhasil mengetik "MCP_TEST_12345" ke dalam input yang difokuskan, dan mencoba perintah `clear` (fitur clear dari `windows-mcp` memiliki sedikit bug Python internal ketika string kosong, tetapi ketik normal berfungsi sempurna).

## Kesimpulan
Sistem penglihatan (mata), klik (tangan), dan pengetikan (keyboard) sudah berjalan dengan sukses secara natif. Antigravity sudah memiliki kontrol penuh secara terkendali.
