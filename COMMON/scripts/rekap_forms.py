"""Rekap nilai kuis Google Forms -> Excel siap cetak.

Baca CSV hasil "Respons" -> "Download responses (.csv)" (atau link publish-to-web
CSV dari Google Sheets yang ditautkan ke Form), hitung skor + persentase,
petakan predikat (ambang KKTP), lalu tulis workbook Excel rapi dengan lapisan
cetak (configure_printing, pola LRN-20260924-003).

Cara pakai:
    py rekap_forms.py respons.csv [--out rekap-kuis.xlsx] [--kkpt 90,75,60]

Catatan penting (lihat LRN-20260924-005):
- Sel skor dari Form ber-kuis sering muncul "7/10" (bukan angka) -> script ini
  men-parse otomatis format "N/T".
- Kolom identitas dideteksi otomatis: kolom pertanyaan pertama yang header-nya
  mengandung "Nama", fallback ke kolom email, fallback terakhir "Responden N".
"""
import argparse
import csv
import sys

import openpyxl
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

DEFAULT_KKTP = [("Sangat Baik", 90), ("Baik", 75), ("Cukup", 60)]


def configure_printing(ws):
    ws.print_area = f"A1:{get_column_letter(ws.max_column)}{ws.max_row}"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.print_options.horizontalCentered = True
    ws.print_title_rows = "1:1"
    ws.oddFooter.center.text = "&P / &N"


def detect_columns(headers):
    ts = next((i for i, h in enumerate(headers) if "timestamp" in h.lower()), 0)
    email = next((i for i, h in enumerate(headers) if "email" in h.lower()), None)
    score = next(
        (i for i, h in enumerate(reversed(headers))
         if any(k in h.lower() for k in ("score", "skor", "hasil"))),
        None,
    )
    score = len(headers) - 1 - score if score is not None else None
    nama = next(
        (i for i, h in enumerate(headers)
         if i not in (ts, score) and i != email and "ama" in h.lower()),
        None,
    )
    return ts, email, score, nama


def parse_score(cell):
    if cell is None:
        return None, None
    s = str(cell).strip()
    if "/" in s:
        num, _, tot = s.partition("/")
        try:
            return float(num), float(tot)
        except ValueError:
            return None, None
    try:
        return float(s), None
    except ValueError:
        return None, None


def predikat(persen, kktp):
    for label, ambang in kktp:
        if persen >= ambang:
            return label
    return "Perlu Bimbingan"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    ap = argparse.ArgumentParser(description="Rekap nilai kuis Google Forms dari CSV -> Excel")
    ap.add_argument("csv_path", help="CSV respons Forms (Download responses .csv)")
    ap.add_argument("--out", default=None, help="Nama file Excel output (default: <csv>.rekap.xlsx)")
    ap.add_argument("--kktp", default=None, help="Ambang predikat, format 'SB_ambang,BAIK_ambang,CUKUP_ambang' (default 90,75,60)")
    args = ap.parse_args()

    if args.kktp:
        ambang = [float(x) for x in args.kktp.split(",")]
        if len(ambang) != 3:
            sys.exit("[ERROR] --kktp butuh 3 nilai: SB,BAIK,CUKUP (mis. 90,75,60)")
        kktp = [("Sangat Baik", ambang[0]), ("Baik", ambang[1]), ("Cukup", ambang[2])]
    else:
        kktp = DEFAULT_KKTP

    with open(args.csv_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if len(rows) < 2:
        sys.exit("[ERROR] CSV kosong/hanya header.")

    headers = [h.strip() for h in rows[0]]
    ts_i, email_i, score_i, nama_i = detect_columns(headers)
    out = args.out or args.csv_path.rsplit(".", 1)[0] + ".rekap.xlsx"

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Rekap"
    ws.append(["No", "Waktu", "Identitas", "Skor", "Total", "Persen", "Predikat"])
    bold = Font(bold=True)
    for c in ws[1]:
        c.font = bold
        c.alignment = Alignment(horizontal="center")

    n = 0
    no_score = 0
    for row in rows[1:]:
        if not any(cell.strip() for cell in row if cell):
            continue
        ident = row[nama_i].strip() if nama_i is not None and nama_i < len(row) else ""
        if email_i is not None and email_i < len(row) and row[email_i].strip():
            ident = f"{ident} ({row[email_i].strip()})" if ident else row[email_i].strip()
        if not ident:
            ident = f"Responden {n + 1}"
        cell = row[score_i] if score_i is not None and score_i < len(row) else None
        num, tot = parse_score(cell)
        if num is None:
            no_score += 1
            ws.append([n + 1, row[ts_i] if ts_i < len(row) else "", ident, cell or "", "", "-", "-"])
        else:
            persen = (num / tot * 100) if tot else num
            ws.append([n + 1, row[ts_i] if ts_i < len(row) else "", ident,
                       round(num, 2) if num == int(num) else num,
                       int(tot) if tot else "", round(persen, 1) if persen != int(persen) else int(persen),
                       predikat(persen, kktp)])
        n += 1

    ws.column_dimensions["A"].width = 5
    ws.column_dimensions["B"].width = 20
    ws.column_dimensions["C"].width = 40
    for col in ("D", "E", "F", "G"):
        ws.column_dimensions[col].width = 12
    configure_printing(ws)

    detail = wb.create_sheet("Detail")
    detail.append(headers)
    for row in rows[1:]:
        if any(cell.strip() for cell in row if cell):
            detail.append(row)
    configure_printing(detail)

    wb.save(out)
    print(f"OK: {n} respons diproses -> {out}")
    print(f"  Kolom terdeteksi: Waktu=col{ts_i + 1}, Email={'col' + str(email_i + 1) if email_i is not None else '-'}, "
          f"Nama={'col' + str(nama_i + 1) if nama_i is not None else '-'}, Skor={'col' + str(score_i + 1) if score_i is not None else '-'}")
    print(f"  Predikat (ambang %): {kktp}")
    if no_score:
        print(f"  PERINGATAN: {no_score} baris tanpa skor valid (mungkin belum dinilai / bukan kuis).")


if __name__ == "__main__":
    main()