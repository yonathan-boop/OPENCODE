# ARSIP ABSENSI MURID (Historis 2026)

Arsip detail absensi harian dari MASTER-MEMORY (dipindahkan 15 September 2026 supaya file inti ringan).
Yang dibutuhkan tiap sesi (mapping aktif, file terbaru, kasus khusus) tetap ada di MASTER-MEMORY.md.
Untuk rekap bulanan otomatis: `python3 COMMON/scripts/rekap_absensi.py`

---

## 📋 ABSENSI MURID (PC-06)

### Script
- File: absensi.py
- Lokasi: C:/Users/yonat/OneDrive/Desktop/memory/COMMON/scripts/absensi.py
- FILE_PATH saat ini: Absensi 14 September 2026 Monday 09_09_04.xlsx

### Struktur Excel Absensi (Format Baru)
- Setiap sheet = satu kelas (TKa, TKB1, TKB(2), Absen PG)
- Row 7+ = data murid, Kolom 3 = nama
- Row 6 = header tanggal (Juli 1 = col 4, Juli 2 = col 5, dst)
- Tidak ada sheet 'Data'

### Cara Pakai
```
py absensi.py <nama> <kelas> <tanggal> <alasan>
```

### Absensi 1, 3, 4 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 1/8 | PG | Eireen Lorenzo (disebut "Irene") | I |
| 3/8 | PG | Kimita Dessyana Meisim | I |
| 4/8 | PG | Kimita Dessyana Meisim | I |
| 1/8 | TKa | Matthew Batara Hamonangan Nainggolan | I |
| 3/8 | TKa | Rizky Alfonzo Siregar | S |
| 3/8 | TKa | Ellena Clarissa Toh (disebut "Elena") | S |
| 1/8 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 1/8 | TKB(2) | Celine Grace Zhang | S |
| 1/8 | TKB(2) | Jocelyn Marcella Su (disebut "Yoselyn") | S |
| 3/8 | TKB(2) | Celine Grace Zhang | S |
| 3/8 | TKB(2) | Rui Reynara Shen | S |
| 3/8 | TKB(2) | Keyla Toshiro | S |
| 3/8 | TKB1 | Aletta Felicia Siburian (disebut "Alleta") | A |
| 4/8 | TKB1 | Aletta Felicia Siburian | S |
| 1/8 | TKB1 | Kenzo Ichigo Susantio | S |
| 1/8 | TKB1 | Amora Felicya Situmrang | S |
| 1/8 | TKB1 | Clayton Moliver Tan | S |

### Absensi 6 Agustus 2026 (backfill)

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 6/8 | TKa | Lionel Oscar Hu | S |
| 6/8 | TKB1 | Richelcia Wijaya (disebut "Richele") | S |
| 6/8 | TKB1 | Kayyvant Boido Bona Sinaga (disebut "Kayvant") | I |

### Absensi 7 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 7/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 7/8 | TKB2 | Shelomitha Eliora Simanjuntak (disebut "Shelomita") | S |
| 7/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 7/8 | TKa | Ezequiel Levin Chai | S |
| 7/8 | TKa | Sharren Eliana Simanjuntak (disebut "Sharene") | I |

### Absensi 10 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 10/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 10/8 | PG | Leonil Albert Toh | S |
| 10/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 10/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 10/8 | TKa | Mikaylo Zionathan Girsang (disebut "Mikayla") | S |

### Absensi 11 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 11/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 11/8 | TKB(2) | Jayoti Marnida Haulian Kaur | I |
| 11/8 | TKa | Ruby Reynara Shen | S |
| 11/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 11/8 | TKa | Mikaylo Zionathan Girsang | S |
| 11/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 11/8 | TKB1 | Aletta Felicia Siburian (disebut "Alleta") | S |

### Absensi 12 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 12/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 12/8 | PG | Stefano Benedict Imanuel (disebut "Stevano") | I |
| 12/8 | PG | Axelle Sean Chandra (disebut "Axele") | I |
| 12/8 | TKB2 | Ferencia Lu | S |
| 12/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 12/8 | TKa | Carencya Chailinskie (disebut "Carenya") | S |
| 12/8 | TKa | Axelle Tiandra Ong (disebut "Axell") | S |
| 12/8 | TKa | Mikaylo Zionathan Girsang | S |
| 12/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |

