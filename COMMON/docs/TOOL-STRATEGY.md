# Tool Strategy

## Tool Reference

| Kebutuhan | Tool | Catatan |
|-----------|------|---------|
| Cari file by nama | Glob | Paling cepat untuk pattern matching |
| Cari konten by regex | Grep | Untuk search isi file |
| Baca file | Read | Selalu Read, jangan pakai cat/head/tail |
| Edit file | Edit | Exact string replacement |
| Buat file baru | Write | Hanya untuk file baru |
| Eksekusi command | Bash | git, python, npm, dll |
| Web search | WebSearch | Info real-time |
| Web fetch | WebFetch | Baca URL tertentu |
| Tanya user | Question | Jika benar-benar butuh klarifikasi |
| Tracking tugas | TodoWrite | Untuk complex multistep |

## Sub-Agent Triggers (WAJIB)

Gunakan `task` tool (sub-agent) untuk:

### File Operations
- Membuat file baru (Write)
- Mengedit file (Edit)
- Batch read/write banyak file

### Git Operations
- git add, commit, push
- Git pull (tapi untuk pull di awal sesi, otak boleh langsung)

### Batch Operations
- Multiple python/bash commands berurutan
- Operasi yang butuh banyak langkah (>3)

### Complex Multi-step Tasks
- Task yang butuh riset + coding + testing
- Task yang butuh multiple tool calls dalam sequence

## Direct Execution (Otak Langsung)

### Read Operations
- Baca memory files
- Baca kode untuk understanding
- Search/grep/glob

### Planning & Strategy
- Breakdown task
- Pilih tool/sub-agent
- Design solusi

### Communication
- Semua chat dengan user
- Presentasi plan
- Konfirmasi hasil

### Memory Save (Ringan)
- Catat notes pendek
- Update activity log
- Tapi untuk file besar → sub-agent

## Aturan Tool Ordering

1. **Sebelum edit**: Read dulu file yang akan diedit
2. **Sebelum commit**: git status + git diff dulu
3. **Sebelum execute**: Plan dulu, jangan langsung gas
4. **Setelah execute**: Verify hasilnya
5. **Setelah selesai**: Save ke memory

## Anti-Patterns

❌ JANGAN:
- Pakai Bash untuk baca file (Read lebih tepat)
- Pakai Bash untuk search (Grep lebih tepat)
- Langsung edit tanpa Read dulu
- Spawn sub-agent tanpa instruksi path lengkap
- git add -A tanpa ls/staging check dulu
- Reasoning terus setelah task selesai
