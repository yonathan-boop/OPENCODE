# MEMORI KOMPREHENSIF - Admin's AI Assistant

Di-update: 16 April 2026

---

## 📋 IDENTITAS SAYA (AI)

- **Name:** AI Assistant
- **Creature:** AI Assistant
- **Vibe:** Helpful, concise, can be witty
- **Signature:** 🤖

---

## 📋 TENTANG KAMU (USER)

- **Name:** Admin (di pc-06) / Advan (di pc-rumah)
- **Workspace pc-06:** C:\Users\Admin\.work\workspace
- **Workspace Advan:** C:\Users\Advan\Desktop\workspace
- **GitHub:** https://github.com/yonathan-boop/OPENCODE

---

## 📋 KONFIGURASI PC

### PC-06 (Sekarang - Kantor)
- Nama: pc-06, WORK-PC, OFFICE-06
- OS: Windows 10
- Folder kerja: C:\Users\Admin\.work
- Model: minimax-m2.5-free
- Screen: 1920 x 1080

### PC-Advan (Rumah)
- Nama: ADVAN, ADVAN-PC, DESKTOP-1E1LBB7
- Model: minimax-m2.5-free
- Trigger commands untuk ChatGPT
- **Tesseract OCR:** C:\Program Files\Tesseract-OCR\tesseract.exe (v5.5.0)
- **Python:** C:\Users\Advan\AppData\Local\Programs\Python\Python311\python.exe (3.11)
- **PyAutoGUI:** ✅ installed
- **Image Tools MCP:** C:\Users\Advan\Documents\image-tools-mcp\image-tools-mcp-v1.2.1-windows-amd64.exe
- **MCP Config:** C:\Users\Advan\.config\opencode\opencode.json (tanpa Ollama)

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

5. **ORGANISASI FILE (PENTING!):**
   - **SEMUA file WAJIK dalam folder memory**, tidak boleh di luar
   - Folder disusun sesuai PC & kategori
   - Contoh folder:
     - `PC-06/screenshots/` → screenshot PC-06
     - `PC-06/scripts/` → script untuk PC-06
     - `PC-Advan/output/` → output dari PC-Advan
     - `COMMON/docs/` → dokumentasi umum
   - **JANGAN simpan di luar folder memory!**

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

## 📋 PLAYWRIGHT (PC-Advan)
- Install: `pip install playwright` + `python -m playwright install chromium`
- **Masalah:** launch_persistent_context error dengan user_data_dir
- **Masalah:** encryption error (os_crypt) - tidak bisa akses Chrome profile existing
- **Solusi:** Gunakan PyAutoGUI untuk kontrol Chrome yang sudah terbuka

## 📋 PyAutoGUI YouTube Automation
- Python: C:\Users\Advan\AppData\Local\Programs\Python\Python311\python.exe
- Tesseract: C:\Program Files\Tesseract-OCR\tesseract.exe
- Script: C:\Users\Advan\Desktop\memory\PC-Advan\scripts\
- OCR: pytesseract dengan lang='eng+ind'

### Cara Kerja:
1. Buka Chrome → pilih profile → minimize
2. Buka tab baru dengan URL langsung: `start chrome "https://www.youtube.com/@Gadgetin/videos"`
3. Scroll untuk lihat video
4. Screenshot → OCR baca teks
5. Klik video → scroll ke komentar → screenshot → OCR

### Tips:
- Klik profile di posisi (200, 300) untuk profile admin
- Scroll pakai pyautogui.scroll(-500) untuk scroll down
- OCR perlu adjustment posisi crop untuk dapat komentar

---

## 📋 SCREENSHOT & OCR (PC-Advan)

### Install:
```
pip install pytesseract
```

### Cara Ambil Screenshot:
```python
from PIL import ImageGrab
img = ImageGrab.grab()
img.save(r'C:\Users\Advan\Desktop\screenshot.png')
```

### Cara OCR (Baca Teks dari Gambar):
```python
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open(r'C:\Users\Advan\Desktop\screenshot.png')
text = pytesseract.image_to_string(img, lang='eng+ind')
print(text)
```

### Catatan:
- Python path: C:\Users\Advan\AppData\Local\Programs\Python\Python311\python.exe
- Tesseract path: C:\Program Files\Tesseract-OCR\tesseract.exe
- Simpan screenshot ke Desktop dulu, lalu baca

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

### Chrome Shortcuts (PC-06)
- **Chrome Desktop Jarak Jauh.lnk** - di Desktop (butuh dicek lagi fungsinya)

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

### 16 April 2026 - pc-06 (Session 1):
- Install Tesseract OCR v5.5.0 (via winget)
- Install image_tools_mcp v1.2.1
- Setup MCP config
- Discuss vision model options (kimi-k2.5-free, Gemini)
- Rule added: SAVE EVERYTHING to memory

### 16 April 2026 - pc-06 (Session 2):
- Setup memory system
- Connect Gemini API key
- Test image vision - model tidak support
- Install Tesseract OCR + image_tools_mcp untuk OCR local
- Discuss OCR local solution (Tesseract + image_tools_mcp)
- **ATURAN BARU: SEMUA HAL WAJIB DISIMPAN KE MEMORY**

---

*Catatan: Semua konfigurasi di-sync via GitHub*
*Repo: https://github.com/yonathan-boop/OPENCODE*
