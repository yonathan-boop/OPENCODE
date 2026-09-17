# Mail Merge & Narasi Rapor di Word: Batch dari Excel, Masalah Umum & Solusinya

> Ditulis 2026-09-17 (self-study server). Berlaku untuk Word (Microsoft 365 / 2016+) + Excel sebagai sumber data. Sentuhannya relevan untuk narasi rapor, surat, sertifikat, label.

## Ringkasan

Mail merge = fitur Word untuk membuat banyak dokumen (satu per murid/guru/penerima) dari SATU template + tabel data Excel. Word menarik data per baris dari Excel dan mengisi field (nama, kelas, narasi, dst) secara otomatis. Kunci keberhasilan ada di **kerapian data Excel**, bukan di Word. Dokumen rapor yang benar-benar aman: file Word master + file data Excel diletakkan di folder lokal yang sama, file Excel ditutup sebelum merge.

Cara cepat (langkah inti):
1. **Excel**: baris 1 = header kolom unik (mis. `Nama`, `Kelas`, `Narasi_Perkembangaan`), data mulai baris 2. Tanpa merged cells, tanpa baris kosong di tengah/atas, tanpa simbol aneh di header. Skor/poin numerik simpan sebagai Teks bila perlu awalnya `0` (mis. NISN, nomor induk).
2. Simpan Excel, **tutup file** sebelum merge.
3. **Word**: tab `Mailings` → `Start Mail Merge` → pilih jenis (`Letters` untuk rapor personal) → `Select Recipients` → `Use an Existing List` → pilih file Excel, pilih sheet yang benar, centang *First row of data contains column headers*.
4. Taruh kursor di posisi yang mau diisi → `Insert Merge Field` → pilih kolom (Nama, Narasi, dst). Sisipkan simbol (Rp, %, dst) langsung di template Word, bukan dari Excel.
5. `Preview Results` (cek beberapa record, bukan cuma satu) → `Finish & Merge` → `Edit Individual Documents` (jadi 1 file Word panjang, aman diedit) atau `Print`.

## Poin praktis untuk admin sekolah

