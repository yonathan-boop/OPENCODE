# LINUX-HP — Memory System (Termux Android, Xiaomi)

Di-update: 10 Agustus 2026 (fresh install Termux Android + OpenClaw + opencode)

---

## 📋 Identitas

- **Nama:** linux-hp (Termux Android di HP Xiaomi)
- **OS:** Android 16, kernel 6.6.89-android15, arch aarch64
- **Device:** Xiaomi 2412DPC0AG (Redmi Note series tipe)
- **Lokasi:** /data/data/com.termux/files/home
- **Path:** /data/data/com.termux/files/usr/bin/opencode
- **opencode:** v1.18.16 (terminal UI, built-in provider)
- **Node.js:** v26.4.0 (via Termux Node.js, bukan Windows)
- **Git:** 2.55.0
- **Python:** 3.14.6
- **Bun:** terinstal via npm
- **Cargo/Rust:** terinstal via npm (toolchain)
- **OpenClaw:** 2026.7.1-2 (via npm + glibc, tidak membutuhkan proot-distro)

---

## 📋 Environment Detail

### Storage
- **Total:** 479 GB (filesystem /data/data/com.termux/files/home)
- **Available:** 151 GB
- **No proot-distro required** (Termux natif)
- **OpenClaw:** tidak membutuhkan Linux (melalui glibc loader)

### Installed Tools (Termux)
```bash
# Git
git version 2.55.0

# Node.js
node v26.4.0 (via Termux Node)

# Python
python 3.14.6

# Bun
bun (terinstal)

# Cargo (Rust toolchain)
cargo (terinstal)

# LLVM / Clang
clang 21.0.0 (via Termux)

# npm
npm@11.19.0
npm global: openclaw@2026.7.1-2

# opencode
opencode v1.18.16

# Tools: curl, wget, jq, sqlite3, ffmpeg, etc.
# Plus: core (DevCoreX), openclaw (npm global)
```

### OpenClaw
- **Status:** ✅ Terinstall (openclaw 2026.7.1-2)
- **Path:** /data/data/com.termux/files/usr/bin/openclaw (symlink)
- **Glibc node:** /data/data/com.termux/files/usr/glibc/lib/ld-linux-aarch64.so.1
- **Bin path:** ~/.openclaw-android/bin (glibc wrapper)
- **Status:** `openclaw --version` → 2026.7.1-2

---

## 📋 Memory System (Linux-HP)

### Memori Lokal
- **Folder memory:** /root/memory-linux-hp (legacy, sekarang di `~/OPENCODE`)
- **Repo:** https://github.com/yonathan-boop/OPENCODE

### Trigger Commands
```bash
# Load Memory (awal sesi)
cd ~/OPENCODE && git pull

# Save Memory (akhir sesi)
cd ~/OPENCODE && git add . && git commit -m "update" && git push

# Quick status
cd ~/OPENCODE && git status
```

### Key Files
- `~/OPENCODE/VS&OPENCODE/IDENTITY.md` — AI identitas
- `~/OPENCODE/VS&OPENCODE/USER.md` — Pengguna (Advan/PC)
- `~/OPENCODE/COMMON/docs/MASTER-MEMORY.md` — Memory utama
- `~/OPENCODE/PC-06/summary.md` — PC-06 summary
- `~/OPENCODE/PC-06/facts.md` — Fakta PC-06
- `~/OPENCODE/linux-hp/docs/setup.md` — Setup linux-hp (di sini)
- `~/OPENCODE/linux-tablet/docs/setup.md` — Setup linux-tablet (referensi)

---

## 📋 Cara Kerja

1. cd ~/OPENCODE
2. git pull (ambil data terbaru dari GitHub)
3. Baca semua file .md di COMMON/docs, PC-06, PC-Advan
4. Gabungkan jadi konteks kerja
5. Simpan ke memory (git push)

---

## 📋 Aturan

- WAJIB load memory di awal sesi (cd ~/OPENCODE && git pull)
- WAJIB save memory di akhir sesi (cd ~/OPENCODE && git add . && git commit -m "update" && git push)
- Semua error/keputusan WAJIB dicatat
- **Dengan OpenClaw:**
  - Tidak perlu proot-distro (melalui glibc loader)
  - Buka openclaw: `openclaw`
  - Gunakan `opencode` setelah `openclaw`
  - Mode gateway tersedia: `openclaw gateway`
  - Key OpenRouter untuk provider: `OPENROUTER_API_KEY` di env

---

## 📋 Note

- **Nama model:** `opencode/ling-3.0-tiny-free` (OpenRouter model)
- **Provider:** openrouter (API Key: `sk-or-v1-...` via ~/.local/share/opencode/auth.json)
- **Session:** opencode model di-configurasi via `opencode.jsonc` → `model: opencode/ling-3.0-tiny-free`
- **OpenClaw:** gateway mode local (localhost:19001) tersedia di `openclaw configure`

---

## 📋 Update Riwayat

- 10 Agustus 2026 — Fresh install Termux + OpenClaw + opencode 1.18.16
- Device: Xiaomi 2412DPC0AG, Android 16 (aarch64)
- opencode v1.18.16 (via core-termux / npm)
- OpenClaw 2026.7.1-2 (via glibc node)
- OpenRouter key: `sk-or-v1-...` (dikonfigurasi via auth.json)
