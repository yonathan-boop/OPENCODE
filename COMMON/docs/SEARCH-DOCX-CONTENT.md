# Mencari Isi File di Folder Surat (Methodist-11)

#surat-keluar #methodist-11 #docx #search #kata-kunci #backup

## Masalah
Kadang butuh surat tertentu tapi tidak ingat nama file-nya — hanya ingat kata kunci isinya (contoh: nama murid, "aktif", "Methodist-11", "beasiswa", dll).

## Lokasi Folder
```
E:\Back Up\Back up 20 Juni 2026\Methodist-11 Document\SURAT KELUAR\SD
```
(ada juga subfolder lain: TK, SMP, dll — tinggal ganti path terakhir)

## Cara Cari (Python)
Cari isi semua file `.docx` dengan kata kunci. Jalankan di PowerShell:

```python
python -c "
import glob, os, zipfile
from xml.etree import ElementTree as ET
path=r'E:\Back Up\Back up 20 Juni 2026\Methodist-11 Document\SURAT KELUAR\SD'
KW=['NAMA ATAU KATA KUNCI DI SINI']
def txt(f):
    try:
        z=zipfile.ZipFile(f)
        x=z.read('word/document.xml')
        r=ET.fromstring(x)
        return ''.join(t.text or '' for t in r.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    except: return ''
for f in glob.glob(os.path.join(path,'*.docx')):
    t=txt(f).lower()
    if any(k.lower() in t for k in KW):
        print('===', os.path.basename(f))
        print(txt(f)[:1200])
        print()
"
```

Ganti `KW=['...']` dengan kata kunci yang dicari (boleh lebih dari satu).

## Tips
- Kata kunci dalam `KW` di-OR (cukup salah satu cocok).
- Buat lebih ketat → tulis 2+ kata kunci dan ganti `any(...)` jadi `all(...)`.
- Ekstrak isi `.docx` = file zip → baca `word/document.xml` → ambil semua tag `<w:t>`.
- Path bisa dipakai juga di subfolder lain (ganti `SD` → `TK`, `SMP`, dst).

## Catatan
- Diperkuat 5 Agustus 2026 saat cari surat "murid Methodist-11 masih aktif" — hasilnya banyak Surat Keterangan standar: `SD No. 531` (Irene), `549` (Reviona), `551` (Gebyar, "aktif sampai sekarang"), dll.
- File `~$...` = file lock sementara, diabaikan.