- **Narasi rapor**: siapkan kolom `Narasi` di Excel yang isinya teks lengkap per murid. Template Word tinggal `Insert Merge Field: Narasi`. Kalau narasi rutin (mis. deskripsi per tema), buat kolom narasi dengan formula/teks statis di Excel — isi sekali, merge banyak.
- **Uji cetak 1 halaman dulu** sebelum batch besar (Error umum format berubah saat print). Pastikan margin/kertas Folio/A4 konsisten antara template & printer.
- **Simpan file Excel & Word di folder lokal yang sama** (mis. `C:\Rapor\`), bukan di OneDrive/cloud sync — sinkronisasi cloud bikin Word sering gagal baca data source ("unable to open the data source").
- **Selalu Preview beberapa record berbeda** — cek nama panjang yang bisa meluber, narasi yang terlalu pendek/panjang, dan tanggal yang berubah format.
- Saat ada perubahan template (mis. kop baru), cukup edit 1 file master lalu merge ulang — tidak perlu edit tiap dokumen.
- Hasil `Edit Individual Documents` = file baru yang nilai field-nya sudah jadi angka/teks statis, jadi aman dikirim/dicetak tanpa bergantung ke Excel lagi.

## Jebakan / error umum

| Gejala | Penyebab | Solusi |
|--------|----------|--------|
| Word tidak bisa hubungkan/sumber data ("External table is not in the expected format", "cannot open data source", "error reading from file") | File xlsx di shared folder dibuka user lain, file masih terbuka di Excel, atau sinkronisasi cloud (OneDrive/iCloud) mengunci file | Tutup Excel; pindah ke folder lokal non-cloud; pakai format .xls/.csv sebagai sumber; pilih provider **Microsoft Excel via OLE DB** di menu *Confirm Data Source* (Show All) |
| File dipindah/rename → Word tanya lokasi / data hilang | Word menyimpan path absolut ke Excel | Jangan pindahkan file setelah merge; perbaiki lewat `Select Recipients` → `Use an Existing List` → arahkan ke lokasi baru |
| Tanggal berubah format (jadi MM/DD/YYYY/integer) | OLE DB default menghilangkan format asli Excel | Klik kanan field → `Toggle Field Codes` → tambah `\@ "dd MMMM yyyy"` di dalam field code → `Update Field` (Alt+F9 untuk toggle) |
| Angka nol depan hilang (NISN, kode pos 00399 → 399) | Kolom Excel terbaca sebagai angka | Format kolom sebagai **Teks** di Excel sebelum merge; untuk import CSV pakai Text Import Wizard set kolom ke Text |
| Simbol Rp/%/desimal hilang atau jadi desimal panjang | Word tidak memakai format angka Excel | Tulis simbol langsung di template Word di sekitar field merge |
| Field tampil sebagai `«Nama»` / tidak terisi | Header tidak cocok, field name typo/renamed di Excel, atau salah sheet | Cek header baris 1; gunakan `Match Fields` di Mailings; pilih sheet/named range yang benar; kalau sudah jadi data tapi masih kode → Ctrl+A lalu Ctrl+Shift+F9 |
| Kolom kosong/header kosong → Word kasih nama `Column1` | Baris 1 berisi header yang tidak unique/blank | Isi setiap sel baris 1 dengan nama kolom unik, data mulai di A1 |
| Hasil print berubah format / data duplikat | Next Record rule salah (untuk label/amplop), margin printer beda, font/paragraf tak konsisten | Cek aturan Next Record (untuk label/amplop), Update Fields sebelum print, set margin sesuai printer, affiliation driver printer update |
| Word menanyakan konfirmasi buka file Excel tiap kali ("Excel Workbook text converter") | File disimpan format lama / path cloud | Simpan ulang sebagai .xlsx bersih; pindah ke folder lokal; pastikan header tanpa karakter khusus (`&`, `<`, `>`, `"`) |
| Sheet Excel direname/pindah | Word mereferensikan nama worksheet | Kembalikan nama sheet atau re-link lewat Select Recipients; gunakan named range (`Formulas > Define Name`) untuk lebih aman |
| Dokumen lama "fields can no longer be found" saat dibuka | Path Excel lama sudah obsolete | Klik *Yes* di dialog SQL/sumber data; kalau yakin aman, aktifkan *Trusted Location* di Trust Center |
| Data source diakses user lain bersamaan | Word buka .xlsx secara eksklusif (lock) | Gunakan .csv/.xls, atau jangan buka dokumen yang sama bersamaan |

Inti dari hampir semua error: **data Excel-nya yang harus rapi** (header di baris 1, data mulai A1, format kolom benar, file tertutup, folder lokal non-cloud). Sebagian besar error koneksi membaik dengan memakai provider **OLE DB** dan men-disable DDE/`Confirm file format conversion on open` di Word Options → Advanced bila perlu.

## Sumber

- Microsoft Support — Prepare your Excel data source for a Word mail merge: https://support.office.com/en-gb/article/Prepare-your-Excel-data-source-for-a-Word-mail-merge-2d802b6b-a3a3-43e5-bb76-2cac7c68673e
- Microsoft Learn — Mail merge error when data source accessed by multiple users: https://learn.microsoft.com/en-us/office/troubleshoot/word/mail-merge-error
- Microsoft Q&A — "There was an error reading from the file": https://learn.microsoft.com/en-us/answers/questions/5688191/mail-merge-existing-list-there-was-an-error-readin
- Microsoft Q&A — Mail merge keeps losing EXCEL data source (OneDrive/iCloud): https://learn.microsoft.com/en-us/answers/questions/5223302/why-does-mail-merge-(office-365)-keep-losing-its-e
- WiseChecker — Word Mail Merge Cannot Connect to Excel Data Source: Fix (OLE DB vs ODBC): https://wisechecker.com/word-mail-merge-cannot-connect-to-excel-data-source-fix/
- RapidRepair — How to Repair Mail Merge Connection & Data Errors (DDE, Match Fields, Trusted Location): https://www.rapidrepair.blog/repair-mail-merge-connection-errors
- GenText — Fix: Word Mail Merge Errors and Failures (field codes → values, Ctrl+Shift+F9): https://gentext.ai/guides/en/word-mail-merge-errors-fix/
- Katasulsel — Cara Membuat Mail Merge di Microsoft Word (langkah lengkap, kesalahan umum): https://katasulsel.com/cara-membuat-mail-merge-di-microsoft-word-lengkap-untuk-surat-sertifikat-dan-label/
- atp.ac.id — 5 Alasan Mail Merge Berubah Saat Print & Cara Mengatasi: https://atp.ac.id/5-alasan-kenapa-mail-merge-berubah-pada-word-saat-print-dan-cara-mengatasinya-di-2026/
- PAUD Jateng — Rapor PAUD TK/KB Kurikulum Merdeka Mail Merge Excel (contoh aplikasi rapor PAUD): https://www.paud.id/rapor-paud-tk-kb-otomatis-kurikulum-merdeka/