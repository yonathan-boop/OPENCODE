import openpyxl
from openpyxl import load_workbook
import sys
import os
import re
import difflib

FILE_PATH = os.environ.get(
    "ABSENSI_FILE",
    "C:/Users/yonat/OneDrive/Desktop/memory/PC-06/docs/Absensi T.P 2026-2027/Absensi 21 September 2026 Monday 09_45_34.xlsx",
)

KELAS_MAP = {
    'tka': 'TKa', 'tk a': 'TKa',
    'tkb1': 'TKB1', 'tk b1': 'TKB1',
    'tkb2': 'TKB(2)', 'tk b2': 'TKB(2)', 'tkb(2)': 'TKB(2)',
    'pg': 'Absen PG', 'playgroup': 'Absen PG', 'absen pg': 'Absen PG'
}

KODE = {
    's': 'S', 'sakit': 'S',
    'i': 'I', 'izin': 'I',
    'a': 'A', 'alpha': 'A',
    '.': '.'
}

# Skor kemiripan maksimum yang masih dianggap cocok (0.0 = sama, 1.0 = beda total)
SIM_THRESHOLD = 0.30


def norm(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    s = re.sub(r'(.)\1+', r'\1', s)
    return s


def levenshtein(a, b):
    if a == b:
        return 0
    la, lb = len(a), len(b)
    if la == 0:
        return lb
    if lb == 0:
        return la
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        for j in range(1, lb + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))
        prev = cur
    return prev[lb]


def skor_kemiripan(nc, nm):
    # nm = nama asli (dengan spasi); token dinormalisasi satu-satu
    kandidat_teks = [norm(nm)] + [norm(t) for t in nm.split()]
    terbaik = float('inf')
    for t in kandidat_teks:
        if not t:
            continue
        d = levenshtein(nc, t)
        ambang = max(2, min(3, len(nc) // 2))
        if d <= ambang:
            terbaik = min(terbaik, d / max(1, len(nc)))
        r = 1.0 - difflib.SequenceMatcher(None, nc, t).ratio()
        if r <= SIM_THRESHOLD:
            terbaik = min(terbaik, r)
        if terbaik == 0.0:
            break
    return terbaik if terbaik < float('inf') else None


def build_tanggal_map(ws):
    tanggal_to_col = {}
    for c in range(4, 50):
        tgl = ws.cell(6, c).value
        if tgl and str(tgl).isdigit():
            tanggal_to_col[int(tgl)] = c
    return tanggal_to_col


def cari_murid(ws, nama):
    nc = norm(nama)
    raw_low = nama.lower()
    kandidat = []  # (skor, row, nama)
    for row in range(7, 100):
        nama_murid = ws.cell(row, 3).value
        if not nama_murid or len(str(nama_murid).strip()) <= 1:
            continue
        nm = str(nama_murid).strip()
        nmn = norm(nm)
        nm_low = nm.lower()
        if nc == nmn or raw_low == nm_low:
            return row, nm, 0
        if nc in nmn or nmn in nc or raw_low in nm_low or nm_low in raw_low:
            return row, nm, 1
        skor = skor_kemiripan(nc, nm)
        if skor is not None and skor <= SIM_THRESHOLD:
            kandidat.append((round(skor, 3), row, nm))
    if not kandidat:
        return None, None, None
    kandidat.sort()
    skor_terbaik = kandidat[0][0]
    dekat = [k for k in kandidat if k[0] <= skor_terbaik + 0.05]
    nama_unik = {k[2] for k in dekat}
    if len(nama_unik) > 1:
        print(f"[WARNING] Beberapa kandidat mirip untuk '{nama}': "
              + ", ".join(f"{k[2]} (skor {k[0]})" for k in dekat))
        print("[SKIP] Tidak disimpan - cek nama lagi / pakai nama lengkap dari daftar.")
        return None, None, -1
    return kandidat[0][1], kandidat[0][2], 2


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

    col_tanggal = tanggal_map[int(tanggal)]
    kode = KODE.get(alasan.lower(), alasan.upper())

    row_ditemukan, nama_ditemukan, cara = cari_murid(ws, nama)

    if cara == -1:
        return
    if not row_ditemukan:
        print(f"[ERROR] Murid '{nama}' tidak ditemukan di kelas {kelas}")
        return

    ws.cell(row_ditemukan, col_tanggal).value = kode
    wb.save(FILE_PATH)

    match_type = {0: "tepat", 1: "substring", 2: "kemiripan"}[cara]
    print(f"[OK] {nama_ditemukan} ({sheet_name}) - Tanggal {tanggal} = {kode} [cocok {match_type}]")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0].lower().endswith('.xlsx'):
        FILE_PATH = args[0]
        args = args[1:]
    if len(args) < 4:
        print("Cara pakai: py absensi.py <nama> <kelas> <tanggal> <alasan>")
        print("Contoh: py absensi.py Aldrich TKa 18 sakit")
        print("Opsional: file path sebagai argumen pertama diikuti 4 data (atau env ABSENSI_FILE)")
        sys.exit(1)

    absen(args[0], args[1], args[2], args[3])