### Absensi 13-15 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 13/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 13/8 | TKa | Mikaylo Zionathan Girsang | S |
| 13/8 | TKa | Axelle Tiandra Ong | S |
| 13/8 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 13/8 | TKB1 | Lucas Helsinki Sijabat | I |
| 14/8 | TKa | Valerie Sharon Nainggolan | S |
| 14/8 | TKa | Axelle Tiandra Ong | S |
| 15/8 | PG | Axelle Sean Chandra | I |
| 15/8 | PG | Dareen Chandra | I |
| 15/8 | TKa | Brielle Claire Arinauli Pardosi | S |
| 15/8 | TKa | Valerie Sharon Nainggolan | S |

### Absensi 18-19 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 18/8 | PG | Axelle Sean Chandra | I |
| 18/8 | PG | Eireen Lorenzo | S |
| 18/8 | TKa | Edbert Reynaldo Lim | S |
| 18/8 | TKB(2) | Liora Eliana Panjaitan | S |
| 18/8 | TKB(2) | Willian Geoffrey Utama | S |
| 18/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 18/8 | TKB1 | Richelcia Wijaya | S |
| 19/8 | PG | Nathanael Alessandro Buaya | S |
| 19/8 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 19/8 | TKa | Edbert Reynaldo Lim | S |
| 19/8 | TKa | Chesa Efrata Ronatio Tampubolon | I |
| 19/8 | TKa | Axelle Tiandra Ong | S |
| 19/8 | TKB(2) | Liora Eliana Panjaitan | S |
| 19/8 | TKB(2) | Willian Geoffrey Utama | S |
| 19/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 19/8 | TKB1 | Richelcia Wijaya | S |
| 19/8 | TKB1 | Venedict Sky Lou | S |

- **KIMITA KELUAR SEKOLAH (10 Agustus 2026):** Kimita Dessyana Meisim (PG) resmi keluar dari sekolah → row-nya dihapus dari roster PG di versi file terbaru (arsip tetap ada di file versi lama). Jangan cari/mark Kimita lagi.
- Nama murid dicocokkan fonetik: Mikayla→Mikaylo Zionathan Girsang (TKa)
- File versi terbaru: Absensi 19 Agustus 2026 Tuesday 08_00_00.xlsx
- Nama murid dicocokkan fonetik: Irene→Eireen, Elena→Ellena, Alleta→Aletta, Yoselyn→Jocelyn, Richele→Richelcia, Kayvant→Kayyvant, Shelomita→Shelomitha, Sharene→Sharren, Stevano→Stefano Benedict Imanuel, Axele→Axelle Sean Chandra, Carenya→Carencya Chailinskie, Axell→Axelle Tiandra Ong
- Rantai versi: v-tgl-1 (8) → v-tgl-3 (15) → v-tgl-4 (17) → v-tgl-5 → v-tgl-7 → v-tgl-10 → v-tgl-11 (7 mark) → v-tgl-12 (9 mark) → v-tgl-15 (11 mark) → v-tgl-19 (17 mark18-19) → v-tgl-21 (19 mark20-21) → v-tgl-22 (8 mark22) → v-tgl-24 (VERSI TERBARU, 3 mark24). ABSENSI Agustus.xlsx = v1.0 kosong.
- Format nama versi: tgl dulu baru bulan, jam_menit_detik = waktu asli (mis. "Absensi 4 Agustus 2026 Tuesday 10_04_37.xlsx").

### Absensi 20-21 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 20/8 | PG | Nathanael Alessandro Buaya | S |
| 20/8 | PG | Erick Raphael Nasution | S |
| 20/8 | TKa | Edbert Reynaldo Lim | S |
| 20/8 | TKa | Axelle Tiandra Ong | S |
| 20/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 20/8 | TKB1 | Coryn Aurora Zhan | S |
| 20/8 | TKB1 | Venedict Sky Lou | S |
| 20/8 | TKB1 | Melvin Panca Sihombing | S |
| 20/8 | TKB(2) | Darren Elvano | S |
| 20/8 | TKB(2) | Lishaalini Krisna Naidu | S |
| 20/8 | TKB(2) | Liora Eliana Panjaitan | S |
| 20/8 | TKB(2) | Willian Geoffrey Utama | S |
| 21/8 | PG | Nathanael Alessandro Buaya | S |
| 21/8 | PG | Erick Raphael Nasution | S |
| 21/8 | TKa | Axelle Tiandra Ong | S |
| 21/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 21/8 | TKB(2) | Shane Michael Lienardie | S |
| 21/8 | TKB(2) | Damian Almero Chen | S |
| 21/8 | TKB(2) | Ferencia Lu | S |

