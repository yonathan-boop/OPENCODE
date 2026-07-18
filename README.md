# Memory System — Petunjuk Penggunaan

## Overview

Sistem memory ini memungkinkan AI (opencode) untuk "ingat" semua konteks dari sesi sebelumnya. Setiap kali session baru dimulai, AI akan otomatis load semua memory dari GitHub.

## Lokasi Memory

- **Folder:** `C:\Users\yonat\OneDrive\Desktop\memory`
- **GitHub:** https://github.com/yonathan-boop/OPENCODE

## Cara Kerja

### 1. Auto-Load (Otomatis)

Saat kamu buka opencode baru dan ketik "halo" atau sapaan lainnya, AI akan otomatis:

1. Git pull dari GitHub (ambil data terbaru)
2. Baca semua file memory
3. Lapor "Memory loaded!"

### 2. Manual Commands

| Command | Fungsi |
|---------|--------|
| `/loadmemory` | Git pull + baca semua memory |
| `/savememory` | Commit + push ke GitHub |
| `/ingat "isi"` | Catat ke MASTER-MEMORY.md |
| `/status` | Cek git status |

## Struktur Folder

```
memory/
├── COMMON/
│   ├── docs/           # Dokumentasi umum
│   │   ├── MASTER-MEMORY.md      # Memory utama
│   │   ├── MEMORY-LEARNINGS.md   # Pembelajaran
│   │   ├── MEMORY-ERRORS.md      # Error yang perlu dihindari
│   │   └── MEMORY-FEATURE-REQUESTS.md
│   └── scripts/        # Script Python
├── PC-06/
│   ├── docs/           # Session logs & absensi
│   ├── summary.md      # Ringkasan PC
│   └── facts.md        # Fakta user
├── VS&OPENCODE/
│   ├── SOUL.md         # Identitas AI
│   ├── USER.md         # Profil user
│   ├── AGENTS.md       # Protokol kerja
│   ├── AGENTS-GLOBAL.md # Backup global config
│   └── opencode-config.jsonc # Backup config
└── README.md           # File ini
```

## Setup di PC Baru

### 1. Install Git

```powershell
winget install Git.Git
```

### 2. Clone Memory

```powershell
cd C:\Users\YO-NAMA\OneDrive\Desktop
git clone https://github.com/yonathan-boop/OPENCODE.git memory
```

### 3. Setup Config

Buat file `~/.config/opencode/AGENTS.md` dengan isi:

```markdown
# AGENTS.md — Global Instructions

## Session Startup — WAJIB

Saat session baru dimulai, ATAU saat user ketik "halo", "hai", "hello", atau sapaan lainnya:

1. **Git pull memory:**
   ```
   cd C:\Users\YO-NAMA\OneDrive\Desktop\memory && git pull
   ```

2. **Baca file berikut secara berurutan:**
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\VS&OPENCODE\SOUL.md`
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\VS&OPENCODE\USER.md`
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\VS&OPENCODE\AGENTS.md`
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\COMMON\docs\MASTER-MEMORY.md`
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\COMMON\docs\MEMORY-LEARNINGS.md`
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\COMMON\docs\MEMORY-ERRORS.md`
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\PC-06\summary.md`
   - `C:\Users\YO-NAMA\OneDrive\Desktop\memory\PC-06\facts.md`

3. **Set todo panel** dari `VS&OPENCODE/.learnings/TODO-STATE.md`

4. **Lapor ke user:** "Memory loaded!" + ringkasan singkat
```

### 4. Setup Config JSON

Buat file `~/.config/opencode/opencode.jsonc`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\VS&OPENCODE\\SOUL.md",
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\VS&OPENCODE\\USER.md",
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\VS&OPENCODE\\AGENTS.md",
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\COMMON\\docs\\MASTER-MEMORY.md",
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\COMMON\\docs\\MEMORY-LEARNINGS.md",
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\COMMON\\docs\\MEMORY-ERRORS.md",
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\PC-06\\summary.md",
    "C:\\Users\\YO-NAMA\\OneDrive\\Desktop\\memory\\PC-06\\facts.md"
  ]
}
```

**Ganti `YO-NAMA` dengan username Windows kamu.**

## Troubleshooting

### AI tidak load memory?

1. Pastikan Git sudah terinstall: `git --version`
2. Pastikan folder memory ada: `dir C:\Users\YO-NAMA\OneDrive\Desktop\memory`
3. Test git pull manual: `cd C:\Users\YO-NAMA\OneDrive\Desktop\memory && git pull`
4. Restart opencode

### Git pull gagal?

1. Cek koneksi internet
2. Cek apakah token GitHub masih valid
3. Kalau token expired, generate baru di GitHub Settings → Developer settings → Personal access tokens

### AI lupa konteks?

1. Ketik `/loadmemory` untuk reload
2. Atau ketik "catat [isi]" untuk simpan ke memory

## Sub-Agent Protocol

- **Otak (main session):** Planning, strategi, baca/simpan memory, chat
- **Sub-agent (task tool):** Edit/buat file, git commit/push, run script

Selalu spawn sub-agent untuk eksekusi berat, otak fokus planning.

## Red Lines

- Jangan bocorkan data pribadi
- Jangan aksi eksternal tanpa izin
- Jangan hapus file permanent tanpa konfirmasi

---

*Terakhir diupdate: 18 Juli 2026*
*Repo: https://github.com/yonathan-boop/OPENCODE*
