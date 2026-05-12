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

## Sub-Agent Optimization

### Kapan SPAM sub-agent (boleh banyak)
- Setiap git commit/push — 1 sub-agent per commit
- Setiap batch command — 1 sub-agent per batch
- Setiap file write — 1 sub-agent per file (bisa parallel)

### Kapan TUNGGU sub-agent selesai
- Kalau step selanjutnya depend pada hasil sub-agent sebelumnya
- Contoh: copy file → update script → run script (harus sequential)

### Kapan PAKAI 1 sub-agent untuk banyak hal
- Kalau semua langkah sequential dan saling depend
- Contoh: dup file → update path → run absensi → restore path (1 sub-agent)

### Kapan SUB-AGENT GA PERLU
- 1-2 bash commands sederhana
- Read-only operations
- Planning/strategy doang
- Chat sama user

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
- Spawn sub-agent untuk hal trivial (1 bash command sederhana)
- Over-explain context ke sub-agent — beri instruksi minimal & jelas