- File versi terbaru: Absensi 21 Agustus 2026 Friday 12_44_43.xlsx (12 mark tgl 20 + 7 mark tgl 21)
- Nama mapping baru (konfirmasi user): "Eric"→Erick Raphael Nasution (PG), "Coryn"→Coryn Aurora Zhan (TKB1; HATI-HATI ada juga Corin Falove Manurung di TKB1 — 2 nama mirip 1 kelas), "Valencia"→**Ferencia Lu** (TKB2, user salah sebut Valencia), "Daren Elvano"→Darren Elvano (TKB2), "Lisahalini"→Lishaalini Krisna Naidu (TKB2), "Shane"→Shane Michael Lienardie, "Damian"→Damian Almero Chen
- Catatan: Darren Elvano & Lishaalini sekarang di TKB(2) (naik kelas dari TKa tahun ajaran lalu); murid baru terdeteksi di roster: Shane Michael Lienardie, Damian Almero Chen, Coryn Aurora Zhan, Erick Raphael Nasution

### Absensi 22 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 22/8 | PG | Nathanael Alessandro Buaya | S |
| 22/8 | PG | Erick Raphael Nasution | S |
| 22/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 22/8 | TKa | Carencya Chailinskie | I |
| 22/8 | TKa | Axelle Tiandra Ong | S |
| 22/8 | TKa | Hugo Chavez Tarigan | I |
| 22/8 | TKB(2) | Ferencia Lu | S |
| 22/8 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |

- File versi terbaru: Absensi 22 Agustus 2026 Saturday 10_00_52.xlsx (8 mark, validasi lulus)
- Mapping hari ini: "Varencya"→Ferencia Lu (pola sama dgn "Valencia"), "Hugo"→Hugo Chavez Tarigan (TKa) — pertama kali tercatat
- **ROSTER DISINKRONKAN** dengan `DAFTAR MURID T.P.2026-2027 lengkap.xlsx` (folder `PC-06/docs/Absensi T.P 2025-2026/`): TKa (33) & TKB(2) (25) identik; **Kayla Hosanna Charissa Sihombing** (TKB1 r11) DIHAPUS dari absensi — tidak ada di daftar resmi & tanpa mark; Kimita tetap tidak masuk (sudah keluar); urutan PG beda dikit (Dareen paling bawah) — dibiarkan aman
- Prinsip user (22/8): update nama TIDAK BOLEH menggeser mark antar murid — rename selalu in-place per nama, jangan insert/delete row di tengah list

### Absensi 24 Agustus 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 24/8 | TKa | Carencya Chailinskie | I |
| 24/8 | TKB1 | Kayyvant Boido Bona Sinaga | S |
| 24/8 | TKB1 | Venedict Sky Lou | S |

- File versi terbaru: Absensi 24 Agustus 2026 Monday 09_01_05.xlsx (3 mark, validasi lulus — verifikasi ganda otak+sub-agent)
- **KOREKSI MAPPING KOLOM (24/8):** workbook versi Agustus ini SATU blok bulan saja — header `r5c4="Agustus"`, hari 1–31 di kolom 4–34 → tanggal d = kolom 3+d (24/8 = kolom 27). Catatan lama "Juli 1 = col 4 → Agustus 1 = col 35" HANYA berlaku untuk file era Juli (ABSENSI Juli.xlsx). absensi.py resolve via header row 6 jadi tetap akurat; validasi manual harus pakai kolom 3+d.

### Absensi 5 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 5/9 | TKB(2) | Willian Geoffrey Utama | S |
| 5/9 | TKB1 | Azka Andreas | S |
| 5/9 | PG | Erick Raphael Nasution | S |

