import openpyxl
from openpyxl import load_workbook
import sys

FILE_PATH = "C:/Users/Admin/Desktop/Absensi/ABSENSI April.xlsx"

KELAS_MAP = {
    'tka': 'TKa', 'tk a': 'TKa',
    'tkb1': 'TKB1', 'tk b1': 'TKB1',
    'tkb2': 'TKB(2)', 'tk b2': 'TKB(2)', 'tkb(2)': 'TKB(2)',
    'pg': 'Absen PG', 'playgroup': 'Absen PG', 'absen pg': 'Absen PG'
}

TANGGAL_MAP = {}

KODE = {
    'sakit': 'S', 's': 'S',
    'izin': 'I', 'i': 'I',
    'alpha': 'A', 'a': 'A'
}

def build_tanggal_map(ws):
    tanggal_to_col = {}
    for c in range(4, 35):
        tgl = ws.cell(6, c).value
        if tgl and str(tgl).isdigit():
            tanggal_to_col[int(tgl)] = c
    return tanggal_to_col

def absen(nama, kelas, tanggal, alasan):
    wb = load_workbook(FILE_PATH)
    
    kelas = kelas.lower().strip()
    sheet_name = KELAS_MAP.get(kelas)
    
    if not sheet_name:
        print(f"[ERROR] Kelas tidak dikenal: {kelas}")
        return
    
    ws = wb[sheet_name]
    tanggal_map = build_tanggal_map(ws)
    
    if int(tanggal) not in tanggal_map:
        print(f"[ERROR] Tanggal {tanggal} tidak ada di sheet {sheet_name}")
        print(f"Tanggal tersedia: {sorted(tanggal_map.keys())}")
        return
    
    col_hari = tanggal_map[int(tanggal)]
    kode = KODE.get(alasan.lower(), alasan.upper())
    
    ws_data = wb['Data']
    kelas_upper = kelas.upper() if kelas != 'pg' else 'PG'
    
    row_ditemukan = None
    nama_ditemukan = None
    for row in range(4, 150):
        nama_murid = ws_data.cell(row, 4).value
        kelas_murid = ws_data.cell(row, 5).value
        if nama_murid and kelas_murid == kelas_upper:
            if nama.lower() in nama_murid.lower():
                row_ditemukan = row
                nama_ditemukan = nama_murid
                break
    
    if not row_ditemukan:
        print(f"[ERROR] Murid '{nama}' tidak ditemukan di kelas {kelas}")
        return
    
    no_urut = ws_data.cell(row_ditemukan, 2).value
    absen_row = 7 + int(no_urut) - 1
    
    ws.cell(absen_row, col_hari).value = kode
    wb.save(FILE_PATH)
    
    print(f"[OK] {nama_ditemukan} ({sheet_name}) - Tanggal {tanggal} = {kode} (baris {absen_row})")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Cara pakai: py absensi.py <nama> <kelas> <tanggal> <alasan>")
        print("Contoh: py absensi.py Kyla TKB1 14 sakit")
        sys.exit(1)
    
    absen(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])