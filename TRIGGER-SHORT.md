=================================================================================
INIT MEMORY SYSTEM - WAJIB JALANKAN DI AWAL SETIAP SESI
=================================================================================

CARAKERJA:
1. Deteksi folder memory aktif:
   - pc-06 (kerja): C:\Users\Admin\Desktop\memory
   - PC-Advan (rumah): C:\Users\Advan\Desktop\memory
   - linux-hp: /root/memory-linux-hp
   - linux-tablet: /data/data/com.termux/files/home/Desktop/New Folder/memory
2. cd ke folder memory aktif
3. git pull (ambil data terbaru dari GitHub)
4. Baca semua file .md di: COMMON/docs, PC-06, PC-Advan, linux-tablet/docs
5. Baca juga log pembelajaran:
   - MEMORY-LEARNINGS.md
   - MEMORY-ERRORS.md
   - MEMORY-FEATURE-REQUESTS.md
6. Gabungkan jadi konteks kerja
7. Laporkan ke user: "Memory loaded!" + ringkasan aktif

=================================================================================
TRIGGER COMMANDS
=================================================================================

/loadmemory      → git pull + baca semua memory (AWAL SESI)
/savememory      → commit + push semua perubahan ke GitHub (AKHIR SESI)
/ingat "isi"    → catat hal penting ke MASTER-MEMORY.md
/status          → cek status git dan commit terbaru

=================================================================================
PERILAKU ASISTEN (WAJIB DIINGAT)
=================================================================================

SAAT AWAL SESI:
- Baca memory dulu sebelum kerja besar
- Langsung kerja jika instruksi sudah jelas

SAAT INTERAKSI:
- Pahami maksud dulu, jangan banyak Tanya
- Jika ada referensi/contoh hasil, gunakan sebagai acuan utama
- Jika instruksi pendek/ambigu, tafsirkan sendiri dan kerjakan
- Utamakan hasil jadi, bukan teori panjang
- Respons ringkas dan natural

SAAT AKHIR SESI:
- Simpan semua perubahan ke memory
- Catat pembelajaran/error jika ada
- Push ke GitHub

=================================================================================
KONTAK LANJUT:Jika ada pertanyaan tentang sistem ini, cek MASTER-MEMORY.md
=================================================================================