- File versi terbaru: Absensi 5 September 2026 Saturday 13_02_38.xlsx (3 mark tgl 5, validasi lulus)
- Mapping: "Wilian"→Willian Geoffrey Utama (TKB2), "Azka"→Azka Andreas (TKB1)
- **DARREEN & AXELLE KELUAR SEKOLAH (5 September 2026):** Dareen Chandra (PG) dan Axelle Sean Chandra (PG) resmi keluar → row KEDUANYA dihapus dari roster PG di file versi terbaru (arsip tetap di file versi lama, termasuk mark Dareen tgl 1/9). Jangan cari/mark mereka lagi. Roster PG sekarang 11 siswa.
- Mapping kolom September (sama seperti Agustus): tgl d → kolom 3+d (5/9 = kolom 8). FILE_PATH absensi.py → file versi 5 September.
- **OBSERVASI NIGHT-SHIFT (6 Sept 2026):** file `Absensi September 2026 Saturday 08_33_12.xlsx` & file 5 Sept berisi MARK 2-4 SEPTEMBER yang BELUM pernah dicatat di memory (Dearni F A Parapat 2-S, 3-S; Roderick Yang 2-S, 3-S, 4-S; Ellena 2-S; Giovan O 2-S; Lionel 2-S; Ezequiel 4-S; TKB1 Venedict 2-S; TKB(2) Melviano 2-S, Shane 4-S) — kemungkinan diisi user langsung di PC. Data TIDAK diubah, hanya dicatat.
- **TOOL REKAP (6 Sept 2026):** `COMMON/scripts/rekap_absensi.py` — rekap bulanan S/I/A otomatis dari file absensi versi terbaru (deteksi file otomatis via parse nama bulan+tanggal, KOMPATIBEL lintas PC; ⚠️ jangan pakai mtime — base file 4ms lebih baru di server walau bukan versi terakhir). Butuh `openpyxl` (terpasang di server Linux, versi 3.1.5). Cara pakai: `python3 COMMON/scripts/rekap_absensi.py [--file "nama file"]`.

### Absensi 7-11 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 7/9 | PG | Erick Raphael Nasution | S |
| 7/9 | TKa | Lionel Oscar Hu | S |
| 7/9 | TKB(2) | Celine Grace Zhang | S |
| 7/9 | TKB(2) | Queenly Nathaniela | S |
| 7/9 | TKB(2) | Melviano Arentino Wijaya | S |
| 7/9 | TKB(2) | Jayoti Marnida Haulian Kaur | I |
| 7/9 | TKB(2) | Shane Michael Lienardie | S |
| 7/9 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 8/9 | PG | Erick Raphael Nasution | S |
| 8/9 | TKa | Dearni Felixa Alexandria Parapat | S |
| 8/9 | TKa | Ellena Clarissa Toh | S |
| 8/9 | TKB1 | Elsa Harianja | S |
| 8/9 | TKB(2) | Celine Grace Zhang | S |
| 9/9 | PG | Erick Raphael Nasution | S |
| 9/9 | TKB(2) | Celine Grace Zhang | S |
| 9/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 9/9 | TKB1 | Corin Falove Manurung | S |
| 9/9 | TKB1 | Elsa Harianja | S |
| 10/9 | PG | Jayden Kingwell Zhang | S |
| 10/9 | PG | Erick Raphael Nasution | S |
| 10/9 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 10/9 | TKa | Mikaylo Zionathan Girsang | S |
| 10/9 | TKa | Sharren Eliana Simanjuntak | S |
| 10/9 | TKa | Lionel Oscar Hu | S |
| 10/9 | TKa | Evano Ryu Tanzil | S |
| 10/9 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 10/9 | TKB1 | Corin Falove Manurung | S |
| 10/9 | TKB(2) | Shelomitha Eliora Simanjuntak | S |
| 10/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 10/9 | TKB(2) | Rui Reynara Shen | S |
| 11/9 | PG | Erick Raphael Nasution | S |
| 11/9 | TKa | Hester Kholyn | I |
| 11/9 | TKa | Hestine Kholyn | I |
| 11/9 | TKa | Lionel Oscar Hu | S |
| 11/9 | TKa | Ellena Clarissa Toh | S |
| 11/9 | TKa | Matthew Batara Hamonangan Nainggolan | S |
| 11/9 | TKa | Ruby Reynara Shen | S |
| 11/9 | TKa | Evano Ryu Tanzil | S |
| 11/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 11/9 | TKB(2) | Rui Reynara Shen | S |
| 11/9 | TKB1 | Generation Michael Abdiel Gea | S |
| 11/9 | TKB1 | Brenden Maxwell Angkasa | I |

