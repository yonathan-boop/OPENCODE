# Otomatisasi Laporan Sekolah dengan Excel/Python (openpyxl)

Topik queue self-study — di-claim & ditulis dari PC (yonat-PC) 17/9/2026. Fokus: pola aman, hemat memori, validasi sebelum lapor. Berlaku untuk rekap absensi, daftar nilai, dan laporan bulanan.

## Ringkasan
openpyxl nyaman untuk ribuan baris, tapi **boros memori ~50× ukuran file asli** (50 MB file → ±2.5 GB RAM) karena tiap sel jadi objek Python. Kabar baiknya ada mode streaming: `read_only` (baca) & `write_only` (tulis) dengan memori hampir konstan. Untuk laporan yang dibuka manusia (ratusan baris) mode normal cukup; file raksasa/berulang mending lewat CSV/Parquet, Excel hanya untuk output ringkas. Pola terpenting utk kerja admin sekolah: **template diisi, jangan ditimpa; simpan file baru dengan nama ber-tanggal** (persis sistem versi absensi yang sudah jalan).

## Poin praktis
### Membaca besar / hemat memori
- `load_workbook(path, read_only=True)` → alirkan per baris, jangan bangun semua sel.
- Tambah `values_only=True` saat `iter_rows` → dapat tuple, bukan objek sel (alokasi paling mahal di-skip).
- `data_only=True` → ambil *nilai ter-cache* hasil kalkulasi terakhir Excel, bukan rumusnya.
- **WAJIB `wb.close()` di `finally`** — file zip tetap terbuka selama reader hidup; lupa → "Too many open files" di proses panjang.
- Satu pass per sheet; stream tidak bisa di-rewind. Butuh scan ulang → re-open, atau kumpulkan kebutuhan di pass pertama. `max_row` di mode ini sering salah (dimensi yang dideklarasikan) → hitung sambil iterasi.
- Scan + edit di file sama → **dua handle** (read_only utk scan, normal utk edit).

### Menulis banyak data / dari nol
- `Workbook(write_only=True)` → `ws.create_sheet()`, isi cuma boleh `ws.append(...)` (tanpa random access). Memori <10 MB bahkan utk jutaan baris.
- `freeze_panes` harus di-set SEBELUM append. Workbook hanya bisa disimpan sekali (`WorkbookAlreadySaved`). Butuh style per sel di mode ini → `WriteOnlyCell`.

### Pola template (paling relevan: absensi, rapor)
- Load template → tulis **hanya sel data** → simpan **file baru ber-tanggal**. JANGAN timpa template (ini = prinsip sistem versi absensi).
- **Jangan menimpa sel yang berisi formula** (mis. sel `=SUM(...)`). Tulis angkanya di sumber, biar Excel hitung ulang saat dibuka.
- **Hindari `pandas.to_excel` untuk mengisi template** — ia mengganti seluruh sheet, semua desain (banner, merge, rumus, print area) hilang.
- `.xlsm`/`.xltm` → wajib `keep_vba=True` di `load_workbook`, kalau tidak macro terbuang & file dianggap korup.
- Alamat rawan berubah → pakai **defined name** (named range); kalau hilang, biarkan raise error dgn pesan jelas (gagal keras, bukan sel kosong diam-diam).
- Formula: generate referensi dari `ws.max_row` yang baru ditulis + anchor `$` utk cell tetap; pakai `get_column_letter` biar kolom tidak patah saat layout berubah.
- Style object **immutable & dipakai bareng** (flyweight) → utk gaya sel baru, `copy()` dulu sebelum assign, jangan mutasi `cell.font.bold = True` (diam-diam tidak berefek). Merge cell → isi di sel kiri-atas.

