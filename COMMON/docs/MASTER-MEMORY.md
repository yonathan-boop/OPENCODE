# MEMORI KOMPREHENSIF - Admin's AI Assistant

Di-update: 16 April 2026

---

## 📋 IDENTITAS SAYA (AI)

- **Name:** OpenCode Agent / OpenClaw Agent
- **Creature:** AI Assistant
- **Vibe:** Helpful, concise, can be witty
- **Signature:** 🤖

---

## 📋 TENTANG KAMU (USER)

- **Name:** Admin (di pc-06) / Advan (di pc-rumah)
- **Workspace pc-06:** C:\Users\Admin\.openclaw\workspace
- **Workspace Advan:** C:\Users\Advan\Desktop\workspace
- **GitHub:** https://github.com/yonathan-boop/OPENCODE

---

## 📋 KONFIGURASI PC

### PC-06 (Sekarang - Kantor)
- Nama: pc-06, WORK-PC, OFFICE-06
- OS: Windows 10
- Folder openclaw: C:\Users\Admin\.openclaw
- Folder opencode: C:\Users\Admin\.opencode
- Model: minimax-m2.5-free (opencode: big-pickle)
- Screen: 1920 x 1080

### PC-Advan (Rumah)
- Nama: ADVAN, ADVAN-PC, DESKTOP-1E1LBB7
- Model: minimax-m2.5-free
- Trigger commands untuk ChatGPT

---

## 📋 ATURAN UTAMA

1. **Session Startup:** 
   - Baca MASTER-MEMORY.md
   - Sync dari GitHub jika perlu

2. **Memory System:**
   - Sinkronisasi via GitHub
   - **WAJIB SIMPAN SEMUA HAL** - Apapun yang terjadi di session, keputusan user, installasi, konfigurasi, dll → SIMPAN ke memory

3. **Red Lines:**
   - Jangan bocorkan data pribadi
   - Jangan aksi eksternal tanpa izin

4. **SAVE EVERYTHING:**
   - Semua installasi → catat
   - Semua konfigurasi → catat
   - Semua keputusan user → catat
   - Semua error/solusi → catat
   - Buat sub-memory file jika perlu (per-PC, per-project, per-topic)
   - Jangan ada yang terlewat, SELALU SIMPAN

---

## 📋 ABSENSI MURID (PC-06)

### Script
- File: absensi.py
- Lokasi: C:/Users/Admin/Desktop/memory/absensi.py

### Cara Pakai
```
py absensi.py <nama> <kelas> <tanggal> <alasan>
```

### Kelas: TKa, TKB1, TKB2, PG

### Alasan: sakit (S), izin (I), alpha (A)

---

## 📋 TRIGGER COMMANDS

- `/loadmemory` → git pull + baca memory
- `/savememory` atau "simpan" → commit + push  
- `/ingat "<isi>"` → catat ke memory

---

## 📋 BROWSER AUTOMATION

### 1. PYAUTOGUI (RECOMMENDED untuk Chrome)

**Install:**
```
pip install pyautogui pymsgbox
```

**KELEBIHAN:**
- Buka Chrome existing (login tetap tersimpan!)
- Tidak ada masalah encryption
- Simple dan reliable

**Script:** chrome_automation.py
- Buka Chrome + URL
- Focus ke Chrome yang sudah terbuka
- Refresh, tab baru, dll

**Status:** ✅ Tested & Working

---

### 2. PLAYWRIGHT

**Install:**
```
pip install playwright
playwright install chromium
```

**MASALAH:**
- launch_persistent_context error dengan user_data_dir
- encryption error (os_crypt)
- Tidak bisa akses existing Chrome profile dengan baik

**Gunakan hanya untuk:**
- Fresh browser automation
- Web scraping tanpa perlu login
- Testing

**Status:** ⚠️ Ada masalah dengan existing profile

---

## 📋 OCR & IMAGE TOOLS (PC-06)

### Tesseract OCR
- **Install:** via winget (`winget install -e --id tesseract-ocr.tesseract`)
- **Version:** 5.5.0.20241111
- **Path:** C:\Program Files\Tesseract-OCR\tesseract.exe
- **Status:** ✅ Installed & Working

### Image Tools MCP
- **Download:** https://github.com/ironsheep/image_tools_mcp/releases
- **File:** image-tools-mcp-v1.2.1-windows-amd64.exe
- **Lokasi:** C:\Users\Admin\Documents\image-tools-mcp-v1.2.1-windows-amd64.exe
- **Status:** ✅ Installed

### OpenCode MCP Config
- **File:** C:\Users\Admin\.config\opencode\opencode.json
- **Config:** 
  ```json
  {
    "mcp": {
      "image_tools": {
        "command": "C:\\Users\\Admin\\Documents\\image-tools-mcp-v1.2.1-windows-amd64.exe",
        "env": {
          "TESSERACT_PATH": "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        }
      }
    }
  }
  ```

### Tools Available
- `image_ocr_full` - baca teks dari gambar
- `image_load` - load gambar
- `image_dimensions` - ukuran gambar
- `image_sample_color` - ambil warna pixel
- `image_detect_text_regions` - deteksi area teks

---

## 📋 OPENCODE SETUP (PC-06)

### CLI Location
- CLI: C:\Users\Admin\AppData\Local\OpenCode\opencode-cli.exe
- GUI: C:\Users\Admin\AppData\Local\OpenCode\OpenCode.exe

### Memory System
- Folder: C:\Users\Admin\.opencode\memory\
- Files: summary.md, facts/database.md, facts/2026-04-11.md

### Shortcuts (Desktop)
- Buka OpenCode - Baca Memory.bat → auto-load opencode memory
- Buka OpenCode - Baca Memory Openclaw.bat → auto-load openclaw memory
- Buka OpenCode GUI.bat → GUI mode

### Model: big-pickle (default)

---

## 📋 RECENT ACTIVITY

### 16 April 2026 - pc-06 (Session 1 - OpenCode):
- Install Tesseract OCR v5.5.0 (via winget)
- Install image_tools_mcp v1.2.1
- Setup opencode.json MCP config
- Discuss vision model options (kimi-k2.5-free, Gemini)
- Rule added: SAVE EVERYTHING to memory

### 16 April 2026 - pc-06 (Session 2 - OpenCode):
- Setup memory system untuk opencode
- Connect Gemini API key
- Test image vision - model big-pickle tidak support
- Install Tesseract OCR + image_tools_mcp untuk OCR local
- Discuss OCR local solution (Tesseract + image_tools_mcp)
- **ATURAN BARU: SEMUA HAL WAJIB DISIMPAN KE MEMORY**

---

*Catatan: Semua konfigurasi di-sync via GitHub*
*Repo: https://github.com/yonathan-boop/OPENCODE*
