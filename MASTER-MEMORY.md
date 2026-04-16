# MEMORI KOMPREHENSIF - Admin's AI Assistant

Di-update: 16 April 2026

---

## 📋 IDENTITAS SAYA (AI)

- **Name:** OpenCode Agent
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
- OS: Windows
- Folder openclaw: C:\Users\Admin\.openclaw
- Model: minimax-m2.5-free
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

3. **Red Lines:**
   - Jangan bocorkan data pribadi
   - Jangan aksi eksternal tanpa izin

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

## 📋 RECENT ACTIVITY

### 16 April 2026 - pc-06:
- Setup Python + openpyxl
- Absensi script untuk 4 kelas (TKa, TKB1, TKB2, PG)
- Install PyAutoGUI - ✅ Tested (screen 1920x1080, mouse control OK)
- Install Playwright - ⚠️ Problem dengan existing profile
- **Solusi: Pakai PyAutoGUI untuk Chrome automation (login tetap ada)**
- Buat chrome_automation.py - cara yang berhasil

---

*Catatan: Semua konfigurasi di-sync via GitHub*
*Repo: https://github.com/yonathan-boop/OPENCODE*
