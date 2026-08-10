# Facts Database - linux-hp

Fakta-fakta penting tentang linux-hp (Termux Android) yang harus diingat:

## Personal
- Nama device: linux-hp (HP Xiaomi)
- Device: Xiaomi 2412DPC0AG
- OS: Android 16, kernel 6.6.89-android15, aarch64
- Home: /data/data/com.termux/files/home

## Technical
- Termux natif, TIDAK pakai proot-distro
- OpenClaw via glibc node (~/.openclaw-android/), tanpa Linux full
- opencode v1.18.16, path: /data/data/com.termux/files/usr/bin/opencode
- Node glibc: ~/.openclaw-android/bin/node (wrapper)
- Storage: 479 GB total, ~151 GB available

## GitHub
- Repo: https://github.com/yonathan-boop/OPENCODE
- Akses: ~/OPENCODE (sudah di-clone)
- Token: (tersimpan, JANGAN di-commit)

## OpenRouter
- Provider: openrouter
- Key tersimpan di: ~/.local/share/opencode/auth.json
- Model default: opencode/ling-3.0-tiny-free (free)
- Config: ~/.config/opencode/opencode.jsonc
- JANGAN commit key ke repo!

## Preferences
- Bahasa utama: Indonesia
- Model AI: openrouter/opencode (free model)
- User suka instruksi singkat, hasil clean

## Pesan Penting dari User
- "rajin mencatat dan membaca di memori, tolong di simpan ya"
- Memory wajib disimpan di akhir sesi

## Projects
- Memory system: Sinkronisasi via GitHub
- OpenClaw: gateway local mode
- opencode: AI coding assistant (model openrouter)

## OpenClaw
- Version: 2026.7.1-2
- Install: npm global via glibc node (--ignore-scripts)
- Gateway mode: local (localhost:19001)
- Bin: /data/data/com.termux/files/usr/bin/openclaw
- Jangan pakai npm Termux langsung (gagal di tree-sitter-bash)