- File versi tgl 7-11: Absensi 11 September 2026 Friday 09_00_00.xlsx (42 mark tgl 7-11, validasi lulus)
- File versi tgl 12: Absensi 12 September 2026 Saturday 09_46_38.xlsx (5 mark tgl 12: Ruby/Lionel/Valerie/Evano/Carencya TKa = S)
- **GENERATION MICHAEL ABIDEL GEA — MURID BARU TKB1:** ditambahkan ke roster TKB1 di file versi ini. Jangan lupa include di absensi berikutnya.
- Mapping: "Shallen"→Sharren Eliana Simanjuntak (TKa), "Dierni"→Dearni Felixa Alexandria Parapat (TKa), "Elena"→Ellena Clarissa Toh (TKa), "Evano"→Evano Ryu Tanzil (TKa), "Ryui"→Rui Reynara Shen (TKB2), "Quenly"→Queenly Nathaniela (TKB2), "Generation"→Generation Michael Abdiel Gea (TKB1)
- Catatan: user input "tkb1" untuk data tgl 7 Quenly/Melviano/Jayoti/Celine/Shane/Jemia — semua nama ada di roster TKB(2), dimasukkan ke TKB(2)

### Absensi 12 & 14 September 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 12/9 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 12/9 | TKB(2) | Jemia Zhevano Yamresa Kembaren | S |
| 12/9 | TKB(2) | Rui Reynara Shen | S |
| 12/9 | TKB(2) | Joevanca Chesa Athalia | S |
| 12/9 | TKB(2) | Celine Grace Zhang | S |
| 12/9 | TKB(2) | Brilliant | S |
| 12/9 | PG | Amelia Arthanauli Nainggolan | S |
| 12/9 | PG | Erick Raphael Nasution | S |
| 12/9 | PG | Eireen Lorenzo | S |
| 12/9 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 14/9 | TKB1 | Richelcia Wijaya | I |
| 14/9 | TKa | Ruby Reynara Shen | S |
| 14/9 | TKa | Valerie Sharon Nainggolan | S |
| 14/9 | TKa | Evano Ryu Tanzil | S |
| 14/9 | TKa | Lionel Oscar Hu | S |
| 14/9 | TKB(2) | Rui Reynara Shen | S |
| 14/9 | TKB(2) | Celine Grace Zhang | S |
| 14/9 | TKB(2) | Brilliant | S |
| 14/9 | TKB(2) | Lishaalini Krisna Naidu | S |
| 14/9 | PG | Erick Raphael Nasution | I |

- File versi terbaru: Absensi 14 September 2026 Monday 09_09_04.xlsx (20 mark tgl 12&14, validasi lulus)
- **BRILLIANT — MURID BARU TKB(2):** ditambahkan ke roster TKB(2) di file versi ini (row 32, kolom C, setelah Jayoti). Nama tanpa nama keluarga (diberi user apa adanya). Jangan lupa include di absensi berikutnya.
- Sebelumnya: file versi tgl 12 punya 5 mark TKa (Ruby/Lionel/Valerie/Evano/Carencya = S) yang sudah ada di file Absensi 12 September (dicatat di sesi sebelumnya).

### Kelas: TKa, TKB1, TKB2, PG

### Alasan: sakit (S), izin (I), alpha (A)

### Absensi 13-15 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| Senin 13/4 | TKB1 | Gabe | I |
| Senin 13/4 | TKB1 | Larasati | S |
| Selasa 14/4 | TKB1 | Gabe | I |
| Rabu 15/4 | TKB1 | Gabe | I |
| Rabin 15/4 | TKB1 | Naraya | S |

