# MASTER-MEMORY — VS&OPENCODE

Di-update: 9 Mei 2026
Bersumber dari memory bersama: `C:\Users\Advan\Desktop\memory\`

---

## 📋 SEMUA PC & DEVICE

### 1. PC-06 (Kantor)
- **Nama:** pc-06, WORK-PC, OFFICE-06
- **OS:** Windows 10
- **User:** Admin
- **Folder kerja:** C:\Users\Admin\.work
- **Workspace:** C:\Users\Admin\.work\workspace
- **Screen:** 1920x1080
- **Git:** C:\Users\Admin\Desktop\memory
- **OpenCode:** CLI + GUI

### 2. PC-Advan (Rumah)
- **Nama:** ADVAN, ADVAN-PC, DESKTOP-1E1LBB7
- **OS:** Windows
- **User:** Advan
- **Python:** C:\Users\Advan\AppData\Local\Programs\Python\Python311\python.exe (3.11)
- **Git Portable:** C:\Users\Advan\Documents\PortableGit\bin\git.exe
- **Tesseract:** C:\Program Files\Tesseract-OCR\tesseract.exe (v5.5.0)
- **PyAutoGUI:** ✅ installed
- **VS Code:** C:\Users\Advan\AppData\Local\Programs\Microsoft VS Code\Code.exe
- **Memory folder:** C:\Users\Advan\Desktop\memory

### 3. linux-tablet
- **Device:** Red Magic Tab Astra 3 Pro
- **OS:** Android 15 → Ubuntu (via Termux proot-distro)
- **RAM:** 12 GB
- **Akses:** VNC localhost:5905 (Xtigervnc :5)
- **Path:** /data/data/com.termux/files/home/Desktop/New Folder/memory
- **Software:** Chromium, WPS Office, QEMU (Windows ARM), Remmina, OpenCode

### 4. linux-hp
- **Device:** HP Victus
- **OS:** Linux
- **Path:** /root/memory-linux-hp

### 5. linux-tablet-tiny
- **Device:** Linux langsung di Termux (tanpa VNC/Ubuntu)
- **Path:** /root/Desktop/memory
- **Software:** WPS Office, smbclient
- **SMB Server:** 192.168.1.200 (Methodist-11 Document, user: wilianto)

---

## 📋 PROJECT AKTIF

### 1. Memory System ✅
- Semua memory di-sync via GitHub
- Repo: https://github.com/yonathan-boop/OPENCODE
- Sistem: folder per PC + COMMON/docs

### 2. Absensi Murid
- **Script:** COMMON/scripts/absensi.py
- **Excel:** PC-06/docs/ABSENSI April.xlsx, ABSENSI Mei.xlsx
- **Kelas:** TKa, TKB1, TKB2, PG
- **Format:** Setiap hari duplicate Excel dulu, baru edit
- **Backup:** Banyak file arsip di PC-06/docs/

### 3. Dokumen Ujian (Word)
- **Template:** Agama 6 (checked) Edit.docx
- **Isi:** Pilihan Bergand1.docx
- **Format:** Folio (8.5x13), TNR 11, margin 0.5/0.6/1/1
- **Aturan:** Copy-paste plain text, jangan parsing otomatis

### 4. YouTube Automation (PC-Advan)
- **Tools:** PyAutoGUI + Tesseract OCR
- **Script:** PC-Advan/scripts/
- **Cara:** Buka Chrome → scroll → screenshot → OCR

---

## 📋 ATURAN PENTING

1. **LOAD MEMORY DULU** sebelum kerja besar
2. **SAVE EVERYTHING** — semua instalasi, konfigurasi, keputusan, error WAJIB dicatat
3. **Organisasi file:** SEMUA file dalam folder memory, folder per PC & kategori
4. **Git sync:** pull awal sesi, push akhir sesi
5. **Jangan simpan di luar folder memory!**

## 📋 GAYA KERJA USER
- Instruksi singkat, informal, kadang setengah jadi
- Tangkap maksud paling masuk akal, jangan nunggu prompt detail
- Jangan sering minta klarifikasi kalau arah umum sudah jelas
- Utamakan hasil jadi dibanding teori
- Respons ringkas, natural, langsung ke inti
- `lebih clean` = kurangi ramai, rapikan spacing
- `lebih enak dilihat` = benahi typography, alignment, warna
- `jangan rame` = dekorasi seperlunya
- `bikin modern` = visual segar, sederhana

---

## 📋 LOG PEMBELAJARAN

Lihat file terpisah di COMMON/docs/:
- `MEMORY-LEARNINGS.md` — koreksi, insight, pola yang berhasil
- `MEMORY-ERRORS.md` — error command, tool failure
- `MEMORY-FEATURE-REQUESTS.md` — kemampuan yang diminta user

---

## 📋 RECENT ACTIVITY

### 📋 GIT PUSH PROTOCOL
1. WAJIB specify exact `workdir` saat spawn sub-agent buat commit/push
2. Jangan `git add -A` di root tanpa ls dulu
3. Dua repo wajib: `C:\Users\Advan\Desktop\memory` (shared) + `C:\Users\Advan\memory` (local)
4. Kalau ragu → spawn sub-agent khusus push dengan instruksi path lengkap

--- 

### 9 Mei 2026 — PC-Advan
- Install VS Code v1.116.0
- Install Extension Pack for Java
- Inject dark mode ke Chrome (e-learning UT)
- Setup folder VS&OPENCODE untuk OpenCode VS Code extension
- Update memory dari GitHub (banyak data baru dari PC lain)
- Setup AGENTS.md/SOUL.md/USER.md untuk CLI (openclaw) di `.openclaw\workspace\` biar auto-load shared memory
- Boundary rule: VS Code instance cuma edit `VS&OPENCODE/` — jangan sentuh folder lain di shared memory
- Bantu buat Tugas1.java (Tugas 1 Sistem Data)
