# Memory Feature Requests

Catatan kemampuan baru yang diminta user agar sistem memory dan asisten berkembang.

---

## [FEAT-20260917-001] autonomous_self_learning_mode

**Tanggal**: 2026-09-17
**Priority**: high
**Status**: active

### Requested Capability
User minta AI (di PC dan di server) bisa "berjalan sendiri" — proaktif belajar & mengembangkan diri pakai akses internet, sambil terus membantu user makin banyak hal ke depannya.

### User Context (PENTING — arah final, 17/9)
- **Server Linux (24/7) SUDAH disuruh user belajar mandiri sendiri.** JANGAN bikin/pasang konfigurasi self-learn untuk server dari PC ini — itu domain server.
- Mode mandiri di sini = untuk **PC lokal (yonat-PC)** saja, waktu-nya terbatas (PC dimatikan), makanya porsi belajar server > porsi PC.
- **PC & server harus SALING MELENGKAPI, bukan menimpa.** Hindari menulis catatan/job yang menimpa atau mengubah konfigurasi belajar mandiri yang sudah jalan di server.
- Acuan belajar: histori kerja (git history memory, MASTER-MEMORY, LEARNINGS, todo backlog).
- User eksplisit: kalau context hampir habis → catat dulu (save memory), baru spawn sub-agent baru yang lanjut.

### Batas & Realita
- AI reaktif: nggak punya "keinginan" sendiri; semua langkah tetap butuh trigger/izin. Inisiatif = menyarankan & langsung jalan pakai tool saat user setuju.
- Aksi eksternal (email, post, pesan ke orang lain) tetap WAJIB izin (red line).
- Web research / baca artikel / scrape info → boleh proaktif saat sudah diizinkan.

### Batas Implementasi di PC (local only)
1. Awal sesi: baca histori + backlog → awasi apa yang sedang dikerjakan server (cek recent activity/komit) → pilih topik belajar yang melengkapi, BUKAN duplikat.
2. Kalau user idle/izinkan → riset web, verifikasi, simpan insight ke MEMORY-LEARNINGS (append, jangan rewrite file).
3. Tiap ±3 task: cek context usage; kalau >70% → simpan lengkap ke memory, spawn sub-agent lanjutan.
4. Selalu git pull sebelum edit memory & commit+push setelahnya, supaya nggak konflik sama tulis-menulis memory dari server.
5. Jangan pernah aksi eksternal tanpa izin; jangan bocor data pribadi.

---

## [FEAT-20260422-001] smarter_assistant_memory_mode

**Tanggal**: 2026-04-22
**Priority**: high
**Status**: active

### Requested Capability
Asisten yang lebih natural, lebih manusiawi, lebih pintar menangkap maksud, dan lebih kuat mengikuti contoh hasil yang disukai user.

### User Context
User sering malas mengulang prompt panjang. User ingin AI yang bisa bekerja lebih seperti partner yang cepat paham arah, terutama untuk coding, UI, landing page, dan revisi desain.

### Suggested Implementation
- simpan profil perilaku asisten di memory
- simpan preferensi visual user
- baca memory di awal sesi
- catat koreksi, error, dan pola yang berhasil ke log pembelajaran
- promosikan pola penting ke `MASTER-MEMORY.md`

---
