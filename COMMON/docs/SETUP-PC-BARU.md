# SETUP PC BARU / RESET — Panduan Lengkap

## 1. Install Git (kalau belum)
```bash
# Windows (winget)
winget install -e --id Git.Git

# Linux
sudo apt update && sudo apt install -y git
```

## 2. Clone Memory dari GitHub
```bash
cd ~\Desktop
git clone https://ghp_TOKEN_DARI_SERVER@github.com/yonathan-boop/OPENCODE memory
cd memory
git pull
```

**Kalau token expired / error 403:**
1. Buka https://github.com/settings/tokens
2. Generate new token (classic) → centang scope `repo`
3. Copy token baru, jalankan:
```bash
git remote set-url origin https://ghp_TOKEN_BARU@github.com/yonathan-boop/OPENCODE
git pull
```

## 3. Install OpenCode
```bash
# Windows (Scoop)
scoop install opencode

# Linux (npm)
npm install -g opencode-ai

# macOS (brew)
brew install opencode
```

## 4. Setup Config OpenCode

**Windows:**
```powershell
mkdir C:\Users\NAMA_USER\.config\opencode -Force
```

**Linux/macOS:**
```bash
mkdir -p ~/.config/opencode
```

Lalu buat file `opencode.json`:

**Windows:** `C:\Users\NAMA_USER\.config\opencode\opencode.json`
**Linux:** `~/.config/opencode/opencode.json`

Isi file (sesuaikan path sesuai OS):
```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": "allow",
  "instructions": [
    "FOLDER_MEMORY/VS&OPENCODE/SOUL.md",
    "FOLDER_MEMORY/VS&OPENCODE/USER.md",
    "FOLDER_MEMORY/VS&OPENCODE/AGENTS.md",
    "FOLDER_MEMORY/COMMON/docs/MASTER-MEMORY.md",
    "FOLDER_MEMORY/COMMON/docs/MEMORY-LEARNINGS.md",
    "FOLDER_MEMORY/COMMON/docs/MEMORY-ERRORS.md",
    "FOLDER_MEMORY/PC-06/summary.md",
    "FOLDER_MEMORY/PC-06/facts.md"
  ],
  "plugin": [
    "context-mode"
  ]
}
```

**Contoh path Windows (PC-Advan):**
```json
"instructions": [
  "C:/Users/Advan/Desktop/memory/VS&OPENCODE/SOUL.md",
  "C:/Users/Advan/Desktop/memory/VS&OPENCODE/USER.md",
  "C:/Users/Advan/Desktop/memory/VS&OPENCODE/AGENTS.md",
  "C:/Users/Advan/Desktop/memory/COMMON/docs/MASTER-MEMORY.md",
  "C:/Users/Advan/Desktop/memory/COMMON/docs/MEMORY-LEARNINGS.md",
  "C:/Users/Advan/Desktop/memory/COMMON/docs/MEMORY-ERRORS.md",
  "C:/Users/Advan/Desktop/memory/PC-Advan/summary.md",
  "C:/Users/Advan/Desktop/memory/PC-Advan/facts.md"
]
```

**Contoh path Linux:**
```json
"instructions": [
  "/root/memory/VS&OPENCODE/SOUL.md",
  "/root/memory/VS&OPENCODE/USER.md",
  "/root/memory/VS&OPENCODE/AGENTS.md",
  "/root/memory/COMMON/docs/MASTER-MEMORY.md",
  "/root/memory/COMMON/docs/MEMORY-LEARNINGS.md",
  "/root/memory/COMMON/docs/MEMORY-ERRORS.md",
  "/root/memory/PC-06/summary.md",
  "/root/memory/PC-06/facts.md"
]
```

## 5. Install Context-Mode (Plugin Hemat Token)
```bash
npm install -g context-mode
```

## 6. Setup Git Config (biar pull/push otomatis)
```bash
cd FOLDER_MEMORY
git config user.email "email@kamu.com"
git config user.name "Nama Kamu"
```

## 7. Test
```bash
cd FOLDER_MEMORY
opencode
```

Lalu di dalam opencode, ketik:
- `ctx stats` → cek context-mode aktif
- `/loadmemory` → baca semua memory

## 8. Auto-Pull (Opsional)
Supaya memory selalu update, jalankan sebelum mulai kerja:
```bash
cd FOLDER_MEMORY && git pull
```

---

## Info Penting

| Item | Keterangan |
|------|-----------|
| **GitHub Repo** | `https://github.com/yonathan-boop/OPENCODE` |
| **Token** | Ambil dari server: `git remote get-url origin` (format `https://ghp_XXX@github.com/...`) |
| **Model AI** | `opencode/big-pickle` (JANGAN diganti) |
| **Folder Memory** | `~/Desktop/memory` (Windows) atau `/root/memory` (Linux) |
| **Server Website** | methodist-11.my.id (Cloudflare tunnel) |
| **Bot Telegram** | @Qksusb_bot (di server Linux) |

---

## Yang Dilarang
- ❌ Jangan jalankan Ollama
- ❌ Jangan commit token ke repo (GitHub block push)
- ❌ Jangan ganti model AI dari big-pickle
- ❌ Jangan hapus file permanen tanpa konfirmasi

---

*Terakhir diupdate: 10 September 2026*
