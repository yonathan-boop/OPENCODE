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

### PC-Advan (Rumah)
- Nama: ADVAN, ADVAN-PC, DESKTOP-1E1LBB7
- Model: minimax-m2.5-free
- Trigger commands untuk ChatGPT

---

## 📋 ATURAN UTAMA

1. **Session Startup:** 
   - Baca memory/summary.md, memory/facts/database.md
   - Sync dari GitHub jika perlu

2. **Memory System:**
   - Daily notes: memory/YYYY-MM-DD.md
   - Long-term: MEMORY.md
   - Sinkronisasi via GitHub

3. **Red Lines:**
   - Jangan bocorkan data pribadi
   - Jangan aksi eksternal tanpa izin

---

## 📋 ABSENSI MURID (PC-06)

### Script
- File: absensi.py
- Lokasi: C:/Users/Admin/Desktop/absensi.py
- File Excel: ABSENSI April.xlsx (C:/Users/Admin/Desktop/Absensi/)

### Cara Pakai
```
py absensi.py <nama> <kelas> <tanggal> <alasan>
```

### Kelas
- TKa (TK A)
- TKB1 (TK B1)
- TKB2 (TK B2)
- PG (Play Group)

### Alasan
- sakit → S
- izin → I
- alpha → A

### Contoh
```
py absensi.py Aldrich TKa 16 sakit
py absensi.py Kyla TKB1 14 izin
py absensi.py Edbert PG 13 alpha
```

---

## 📋 RECENT ACTIVITY

### 16 April 2026 - pc-06:
- Setup Python + openpyxl
- Buat script absensi.py
- Input absensi untuk 4 kelas (TKa, TKB1, TKB2, PG)
- Format kolom tanggal (hide 1-13, width=5)
- Push ke GitHub

### 15 April 2026 - PC-Advan:
- Konfigurasi Ollama gemma4:e2b
- Buat memory system
- Setup trigger commands

---

*Catatan: Semua konfigurasi di-sync via GitHub*
*Repo: https://github.com/yonathan-boop/OPENCODE*