### Absensi Excel File (SISTEM VERSI — 4 Agustus 2026)
- **ABSENSI Agustus.xlsx = v1.0 sumber awal** (struktur & nama murid dari Juli, label "Agustus", SEMUA mark kosong). File ini TIDAK pernah diisi langsung.
- **Sistem versi:** setiap kali ada update → copy versi terbaru → file versi baru → isi data. File versi terbaru = paling lengkap & yang dipegang (FILE_PATH absensi.py nunjuk ke situ).
- **Backfill bebas:** di versi terbaru boleh diisi tanggal berapa saja (1-31), termasuk yang sebelumnya terlewat.
- Contoh rantai: `Absensi 1 Agustus 2026 Saturday 10_04_37.xlsx` (v-tgl-1, 8 mark) → `Absensi 3 Agustus 2026 Monday 10_04_37.xlsx` (v-tgl-3, 15 mark) → `Absensi 4 Agustus 2026 Tuesday 10_04_37.xlsx` (v-tgl-4, 17 mark) → `Absensi 5 Agustus 2026 Wednesday 09_00_45.xlsx` (v-tgl-5) → `Absensi 7 Agustus 2026 Friday 11_33_00.xlsx` (v-tgl-7) → `Absensi 10 Agustus 2026 Monday 10_34_36.xlsx` (v-tgl-10, 5 mark) → `Absensi 11 Agustus 2026 Tuesday 13_48_14.xlsx` (v-tgl-11, VERSI TERBARU, 7 mark).
- **Format nama file versi:** `Absensi <tgl> <bulan> <tahun> <hari> <jam>_<menit>_<detik>.xlsx` (contoh: "Absensi 4 Agustus 2026 Tuesday 10_04_37.xlsx" — tgl dulu, baru bulan, jam_menit_detik = waktu asli file dibuat). Bukan "Agustus 4".
- **File (Juli, arsip):** ABSENSI Juli.xlsx — master bulan Juli, jadi arsip permanen
- **PENTING (4 Agustus 2026):** Konsep versi dikoreksi user: ABSENSI Agustus.xlsx = v1.0 kosong (sumber awal), jangan menumpuk data di master. Tiap update bikin file versi baru (copy dari versi terakhir), absensi.py diarahkan ke versi terbaru. File snapshot harian yang isinya stale TIDAK dibuat lagi (dulu sempat keliru: "Absensi Agustus 4 08_59_50" isinya lama → dihapus).
- **ATURAN:**
  - ABSENSI Agustus.xlsx = sumber awal, TIDAK diisi langsung
  - Tiap update: copy versi terakhir → versi baru → isi data (via absensi.py yang diarahkan ke versi baru)
  - Setiap hari: **duplicate ABSENSI Juli.xlsx dulu** → arsip harian (snapshot lengkap sampai hari sebelumnya), LALU update master dengan absen hari ini
  - **1 file baru per hari** - tidak boleh lebih dari 1 file sehari
  - File lama = arsip, tidak dihapus
  - JANGAN duplicate file harian lama yang datanya tidak lengkap — selalu dari ABSENSI Juli.xlsx (file terlengkap)
  - Kalau ada keraguan data lengkap atau tidak → cek dulu dengan merge_absensi.py
- **Format Nama File Duplicate:** Absensi <bulan> <tgl> <tahun> <hari> <jam>_<menit>_<detik>.xlsx
  - Contoh: Absensi April 22 2026 Wednesday 10_27_21.xlsx
- **Lokasi File:** C:\Users\Admin\Desktop\memory\PC-06\docs\Absensi T.P 2026-2027\

### Absensi 23 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 23/4 | TKB(2) | Chelsea Valerie | S |
| 23/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 20/4 | TKB1 | Gestalt | I |
| 20/4 | TKB1 | Jocelyn | S |
| 20/4 | TKB1 | Larasaty | S |
| 20/4 | TKB1 | Jayden | I |
| 21/4 | TKB1 | Larasaty | S |
| 22/4 | TKB1 | Raileen | S |
| 22/4 | TKB1 | Larasaty | S |
| 23/4 | TKB1 | Jayden | I |
| 23/4 | TKB1 | Jocelyn | I |
| 23/4 | TKB1 | Reiner | I |
| 23/4 | TKB1 | Gabe | I |
| 23/4 | TKa | Richel Wijaya | S |
| 23/4 | TKa | Darren Elvano | S |
| 23/4 | TKa | Shelo | I |

- File hasil: Absensi April 23 2026 Thursday 12_21_13.xlsx

### Absensi 25 Mei 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 25/5 | PG | Edbert Reynaldo Lim | S |
| 25/5 | TKB2 | Richa Dwily | S |
| 25/5 | TKB1 | Sheera Leticia Nainggolan | I |
| 25/5 | TKB1 | Sheryn Florencia Nainggolan | I |
| 25/5 | TKa | Joevanca | S |
| 25/5 | TKa | Melviano | I |

