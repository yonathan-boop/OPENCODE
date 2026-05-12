# Memory Learnings

Catatan koreksi, insight, dan pola yang terbukti membantu agar asisten berkembang lintas sesi.

---

## [LRN-20260509-003] jangan_jalankan_ollama

**Tanggal**: 2026-05-09
**Priority**: high
**Status**: active

### Summary
Jangan pernah menjalankan Ollama. User melarang keras.

### Details
- Ollama consume resource berat
- User tidak mau Ollama jalan di PC-nya
- Cari alternatif lain untuk vision/image processing

### Action
- JANGAN install, jalankan, atau restart Ollama
- Untuk vision: cari API gratis atau tool lain (Tesseract OCR, free vision API)
- Kalau butuh vision model, tanya dulu sebelum install apa pun

---

## [LRN-20260422-001] inference_from_short_prompts

**Tanggal**: 2026-04-22
**Priority**: high
**Status**: active

### Summary
User ingin asisten yang bisa memahami instruksi singkat, contoh hasil, dan referensi tanpa perlu dijelaskan panjang berulang-ulang.

### Details
- Jangan menunggu prompt super detail jika arah umum sudah jelas
- Gunakan konteks percakapan dan memory aktif untuk mengambil keputusan terbaik
- Saat ada contoh hasil, gunakan itu sebagai acuan utama untuk style, vibe, dan kualitas output

### Action
- Selalu cek memory sebelum kerja besar
- Saat user memberi contoh, cocokkan keputusan desain / struktur, bukan sekadar menyalin tampilan luar
- Saat instruksi pendek muncul, tafsirkan dengan percaya diri lalu kerjakan

---

## [LRN-20260428-002] Launch GUI Apps di XFCE VNC

**Tanggal**: 2026-04-28
**Priority**: high
**Status**: active

### Summary
Untuk launch GUI app di desktop XFCE yang berjalan di VNC display :1, perlu set variabel environment yang benar.

### Details
- Display: `:1` (port 5901)
- XAuthority: `/data/data/com.termux/files/home/.Xauthority`
- Command: `export DISPLAY=:1 && export XAUTHORITY=/data/data/com.termux/files/home/.Xauthority && remmina &`

### Action
- Selalu pakai export DISPLAY dan XAUTHORITY sebelum launch GUI apps di VNC

---

## [LRN-20260422-002] save_and_read_memory_diligently

**Tanggal**: 2026-04-22
**Priority**: high
**Status**: active

### Summary
Asisten harus rajin membaca memory di awal sesi dan rajin menyimpan hal penting di akhir atau saat ada pembelajaran baru.

### Details
- User sudah menegaskan bahwa AI tidak kuat langsung menangani hal besar tanpa bantuan memory yang disiplin
- Karena itu memory harus diperlakukan sebagai konteks kerja utama, bukan arsip pasif

### Action
- Jalankan pola `load -> kerja -> catat -> save`
- Promosikan pola yang berulang ke `MASTER-MEMORY.md`

---

## [LRN-20260509-004] wajib_pakai_sub_agent_untuk_eksekusi

**Tanggal**: 2026-05-09
**Priority**: high
**Status**: active

### Summary
User menegaskan bahwa semua task eksekusi WAJIB via sub-agent (`task` tool). Otak (main session) hanya boleh planning, strategi, dan catat memory.

### Details
- User protes karena commit/push dilakukan langsung, bukan via sub-agent
- Sub-agent protocol sudah ditetapkan di MASTER-MEMORY.md
- Otak = perencana, sub-agent = eksekutor
- **Yang termasuk tugas otak (boleh langsung):** baca memory, catat memory, planning, strategi, komunikasi dengan user
- **Yang WAJIB sub-agent:** bikin/edit file, run command, commit/push, scraping, batch edit

### Action
- Baca & catat memory → OTAK langsung (butuh full context, gak bisa diringkas)
- Planning → spawn sub-agent → sub-agent eksekusi → otak verifikasi + catat
- Git commit/push → sub-agent
- Coding/file creation → sub-agent
- Sub-agent dikasih instruksi spesifik, gak perlu paham konteks penuh

---

## [LRN-20260509-005] sub_agent_path_specification

**Tanggal**: 2026-05-09
**Priority**: high
**Status**: active

### Summary
Waktu spawn sub-agent untuk git commit/push, WAJIB specify exact working directory. Jangan biarkan sub-agent nebak path.

### Details
- Sub-agent init repo di `C:\Users\Advan\` (root) instead of `C:\Users\Advan\memory\`
- `git add -A` di root nyaris stage ribuan file sampah dari Recycle Bin, AppData, dll
- Untung gak sempat commit, cuma staging — bisa di-clean

### Action
- Selalu set `workdir` parameter dengan path exact
- Untuk push, dua repo wajib:
  - `C:\Users\Advan\Desktop\memory` (shared, remote: GitHub)
  - `C:\Users\Advan\memory` (local daily notes)
- Kalau ragu, spawn sub-agent dedicated khusus push dengan instruksi path lengkap
- Jangan `git add -A` sebelum ls dulu

---

## [LRN-20260512-001] wajib_pakai_todowrite_di_setiap_sesi

**Tanggal**: 2026-05-12
**Priority**: high
**Status**: active

### Summary
User ingin todo list selalu kelihatan di samping (via TodoWrite tool), bukan cuma di file backlog.

### Details
- TodoWrite menampilkan task list di UI — user bisa lihat progres langsung
- User bilang ini sudah pernah dibahas sebelumnya
- BACKLOG.md saja tidak cukup — harus ada todo visible di sesi

### Action
- Setiap sesi, pasang TodoWrite di awal: isi dengan task yang akan dikerjakan
- Update status real-time: pending → in_progress → completed
- Pastikan user bisa lihat: apa yang sudah selesai, apa yang sedang dikerjakan, apa yang akan datang
- Jangan lupa update TodoWrite setelah tiap task selesai

---
