# KBBI Keyword Dictionary — Indonesian Intent Recognition

Di-generate: 2026-05-09
Source: KBBI CDN (Naandalist/kbbi-harvester)

## Cara Baca

Kolom KBBI = makna asli dari kamus.
Kolom "Arti buat asisten" = interpretasi ketika kata ini muncul di prompt user.

---

## KATEGORI: PERMINTAAN AKSI (Aksi nyata yang diminta user)

| Kata | KBBI | Arti buat Asisten |
|------|------|------------------|
| **tolong** | bantu: minta bantuan | ✅ LAKUKAN — user butuh sesuatu yang dikerjakan. Prioritas tinggi. |
| **minta** | berkata supaya diberi/mendapat sesuatu; mohon | ✅ LAKUKAN — sinonim "tolong" |
| **perlu** | harus; usah; butuh | ✅ LAKUKAN — ada kebutuhan yang harus dipenuhi |
| **harus** | wajib; mestinya | ✅ LAKUKAN — prioritas tertinggi, ini perintah, bukan saran |
| **suruh** | perintah (supaya melakukan sesuatu) | ✅ LAKUKAN — sinonim "tolong" |
| **bikin** | buat (cakapan) | ✅ BUAT — bikin file, script, dll |
| **buat** | kerjakan; lakukan; bikin | ✅ BUAT — sinonim "bikin" |
| **kerjakan** | melakukan sesuatu; mengerjakan | ✅ LAKUKAN — sinonim "tolong" |
| **selesai** | sudah jadi; habi | ✅ SELESAIKAN — berarti ini tugas, bukan teori |

---

## KATEGORI: PERMINTAAN MEMORY (User ingin sesuatu diingat/catat)

| Kata | KBBI | Arti buat Asisten |
|------|------|------------------|
| **catat** | tulisan sesuatu (dalam kertas dan sebagainya) | 📝 SIMPAN — masukkan ke memory/learning |
| **ingat** | beradi dalam pikiran; tidak lupa / menaruh perhatian; memikirkan | 📝 SIMPAN — sinonim "catat" |
| **mengingat** | menyimpan dalam ingatan; menyuruh ingat | 📝 SIMPAN — sinonim "catat" |
| **jelaskan** | memberikan penjelasan | 📝 SIMPAN — ini permintaan agar assistant memahami/mencatat |
| **tahu** | mengerti; mengenal; memahami | 🔍 PAHAMI — user mau aku "tahu" sesuatu = catat sebagai konteks |
| **temu** | sua; jumpa | 🔍 TEMUKAN — cari sesuatu yang sudah ada |

---

## KATEGORI: KOREKSI / FEEDBACK (User mengoreksi atau memberi tahu kesalahan)

| Kata | KBBI | Arti buat Asisten |
|------|------|------------------|
| **benar** | sesuai seharusnya; betul; tidak salah | ✅ BENAR — aku sudah tepat, lanjutkan |
| **salah** | tidak benar; keliru; khilaf | ❌ SALAH — koreksi! Catat ke ERRORS.md |
| **gak** (enggak) | tidak | ❌ NEGASI — kalimat ini menolak/menolak sesuatu |
| **jangan** | tidak boleh; hendaknya tidak usah | 🚫 LARANGAN — jangan lakukan ini |

---

## KATEGORI: PENCARIAN / PENGECEKAN

| Kata | KBBI | Arti buat Asisten |
|------|------|------------------|
| **cari** | temukan sesuatu | 🔍 CARI — search atau lookup |
| **cek** | periksa | 🔍 CEK — verify, check |
| **temu** | sua; jumpa | 🔍 TEMUKAN — cari yang sudah ada |

---

## KATEGORI: MODIFIER / KUALITAS

| Kata | KBBI | Arti buat Asisten |
|------|------|------------------|
| **ingin** | hendak; mau; berhasrat | 🎯 PREFS — ini preferensi user |
| **perlu** | penting; harus ada | 🎯 PREFS — ini kebutuhan penting |
| **ubah** | tukar; ganti | ✏️ EDIT — ada yang perlu diubah |
| **hapus** | hilangkan; musnahkan | 🗑️ DELETE — hapus sesuatu |

---

## Aturan Inferensi Tambahan

### Pola Kalimat yang Sering Muncul

1. **"tolong X" / "bisa tolong X" / "tolong dong X"**
   → ✅ LAKUKAN X — prioritas tinggi

2. **"bikin X" / "buat X" / "aku mau X"**
   → ✅ BUAT X — buat file, script, fitur baru

3. **"catat X" / "ingat X" / "X tolong diingat"**
   → 📝 SIMPAN X ke memory

4. **"jelaskan X" / "apa itu X"**
   → 📝 SIMPAN konteks + jelaskan

5. **"salah X" / "bukan X" / "X seharusnya Y"**
   → ❌ KOREKSI — catat ke ERRORS.md

6. **"jangan X" / "gak usah X" / "jangan repot-repot"**
   → 🚫 SKIP — jangan lakukan X

7. **"terusin X" / "lanjutkan X"**
   → 🔄 LANJUTKAN — lanjutkan tugas sebelumnya

### Negation Detection

Kata "gak", "jangan", "bukan", "tidak", "nggak" di awal kalimat = negasi.
Kalau kalimat sebelumnya sudah aku interpretasi, negasi ini membalikkan maksud.

Contoh:
- "bikin script buat X" → ✅ BUAT script X
- "gak, bikin script buat Y" → ✅ BUAT script Y (yang sebelumnya X dibatalkan)

---

## Notes

- KBBI adalah kamus resmi. Jadi kalau ragu, cek dulu makna asli kata.
- User sering pakai "tolong" berkali-kali untuk minta sesuatu. Ini sinyal kuat bahwa ada aksi yang perlu dilakukan.
- Kata "ingin" dan "perlu" sering muncul sebagai prefiks: "ingin dicatat", "perlu diingat" → masukkan ke memory.
- Selalu prioritaskan konteks conversation di atas keyword matching. Kalau konteksnya jelas, keyword hanya sebagai backup.