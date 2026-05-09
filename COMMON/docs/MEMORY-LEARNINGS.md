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

### Action
- Planning → spawn sub-agent → sub-agent eksekusi → otak terima hasil
- Git commit/push → sub-agent yang jalanin
- Coding/file creation → sub-agent yang jalanin
- Semua command yang bukan memory/planning → sub-agent

---