- File daily: Absensi Mei 25 2026 Monday 10_39_17.xlsx

### Absensi 27 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 25/4 | PG | Joverick | I |
| 27/4 | PG | Joverick | I |
| 25/4 | TKB(2) | Chelsea Valerie | S |
| 25/4 | TKB(2) | Marquez Boas Aritonang | S |
| 25/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 25/4 | TKB(2) | Jasmine Valerie Yap | S |
| 25/4 | TKB(2) | Christine Laotan | S |
| 27/4 | TKB(2) | Pangeran Hagro Haloho | S |
| 27/4 | TKB(2) | Alvaro Gavriel Karo Karo | S |
| 27/4 | TKB(2) | Brienne Nathania Carolyne Pakpahan | S |
| 25/4 | TKB1 | Jocelyn Marcella Su | I |
| 25/4 | TKB1 | Naraya Elsandri Br. Sembiring | I |
| 25/4 | TKB1 | Gabe Cristiano Gultom | I |
| 27/4 | TKB1 | Grace Felicia Simbolon | S |
| 25/4 | TKa | Azka Andreas | I |
| 25/4 | TKa | Lishaalini Krisna Naidu | S |
| 27/4 | TKa | Richelcia Wijaya | A |
| 27/4 | TKa | Celine Grace Zhang | S |
| 27/4 | TKa | Lishaalini Krisna Naidu | S |

- File hasil: Absensi April 27 2026 Monday 09_09_12.xlsx

### Absensi 22 April 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|------|------|--------|
| 18/4 | TKa | Aldrich, Darren Elvano, Clarita, Richelcia | S |
| 20/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |
| 21/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |
| 22/4 | TKa | Aldrich, Darren Elvano, Richelcia | S |

- File hasil: Absensi April 22 2026 Wednesday 10_27_21.xlsx

### Absensi 21-23 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 21/7 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 22/7 | TKa | Chesa Efrata Ronatio Tampubolon | S |
| 23/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 23/7 | TKa | Jarvis Derren Lai | S |
| 23/7 | TKa | Ray Richson | S |

- File hasil: Absensi Juli 23 2026 Wednesday 11_58_10.xlsx

### Absensi 24 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 24/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 24/7 | TKa | Chesa Efrata Ronatio Tampubolon | S |

### Absensi 30 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 30/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 30/7 | TKB2 | Celine Grace Zhang | S |
| 30/7 | TKB1 | Melvin Panca Sihombing | I |
| 30/7 | TKB1 | Brenden Maxwell Angkasa | S |

- File hasil: Absensi Juli 30 2026 Thursday 09_24_56.xlsx

### Absensi 29 Juli 2026

| Tanggal | Kelas | Nama | Alasan |
|---------|-------|------|--------|
| 29/7 | TKB2 | Jayoti Marnida Haulian Kaur | S |
| 28/7 | PG | Kimita Dessyana Meisim | I |
| 28/7 | PG | Hans Lukas Mangara Datta Tampubolon | I |
| 28/7 | TKB(2) | Shelomitha Eliora Simanjuntak | S |
| 28/7 | TKB(2) | Jocelyn Marcella Su | S |
| 29/7 | TKB(2) | Jocelyn Marcella Su | S |
| 29/7 | TKB(2) | Joevanca Chesa Athalia | S |
| 29/7 | TKB(2) | Celine Grace Zhang | S |
| 28/7 | TKa | Chesa Efrata Ronatio Tampubolon | I |
| 28/7 | TKa | Sharren Eliana Simanjuntak | S |
| 29/7 | TKa | Chesa Efrata Ronatio Tampubolon | I |

- File hasil: Absensi Juli 29 2026 Wednesday 09_40_10.xlsx

### Absensi 17 April 2026

| Kelas | Nama | Alasan |
|-------|------|--------|
| TKa | Richel Wijaya | S |
| TKa | Aldrich S | S |
| TKa | Clarita S | S |
| TKB1 | Joverick S | S |
| TKB2 | Shayna S | S |
| TKB2 | Claudia S | S |
| TKB2 | Brienne S | S |

---
