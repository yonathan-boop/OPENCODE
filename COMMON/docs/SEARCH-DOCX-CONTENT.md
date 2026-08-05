# Mencari Isi File di Folder Surat (Methodist-11)

#surat-keluar #methodist-11 #docx #xlsx #search #kata-kunci #backup

## Masalah
Kadang butuh surat/file tertentu tapi tidak ingat nama file-nya — hanya ingat kata kunci isinya (contoh: nama murid, "aktif", "Methodist-11", "beasiswa", dll).

## Lokasi Folder
```
E:\Back Up\Back up 20 Juni 2026\Methodist-11 Document\SURAT KELUAR\SD
```
- **LOKASI TIDAK TETAP** — user WAJIB ditanya dulu folder mana yang dicari.
- Jangan asumsi pakai path di atas; minta user kasih path dulu sebelum eksekusi.
- Path bisa dipakai juga di subfolder lain (ganti `SD` → `TK`, `SMP`, dst).

## Cara Cari (Python)
### A. Cari isi `.docx` (Word)
```python
python -c "
import glob, os, zipfile
from xml.etree import ElementTree as ET
path=r'GANTI-DENGAN-LOKASI-FOLDER'
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

### B. Cari isi `.xlsx` (Excel)
```python
python -c "
import glob, os, zipfile
from xml.etree import ElementTree as ET
path=r'GANTI-DENGAN-LOKASI-FOLDER'
KW=['NAMA ATAU KATA KUNCI DI SINI']
def txt(f):
    try:
        z=zipfile.ZipFile(f)
        out=[]
        for name in z.namelist():
            if name.startswith('xl/sharedStrings.xml') or (name.startswith('xl/worksheets/') and name.endswith('.xml')):
                x=z.read(name)
                r=ET.fromstring(x)
                out.append(''.join(t.text or '' for t in r.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')))
        return ' '.join(out)
    except: return ''
for f in glob.glob(os.path.join(path,'*.xlsx')):
    t=txt(f).lower()
    if any(k.lower() in t for k in KW):
        print('===', os.path.basename(f))
        print(txt(f)[:1200])
        print()
"
```

Ganti `KW=['...']` dengan kata kunci (boleh lebih dari satu), `path` dengan lokasi folder.

## Tips
- Kata kunci dalam `KW` di-OR (cukup salah satu cocok).
- Buat lebih ketat → tulis 2+ kata kunci dan ganti `any(...)` jadi `all(...)`.
- Ekstrak `.docx` = file zip → baca `word/document.xml` → tag `<w:t>`.
- Ekstrak `.xlsx` = file zip → baca `xl/sharedStrings.xml` + `xl/worksheets/*.xml` → tag `<t>` (namespace spreadsheetml).
- `.doc` / `.xls` (format lama) TIDAK didukung — harus konversi dulu ke docx/xlsx.

## Catatan
- Diperkuat 5 Agustus 2026 saat cari surat "murid Methodist-11 masih aktif" — hasilnya banyak Surat Keterangan standar: `SD No. 531` (Irene), `549` (Reviona), `551` (Gebyar, "aktif sampai sekarang"), dll.
- File `~$...` = file lock sementara, diabaikan.
