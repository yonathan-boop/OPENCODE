# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## [LRN-20260811-001] cloudflare_named_tunnel_website

**Logged**: 2026-08-11
**Priority**: high
**Status**: active
**Area**: website-infra

### Summary
Website SD Methodist-11 live via Cloudflare NAMED tunnel (token), bukan quick tunnel. Domain methodist-11.my.id → localhost:8090.

### Details
- Install: `pkg install cloudflared` (Termux, v2026.7.3)
- Jalankan: `cloudflared tunnel run --token <TOKEN>` (tunnelID 912a22fa-...)
- Dashboard ingress: methodist-11.my.id → http://localhost:8090, config auto ke-push (cloudflared polling)
- Error 1033 = DNS record bukan CNAME tunnel / hostname tidak ter-ingress
- DNS cache lokal bisa nyimpen NXDOMAIN lama → bypass dengan `--resolve` atau tunggu
- Script trigger: `bash linux-tablet/scripts/start-website.sh` (kata kunci user: "hidupkan website")

### Action
- Simpan token + prosedur di `linux-tablet/docs/WEBSITE-METHODIST11.md`
- JANGAN pakai quick tunnel untuk domain ini

### Metadata
- Source: user_feedback
- Related Files: linux-tablet/docs/WEBSITE-METHODIST11.md, linux-tablet/scripts/start-website.sh
- Tags: cloudflare, tunnel, website, methodist-11

---

## [LRN-20260509-004] heartbeat_skip_saat_kosong

**Logged**: 2026-05-09
**Priority**: high
**Status**: active
**Area**: config

### Summary
HEARTBEAT.md yang kosong menyebabkan heartbeat API call skip. Isi dengan task checklist biar heartbeat aktif.

### Details
- File HEARTBEAT.md ada komentar: "Keep this file empty to skip heartbeat API calls"
- Awalnya kosong → heartbeat gak pernah dikirim
- User kira aku cuma reaktif padahal heartbeat cuma perlu diaktifkan

### Action
- HEARTBEAT.md harus selalu berisi task checklist
- Jangan dikosongin kalau mau heartbeat aktif
- Tetap perlu cek tanggal di setiap chat karena bisa beda hari

### Metadata
- Source: user_feedback
- Tags: heartbeat, config

---
**Logged**: 2026-05-09
**Priority**: high
**Status**: promoted
**Area**: config

### Summary
User ingin asisten yang paham instruksi singkat tanpa perlu dijelaskan panjang.

### Details
- Jangan tunggu prompt detail kalau arah umum sudah jelas
- Gunakan konteks memory untuk ambil keputusan
- Saat ada contoh hasil, jadikan acuan gaya dan kualitas

### Action
- Cek memory sebelum kerja besar
- Saat instruksi pendek, tafsirkan dengan percaya diri

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md, SOUL.md
- Tags: communication, workflow

---

## [LRN-20260509-002] save_and_read_memory_diligently

**Logged**: 2026-05-09
**Priority**: high
**Status**: promoted
**Area**: config

### Summary
Asisten harus rajin baca memory di awal sesi dan rajin simpan hal penting.

### Details
- User menegaskan AI tidak kuat langsung tangani hal besar tanpa memory disiplin
- Memory adalah konteks kerja utama, bukan arsip pasif

### Action
- Jalankan pola load -> kerja -> catat -> save
- Promosikan pola berulang ke MASTER-MEMORY.md

### Metadata
- Source: user_feedback
- Related Files: MEMORY.md, AGENTS.md
- Tags: workflow, memory

---

## [LRN-20260509-003] boundary_readonly_by_default

**Logged**: 2026-05-09
**Priority**: high
**Status**: active
**Area**: config

### Summary
User mengubah aturan: file di luar VS&OPENCODE/ bersifat read-only default, jika ingin diedit harus minta izin dulu.

### Details
- Awalnya: hanya boleh edit VS&OPENCODE/, jangan sentuh folder lain
- Sekarang: read-only default, kalau disuruh user → minta izin dulu baru kerja

### Action
- Sudah diupdate di SOUL.md dan AGENTS.md root + shared

### Metadata
- Source: user_feedback
- Related Files: SOUL.md, AGENTS.md
- Tags: boundary, config

---