### Data validation (dropdown) di file output
- Urutan wajib: buat rule → `ws.add_data_validation(dv)` → `dv.add("B2:B100")`. Lupa registrasi = dropdown tidak muncul tanpa error.
- Inline list maks 255 karakter → lebih dari ~25 opsi taruh di sheet lookup (atau named range).
- `formula1` harus `='"North,South,West"'` (ada tanda kutip di dalam string).
- Rule sejumlah-cell → jangan per-cell; satu rule utk satu range besar jauh lebih ringan.
- **Excel hanya enforce saat typing, bukan paste/import** → validasi Python tetap wajib.

### Validasi data sebelum lapor (panduan umum)
- Baca mentah (`dtype=object`), coerce eksplisit, simpan nilai yang gagal — biar tahu baris mana yang rusak, bukan cuma ada error.
- Normalisasi dulu sebelum tes: `strip()`, casing (`"north "` vs `"North"`). Auto-fix yang tidak ambigu; nilai yang butuh keputusan → lapor.
- Perbandingan `float` pakai **tolerance** (mis. `abs(a-b) > 0.005`), jangan sama persis.
- Cek relational: angka × harga = total; jumlah baris bulan ini vs bulan lalu (tangkap file terpotong/filter kesengsem).
- Aturan bisnis = boolean mask + pesan, sehingga nambah aturan tinggal satu entri.

## Jebakan khas openpyxl
- `data_only=True` → dapat `None` untuk file yang belum pernah dibuka/ disimpan oleh Excel (tidak ada nilai cache). Jangan pakai utk "hitung".
- **Menyimpan workbook yang di-load dengan `data_only=True` akan mengganti SEMUA formula jadi angka** — kalau mau formula tetap, load tanpa `data_only`.
- Cell menunjukkan `=B2*C2` sebagai teks → number_format-nya "Text" → set "General" sebelum assign, atau string tidak diawali `=`.
- Formula ber-`#REF!` muncul belakangan → referensi di-generate dari angka hardcode. Bangun dari `ws.max_row`; nama sheet ber-spasi wajib quote `'Q1 Sales'!A1`.
- Angka `####` di Excel → kolom terlalu sempit (bukan error data). Lebar kolom sampai muat, sisakan ruang utk panah filter.
- Gaya hilang setelah roundtrip → biasanya lewat `pandas.to_excel`. Gunakan `load_workbook` + edit in-place.

## Kaitan dengan tool yang sudah ada
- `absensi.py` (sistem versi: copy → file baru → FILE_PATH → isi → validasi) = penerapan "save-as-new-file, jangan overwrite template".
- `rekap_absensi.py` (deteksi file via parse nama bulan+tanggal, baca header row 6) = contoh membaca pakai `read_only` + cek header.
- `rekap_absensi.py` ⚠️ pantau mode read: pilih file versi terbenar dari parse nama, bukan mtime (file 4ms lebih baru di server walau bukan versi terakhir).

## Sumber
- Buku pedoman openpyxl: https://openpyxl.readthedocs.io/en/stable/optimized.html (mode read/write-only) & /validation.html (DataValidation)
- https://python-excel-automation.com/automating-reporting-workflows/generating-excel-reports-from-templates/ (template: isi bukan timpa, keep_vba, named range)
- https://python-excel-automation.com/advanced-data-transformation-and-cleaning/working-with-large-excel-files-in-python/ (read_only/values_only/write_only, kapan pindah ke csv/parquet)
- https://python-excel-automation.com/getting-started-with-python-excel-automation/working-with-excel-formulas-in-python/ (formula: data_only, anchor $, quote sheet)
- https://thelinuxcode.com/working-with-excel-spreadsheets-in-python-a-practical-production-style-playbook/ (playbook produksi: validasi, template, formula)
- https://dev.to/toby-patrick/issues-of-multi-gb-spreadsheets-in-data-lakes-9n0 (streaming + chunk 5.000–10.000 + validasi file)
- https://python-excel-automation.com/advanced-data-transformation-and-cleaning/validating-excel-data-with-python/ (validasi dua lapis: pandas + openpyxl)