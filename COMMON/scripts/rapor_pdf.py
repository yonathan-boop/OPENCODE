"""
Rapor LHB 2026.xlsm -> 1 PDF gabungan per kelas.
Pakai:  py rapor_pdf.py <KELAS>   contoh: py rapor_pdf.py "VB SD"
Mapping sheet: kelas 1/2 -> A, 3/4 -> B, 5/6 -> C (sesuai aturan user 18/9).
Output: <KELAS>.pdf di folder yang sama dengan 2026.xlsm (temp dibersihkan).
"""
import os, sys, re, tempfile, shutil, time

import win32com.client
import pythoncom
import openpyxl
import pymupdf

XLSM = r'C:\Users\yonat\OneDrive\Desktop\Opencode\Test edit\2026.xlsm'
DIR = os.path.dirname(XLSM)

def com_call(fn, *args, tries=60):
    for _ in range(tries):
        try:
            return fn(*args)
        except pythoncom.com_error as e:
            if e.hresult in (-2147418111, -2147417846):  # rejected/busy
                time.sleep(0.5)
                continue
            raise
    raise SystemExit('Excel tetap sibuk (call rejected berulang)')

def detect_sheet(kelas):
    # romawi -> sheet (user: 1/2 -> A, 3/4 -> B, 5/6 -> C)
    rules = [('III', 'B'), ('IV', 'B'), ('VI', 'C'),
             ('II', 'A'), ('V', 'C'), ('I', 'A')]
    for rom, s in rules:
        if kelas.startswith(rom):
            return s
    raise SystemExit(f'Tidak bisa deteksi sheet untuk kelas {kelas!r}')

def nomor_murid(kelas):
    """Kembalikan daftar nomor urut yang benar-benar ada di Data (bisa ada gap)."""
    wb = openpyxl.load_workbook(XLSM, read_only=True, data_only=True)
    ws = wb['Data']
    nums = []
    for r in ws.iter_rows(min_row=3, max_row=700, max_col=1):
        v = r[0].value
        if isinstance(v, str) and v.startswith(kelas):
            suffix = v[len(kelas):].strip()
            if suffix.isdigit():
                nums.append(int(suffix))
    wb.close()
    return sorted(set(nums))

def main():
    if len(sys.argv) < 2:
        raise SystemExit('Pakai: py rapor_pdf.py "<KELAS>"  contoh "VB SD"')
    kelas = sys.argv[1].strip()
    sheet = detect_sheet(kelas)
    nums = nomor_murid(kelas)
    if not nums:
        raise SystemExit(f'Tidak ada data murid untuk kelas {kelas!r}')
    if len(nums) != nums[-1] - nums[0] + 1:
        missing = [n for n in range(nums[0], nums[-1] + 1) if n not in set(nums)]
        print(f'Catatan: nomor kosong di Data: {missing} (dilewati)')
    print(f'Kelas {kelas!r} -> sheet {sheet}, murid {len(nums)} (no {nums[0]}-{nums[-1]})')

    tmp = tempfile.mkdtemp(prefix='rapor_')
    excel = None; wb = None; ws = None
    try:
        excel = win32com.client.DispatchEx('Excel.Application')
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False
        wb = com_call(excel.Workbooks.Open, XLSM, False, True)
        ws = com_call(wb.Worksheets, sheet)
        com_call(ws.Activate)
        ws.Range('F2').Value = kelas
        ws.Range('H7').Value = nums[0]
        ws.Range('H8').Value = nums[-1]

        files = []
        for i in sorted(nums, reverse=True):
            ws.Range('H1').Value = i
            try:
                com_call(ws.Calculate)
            except Exception:
                pass
            no = ws.Range('D7').Value
            if isinstance(no, float) and no.is_integer():
                no = int(no)
            nama = str(ws.Range('D9').Value)
            safe = re.sub(r'[\\/:*?"<>|]', '_', f'{no}-{nama}-{i}')
            out = os.path.join(tmp, f'{i:03d}.pdf')
            com_call(ws.ExportAsFixedFormat, 0, out)
            files.append((i, out, safe))
            print(f'  {safe}')

        merged = pymupdf.open()
        for i, out, safe in sorted(files, key=lambda x: x[0]):
            src = pymupdf.open(out)
            merged.insert_pdf(src)
            src.close()
        dest = os.path.join(DIR, f'{kelas}.pdf')
        merged.save(dest, garbage=4, deflate=True)
        pages = merged.page_count
        merged.close()
        print(f'OK: {dest}  ({pages} halaman)')
    finally:
        try:
            if wb is not None:
                wb.Close(False)
        except Exception:
            pass
        try:
            if excel is not None:
                excel.Quit()
        except Exception:
            pass
        if ws is not None:
            try: import pythoncom; pythoncom.CoUninitialize()
            except Exception: pass
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == '__main__':
    main()