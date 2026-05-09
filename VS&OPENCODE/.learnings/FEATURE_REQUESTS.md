# Feature Requests

Capabilities requested by the user.

---

## [FEAT-20260509-003] session_summary_on_startup

**Logged**: 2026-05-09
**Priority**: high
**Status**: implemented
**Area**: behavior

### Requested Capability
Setiap awal sesi chat, assistant kasih tau "terakhir ngapain" — ringkasan aktivitas sesi sebelumnya agar user tahu mau lanjut yang sama atau mulai baru.

### User Context
User capek harus ngulang konteks. Ingin assistant langsung kasih recap singkat di awal sesi.

### Implementation
Tambahkan section "## Yang sudah dilakukan" + "## Yang masih terbuka" di awal respons pertama tiap sesi.

### Metadata
- Frequency: repeated_demand — user minta 2x karena pertama kali aku gak ngerti
- Root Cause: "tolong" yang diulang berkali-kali tidak trigger inference sebagai "minta dilog/catat"
- Related Features: self_improving_agent

---

## [FEAT-20260509-003] kbbi_keyword_inference

**Logged**: 2026-05-09
**Priority**: high
**Status**: implemented
**Area**: behavior

### Requested Capability
Sistem inferensi berbasis KBBI — assistant harus punya pemahaman berbasis kamus untuk mengenali intent user dari kata-kata kunci bahasa Indonesia, bukan asal tebak.

### User Context
User kecewa karena assistant gagal memahami "tolong" yang diulang berkali-kali sebagai sinyal untuk menyimpan/mengingat sesuatu. User bilang: "download kamus besar bahasa indonesia setiap ada kata tertentu itu artinya mau minta di ingat atau catat."

### Implementation
1. Buat `.learnings/KBBI-KEYWORD-DICT.md` — dictionary mapping kata KBBI ke intent
2. Kategori: REQUEST (aksi), MEMORY (simpan), CORRECTION (koreksi), SEARCH (cari), MODIFIER (kualitas)
3. Include pola kalimat umum dan negation detection
4. Baca di awal sesi sebagai konteks

### Keywords yang Ku涵进来:
- tolong, minta, perlu, harus, suruh, bikin, buat → ✅ LAKUKAN
- catat, ingat, ingatkan, jelaskan, ingin → 📝 SIMPAN ke memory
- salah, gak, jangan → ❌ KOREKSI / 🚫 LARANGAN
- cari, cek, temu → 🔍 CARI
- ingin, perlu → 🎯 PREFERENSI
- ubah, hapus → ✏️ EDIT / 🗑️ DELETE

### Metadata
- Frequency: first_time
- Source: KBBI CDN via jsDelivr (Naandalist/kbbi-harvester)
- Related Features: session_summary_on_startup

---

## [FEAT-20260509-001] self_improving_agent

**Logged**: 2026-05-09
**Priority**: high
**Status**: implemented
**Area**: config

### Requested Capability
Self-learning system — kemampuan untuk belajar dari pengalaman lintas sesi.

### User Context
User lihat openclaw punya self-improving agent skill dan ingin sistem yang sama di VS Code instance.

### Complexity Estimate
simple

### Suggested Implementation
Buat `.learnings/` directory dengan 3 file: LEARNINGS.md, ERRORS.md, FEATURE_REQUESTS.md. Migrasi data dari COMMON/docs. Integrasi workflow ke AGENTS.md.

### Metadata
- Frequency: first_time
- Related Features: memory_system

---

