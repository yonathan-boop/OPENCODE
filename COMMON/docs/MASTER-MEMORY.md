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
- Lokasi: C:/Users/Admin/Desktop/memory/COMMON/scripts/absensi.py

### Struktur Excel Absensi (Format Baru)
- Setiap sheet = satu kelas (TKa, TKB1, TKB(2), Absen PG)
- Row 7+ = data murid, Kolom 3 = nama
- Row 6 = header tanggal (April 1 = col 4, April 2 = col 5, dst)
- Tidak ada sheet 'Data'

### Cara Pakai
```
py absensi.py <nama> <kelas> <tanggal> <alasan>
```

### Kelas: TKa, TKB1, TKB2, PG

### Alasan: sakit (S), izin (I), alpha (A)

### Absensi 13-15 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| Senin 13/4 | TKB1 | Gabe | I |
| Senin 13/4 | TKB1 | Larasati | S |
| Selasa 14/4 | TKB1 | Gabe | I |
| Rabu 15/4 | TKB1 | Gabe | I |
| Rabin 15/4 | TKB1 | Naraya | S |

### Absensi Excel File
- **File:** C:\Users\Admin\Desktop\memory\PC-06\docs\ABSENSI April.xlsx
- **Status:** Aktif digunakan
- **ATURAN:** 
  - Setiap update WAJIB duplicate dulu (buat file baru), baru edit
  - **1 file baru per hari** - tidak boleh lebih dari 1 file sehari
  - File lama = arsip, tidak dihapus
- **Format Nama File Duplicate:** Absensi <bulan> <tgl> <tahun> <hari> <jam>_<menit>_<detik>.xlsx
  - Contoh: Absensi April 22 2026 Wednesday 10_27_21.xlsx
- **Lokasi File:** C:\Users\Admin\Desktop\memory\PC-06\docs\

### Absensi 23 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 23/4 | TKB(2) | Chelsea Valerie | S |
| 23/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 20/4 | TKB1 | Gestalt | I |
| 20/4 | TKB1 | Jocelyn | S |
| 20/4 | TKB1 | Larasaty | S |
| 20/4 | TKB1 | Jayden | I |
| 21/4 | TKB1 | Larasaty | S |
| 22/4 | TKB1 | Raileen | S |
| 22/4 | TKB1 | Larasaty | S |
| 23/4 | TKB1 | Jayden | I |
| 23/4 | TKB1 | Jocelyn | I |
| 23/4 | TKB1 | Reiner | I |
| 23/4 | TKB1 | Gabe | I |
| 23/4 | TKa | Richel Wijaya | S |
| 23/4 | TKa | Darren Elvano | S |
| 23/4 | TKa | Shelo | I |

- File hasil: Absensi April 23 2026 Thursday 12_21_13.xlsx

### Absensi 27 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 25/4 | PG | Joverick | I |
| 27/4 | PG | Joverick | I |
| 25/4 | TKB(2) | Chelsea Valerie | S |
| 25/4 | TKB(2) | Marquez Boas Aritonang | S |
| 25/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 25/4 | TKB(2) | Jasmine Valerie Yap | S |
| 25/4 | TKB(2) | Christine Laotan | S |
| 27/4 | TKB(2) | Pangeran Hagro Haloho | S |
| 27/4 | TKB(2) | Alvaro Gavriel Karo Karo | S |
| 27/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 25/4 | TKB1 | Jocelyn Marcella Su | I |
| 25/4 | TKB1 | Naraya Elsandri Br. Sembiring | I |
| 25/4 | TKB1 | Gabe Cristiano Gultom | I |
| 27/4 | TKB1 | Grace Felicia Simbolon | S |
| 25/4 | TKa | Azka Andreas | I |
| 25/4 | TKa | Lishaalini Krisna Naidu | S |
| 27/4 | TKa | Richelcia Wijaya | A |
| 27/4 | TKa | Celine Grace Zhang | S |
| 27/4 | TKa | Lishaalini Krisna Naidu | S |

- File hasil: Absensi April 27 2026 Monday 09_09_12.xlsx

### Absensi 22 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 18/4 | TKa | Aldrich, Darren Elvano, Clarita, Richelcia | S |
| 20/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |
| 21/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |
| 22/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |

- File hasil: Absensi April 22 2026 Wednesday 10_27_21.xlsx

### Absensi 17 April 2026

| Kelas | Nama | Alasan |
|-------|------|--------|
| TKa | Richel Wijaya | S |
| TKa | Aldrich S | S |
| TKa | Clarita S | S |
| TKB1 | Joverick S | S |
| TKB2 | Shayna S | S |
| TKB2 | Claudia S | S |
| TKB2 | Brienne S | S |

---

## 📋 TRIGGER COMMANDS

- `/loadmemory` → git pull + baca memory
- `/savememory` atau "simpan" → commit + push  
- `/ingat "<isi>"` → catat ke memory

### Perilaku Saat Load Memory
- Deteksi folder memory aktif (pc-06 / PC-Advan)
- Baca `COMMON/docs`, `PC-06`, `PC-Advan`
- Baca log pembelajaran: `MEMORY-LEARNINGS.md`, `MEMORY-ERRORS.md`, `MEMORY-FEATURE-REQUESTS.md`
- Gabungkan semuanya jadi konteks kerja aktif

---

## 📋 GAYA ASISTEN YANG DIINGINKAN USER

### Prinsip Umum
- User suka memberi instruksi singkat, informal, dan kadang setengah jadi
- Asisten harus menangkap maksud paling masuk akal dari konteks, bukan menunggu prompt super detail
- Jangan terlalu sering minta klarifikasi jika arah umum sudah jelas
- Kalau memang perlu tanya, cukup 1 pertanyaan paling penting
- Utamakan hasil jadi dibanding teori panjang
- Jaga agar respons tetap ringkas, natural, dan langsung ke inti

### Jika User Memberi Contoh / Referensi
- Contoh hasil adalah acuan utama
- Pahami vibe, style, struktur layout, tingkat kerapihan, dan rasa visualnya
- Jangan menyalin mentah; tirukan kualitas keputusan desainnya
- Kalau user bilang `kayak yang tadi`, pertahankan arah utama tanpa minta penjelasan ulang dari nol

### Interpretasi Instruksi Pendek
- `lebih clean` = kurangi keramaian, rapikan hierarchy, spacing lebih lega
- `lebih enak dilihat` = typography lebih rapi, alignment lebih baik, warna lebih terkontrol
- `jangan rame` = dekorasi seperlunya, fokus utama jelas
- `bikin modern` = visual lebih segar, sederhana, dan relevan dengan standar UI sekarang

### Profil Natural / Manusiawi
- Terdokumentasi di `COMMON/docs/ASSISTANT-PROFILE-NATURAL.md`

### Profil Khusus Coding + Desain Web
- Terdokumentasi di `COMMON/docs/ASSISTANT-PROFILE-CODING-WEB.md`

---

## 📋 SELF-IMPROVING MEMORY SYSTEM

Tujuan: memory bukan cuma arsip, tapi mesin belajar yang membuat asisten makin pas dari waktu ke waktu.

### File Pembelajaran
- `COMMON/docs/MEMORY-LEARNINGS.md` → koreksi, insight, pola yang berhasil
- `COMMON/docs/MEMORY-ERRORS.md` → error command, tool failure, kegagalan proses
- `COMMON/docs/MEMORY-FEATURE-REQUESTS.md` → kemampuan yang diminta user

### Kapan Harus Dicatat
- User mengoreksi jawaban / arah kerja AI
- Ada error yang penting atau berulang
- User bilang ingin gaya kerja tertentu
- Ditemukan pola keputusan yang jelas lebih cocok untuk user

### Aturan Promosi
- Jika suatu pola muncul berulang atau penting lintas sesi, ringkas dan promosikan ke `MASTER-MEMORY.md`
- Catat secukupnya, tanpa menyimpan data sensitif mentah

### Pesan Penting dari User
- "kamu itu kan tidak bisa langsung megerjakan hal besar... jadi harus rajin rajin mencatat dan membaca di memori tolong di simpan ya"
- Asisten harus rajin baca memory sebelum kerja dan rajin simpan hal penting setelah kerja

---

## 📋 GIT (PC-Advan)
- **Git Portable:** C:\Users\Advan\Documents\PortableGit\bin\git.exe (v2.45.1)
- Note: Git regular di-uninstall karena makan RAM
- Sinkronisasi memory via Portable Git

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

## 📋 CARA EDIT DOKUMEN UJIAN (WORD)

### File yang Digunakan
- **Template (Format):** `Agama 6 (checked) Edit.docx` → 100% benar
- **Isi yang Benar:** `Pilihan Bergand1.docx` → dari IPA 6.docx, paste as plain text

### Langkah yang Benar

**1. FIX URUTAN TERLEBIH DAHULU**
- Buka file asli (IPA 6.docx)
- Copy semua → Paste as **Plain Text / Keep Text Only**
- Hasil: `Pilihan Bergand1.docx` (urutan sudah benar, ada 1., 2., a., b., c., d.)

**2. SAMAKAN FORMAT**
- Duplicate file template (Agama Edit) → jadi file baru
- Load template + load `Pilihan Bergand1`
- Ambil **SEMUA** paragraf dari `Pilihan Bergand1` (urutan tetap!)
- Replace paragraf di template mulai dari setelah "Pilihan Ganda (50%)"
- Ganti "Agama" → "IPA" di tabel kop

### Poin Penting
- ❌ Jangan parsing otomatis (AI tidak stabil baca numbering Word)
- ✅ Copy-Paste sebagai Plain Text - urutan pasti benar
- ✅ Replace berdasarkan urutan, bukan index
- ✅ Format dari template, isi dari Pilihan Bergand1

### Aturan Berkas
- Setelah selesai edit dokumen, **hapus file temporary** yang dibuat saat proses editing (bukan file hasil)
- File hasil yang sudah final tetap disimpan
- Jangan biarkan banyak file berserakan di folder kerja

---

## 📋 FORMAT DOKUMEN UJIAN (BARU)

### Spesifikasi
- **Ukuran Kertas:** Folio (8.5 x 13 inch)
- **Margin:** Top 0.5, Bottom 0.6, Left 1, Right 1
- **Font:** Times New Roman, ukuran 11
- **Line Spacing:** 1 (sebelum 0, sesudah 0)
- **Indentasi soal:** First line hanging 0.65
- **Indentasi opsi (a. b. c. d.):** Left indent 0.65 + first line hanging 0.65

### Catatan
- Kalau file sumber **tidak ada nomor** (seperti IPA 6.docx), perlu paste dari file yang sudah ada nomor (Pilihan Bergand1.docx)

---

### 17 April 2026 - pc-06 (Session 3):
- Install xlwings 0.35.1 (pip install xlwings)
- Install pywin32-311 (otomatis)
- Install pandas 3.0.2 + numpy 2.4.4
- win32com sudah tersedia (dari pywin32)
- **Pesan penting user:** "kamu itu kan tidak bisa langsung megerjakan hal besar... jadi harus rajin mencatat dan membaca di memori, tolong di simpan ya"
- Install docxtpl 0.20.2 + jinja2 3.1.6 (untuk edit Word pake template)

---

*Catatan: Semua konfigurasi di-sync via GitHub*
*Repo: https://github.com/yonathan-boop/OPENCODE*
