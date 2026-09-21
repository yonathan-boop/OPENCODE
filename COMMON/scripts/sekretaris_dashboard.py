"""Dashboard Sekretaris — baca CATATAN-AGENDA-SEKOLAH.md dan tampilkan via localhost.

Cara pakai:
    py COMMON/scripts/sekretaris_dashboard.py            # jalankan server (port default 8585)
    py COMMON/scripts/sekretaris_dashboard.py --check    # validasi parsing, tanpa server
    py COMMON/scripts/sekretaris_dashboard.py --port 9000

Buka: http://localhost:8585  (halaman auto-refresh tiap 60 detik)
Env:  SEKPORT untuk ganti port.
"""
import os
import re
import sys
import datetime
import http.server
import threading
from html import escape

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))            # COMMON/scripts
REPO = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))       # folder memory
AGENDA = os.path.join(REPO, "VS&OPENCODE", "CATATAN-AGENDA-SEKOLAH.md")
PORT = int(os.environ.get("SEKPORT", "8585"))

NAMA_BULAN = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
              7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
NAMA_HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

# Kata kunci penanda tenggat penting (highlight di dashboard)
KATA_PENTING = ["UTS", "US 1", "US 2", "ujian semester", "Natal", "PMKK", "Retreat", "retreat",
                "Rapor", "rapor", "nilai", "deadline", "laporan ke", "Hari pertama sekolah",
                "MPLS", "kenaikan kelas", "kumpul", "Surat undangan", "pembicara", "latihan Natal"]


def parse_int(s):
    return int(re.sub(r"\D", "", s)) if re.search(r"\d", s) else None


def ekstrak_tanggal(spec, bulan, tahun):
    """Terima spec tanggal -> list (date_mulai, date_akhir|None).
    - 7/7 tunggal · 1-10 rentang sebulan (1 entri) · 5-7/10 · 30/11-5/12 · 2,4,6/1 daftar hari
    """
    hasil = []
    spec = spec.strip()
    # rentang lintas bulan: 30/11-5/12
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})\s*[-–]\s*(\d{1,2})/(\d{1,2})", spec)
    if m:
        mulai = datetime.date(tahun, int(m.group(2)), int(m.group(1)))
        akhir = datetime.date(tahun, int(m.group(4)), int(m.group(3)))
        return [(mulai, akhir)]
    # rentang dalam satu bulan dgn slash di ujung: 14-19/9 · 5-7/10
    m = re.fullmatch(r"(\d{1,2})\s*[-–]\s*(\d{1,2})/(\d{1,2})", spec)
    if m:
        bln = int(m.group(3))
        return [(datetime.date(tahun, bln, int(m.group(1))),
                 datetime.date(tahun, bln, int(m.group(2))))]
    # rentang dalam satu bulan: 1-10 / 21-31 (satu entri)
    m = re.fullmatch(r"(\d{1,2})\s*[-–]\s*(\d{1,2})", spec)
    if m:
        return [(datetime.date(tahun, bulan, int(m.group(1))),
                 datetime.date(tahun, bulan, int(m.group(2))))]
    # daftar hari: 2,4,6
    m = re.fullmatch(r"(\d{1,2})(?:,(\d{1,2}))?(?:,(\d{1,2}))?", spec)
    if m:
        for g in m.groups():
            if g:
                d = datetime.date(tahun, bulan, int(g))
                hasil.append((d, None))
        return hasil
    # tunggal: 7/7
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})", spec)
    if m:
        return [(datetime.date(tahun, int(m.group(2)), int(m.group(1))), None)]
    return hasil


def parse_agenda(path):
    try:
        with open(path, encoding="utf-8") as f:
            txt = f.read()
    except OSError as e:
        print(f"Gagal baca {path}: {e}")
        sys.exit(1)

    blok = re.search(r"## JADWAL KERJA[^\n]*\n(.*?)(?=\n## |\Z)", txt, re.S)
    if not blok:
        print("Bagian 'JADWAL KERJA' tidak ditemukan di agenda file.")
        sys.exit(1)
    tubuh = blok.group(1)

    acara = []
    bulan = None
    tahun = None
    nama_ke_angka = {v: k for k, v in NAMA_BULAN.items()}
    for baris in tubuh.splitlines():
        mb = re.match(r"###\s+(\w+)\s+(\d{4})", baris)
        if mb:
            bulan = nama_ke_angka.get(mb.group(1))
            tahun = int(mb.group(2))
            continue
        me = re.match(r"-\s+(.+?)(?:\s*:\s*(.*))?$", baris)
        if me and bulan and tahun:
            spec, teks = me.group(1).strip(), me.group(2)
            tgls = ekstrak_tanggal(spec, bulan, tahun)
            judul = (teks or spec).strip()
            for mulai, akhir in tgls:
                acara.append({
                    "mulai": mulai,
                    "akhir": akhir,
                    "judul": judul,
                    "spec": spec,
                })
            # rantai tanggal di dalam teks: "22/9 penyerahan nilai → 24/9 laporan"
            if teks:
                for mt in re.finditer(r"(\d{1,2})/(\d{1,2})\s*([^→·|]*)", teks):
                    d, mo, seg = int(mt.group(1)), int(mt.group(2)), mt.group(3).strip(" :–-")
                    if not (1 <= mo <= 12) or not seg:
                        continue
                    try:
                        t = datetime.date(tahun, mo, d)
                    except ValueError:
                        continue
                    if any(t == a["mulai"] for a in acara):
                        continue
                    acara.append({"mulai": t, "akhir": None, "judul": seg, "spec": spec})
    return acara


def kategori(judul):
    j = judul.lower()
    if any(k in j for k in ["uts", "us 1", "us 2", "ujian semester"]):
        return "ujian"
    if "natal" in j:
        return "natal"
    if "pmkk" in j:
        return "pmkk"
    if "retreat" in j:
        return "retreat"
    if "rapor" in j or "nilai" in j or "laporan ke" in j or "deadline" in j:
        return "tenggat"
    if "libur" in j or "hari raya" in j or "natal" in j:
        return "libur"
    return "biasa"


def fmt_tgl(t):
    return f"{NAMA_HARI[t.weekday()]}, {t.day} {NAMA_BULAN[t.month]} {t.year}"


def fmt_tanggal(a):
    if a["akhir"] and a["akhir"] > a["mulai"]:
        return fmt_tgl(a["mulai"]) + " – " + fmt_tgl(a["akhir"])
    return fmt_tgl(a["mulai"])


def html_dashboard(acara, sekarang):
    hari_ini = sekarang.date()
    mendatang_h30 = [a for a in acara if hari_ini <= a["mulai"] <= hari_ini + datetime.timedelta(days=30)]
    mendatang_h30.sort(key=lambda a: (a["mulai"], a["judul"]))
    bulan_ini = [a for a in acara if a["mulai"].month == hari_ini.month and a["mulai"].year == hari_ini.year]
    semua = sorted(acara, key=lambda a: (a["mulai"], a["judul"]))

    def kartu(a):
        ket = kategori(a["judul"])
        bersih = re.sub(r"\*\*", "", a["judul"])
        return (f'<div class="kartu {ket}"><div class="tgl">{escape(fmt_tanggal(a))}</div>'
                f'<div class="judul">{escape(bersih)}</div></div>')

    h30 = "".join(kartu(a) for a in mendatang_h30) or "<div class='kosong'>Tidak ada acara dalam 30 hari ke depan.</div>"
    bl = "".join(kartu(a) for a in bulan_ini) or "<div class='kosong'>Tidak ada acara bulan ini.</div>"
    semua_blok = ""
    bulan_urut = sorted({(a["mulai"].year, a["mulai"].month) for a in semua}, key=lambda t: (t[0], t[1]))
    for y, m in bulan_urut:
        daftar = [a for a in semua if a["mulai"].year == y and a["mulai"].month == m]
        semua_blok += (f"<h3>{NAMA_BULAN[m]} {y}</h3>" + "".join(kartu(a) for a in daftar))

    catatan_urgent = []
    for a in (x for x in semua if hari_ini <= x["mulai"] <= hari_ini + datetime.timedelta(days=3)):
        catatan_urgent.append(f"• {a['mulai'].day}/{a['mulai'].month} — {escape(a['judul'])}")

    return f"""<!DOCTYPE html>
<html lang="id"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="60">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dashboard Sekretaris — Methodist 11</title>
<style>
:root {{ --navy:#1F2A57; --gold:#D9A441; --tint:#E8ECF5; --ink:#223; --ok:#2e7d32; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:'Segoe UI',Calibri,Arial,sans-serif; background:#f4f6fb; color:var(--ink); }}
header {{ background:var(--navy); color:#fff; padding:18px 28px; }}
header h1 {{ margin:0; font-size:20px; letter-spacing:.5px; }}
header .sub {{ opacity:.8; font-size:13px; margin-top:4px; }}
.wrap {{ max-width:1080px; margin:22px auto; padding:0 18px; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; }}
@media (max-width:760px) {{ .grid {{ grid-template-columns:1fr; }} }}
.panel {{ background:#fff; border:1px solid #e2e6f0; border-radius:10px; padding:16px 18px; }}
.panel h2 {{ margin:0 0 12px; font-size:14px; text-transform:uppercase; letter-spacing:.6px; color:var(--navy); border-bottom:2px solid var(--gold); padding-bottom:8px; }}
.urgent {{ background:#fff7e6; border:1px solid var(--gold); }}
.urgent ul {{ margin:0; padding-left:18px; font-size:14px; line-height:1.7; }}
.kartu {{ border-left:4px solid var(--navy); background:#fafbfe; border-radius:6px; padding:8px 12px; margin:8px 0; }}
.kartu .tgl {{ font-size:11px; color:#668; text-transform:uppercase; letter-spacing:.3px }}
.kartu .judul {{ font-size:14px; margin-top:2px; }}
.kartu.ujian {{ border-left-color:#1b6ca8; }}
.kartu.natal {{ border-left-color:#b23b3b; }}
.kartu.pmkk {{ border-left-color:#8e44ad; }}
.kartu.retreat {{ border-left-color:#1e8449; }}
.kartu.tenggat {{ border-left-color:var(--gold); }}
.kartu.libur {{ border-left-color:#9099aa; }}
.kosong {{ color:#899; font-size:13px; padding:10px 0; }}
h3 {{ font-size:13px; margin:18px 0 4px; color:var(--navy); text-transform:uppercase; letter-spacing:.5px; }}
footer {{ text-align:center; color:#899; font-size:12px; padding:22px; }}
</style></head>
<body>
<header>
<h1>Dashboard Sekretaris · SD/TK/SMP Methodist-11 Medan</h1>
<div class="sub">Update {fmt_tgl(sekarang)} — bersumber dari 'CATATAN-AGENDA-SEKOLAH.md' · auto-refresh 60 detik</div>
</header>
<div class="wrap">
<div class="grid">
<div class="panel urgent"><h2>3 hari ke depan</h2><ul>{"".join(catatan_urgent) or "<li>Tidak ada tenggat dalam 3 hari.</li>"}</ul></div>
<div class="panel"><h2>30 hari ke depan</h2>{h30}</div>
</div>
<div class="grid" style="margin-top:18px">
<div class="panel"><h2>Bulan berjalan · {NAMA_BULAN[hari_ini.month]} {hari_ini.year}</h2>{bl}</div>
<div class="panel"><h2>Bulan berikut · {NAMA_BULAN[hari_ini.month + 1] if hari_ini.month < 12 else 'Januari'}</h2></div>
</div>
<div class="panel" style="margin-top:18px"><h2>Semua agenda T.P. 2026-2027</h2>{semua_blok}</div>
<footer>File sumber: {escape(AGENDA)} · refresh otomatis tiap 60 detik setelah file diedit</footer>
</div>
</body></html>"""


def jalankan_check():
    acara = parse_agenda(AGENDA)
    sekarang = datetime.datetime.now()
    print(f"Parsed {len(acara)} acara dari {AGENDA}")
    for a in sorted(acara, key=lambda x: (x["mulai"], x["judul"]))[:12]:
        print(f"  {fmt_tanggal(a)}  [{kategori(a['judul'])}]  {a['judul'][:70]}")
    h = datetime.date.today()
    n30 = [a for a in acara if h <= a["mulai"] <= h + datetime.timedelta(days=30)]
    print(f"\nDalam 30 hari ke depan ({h} s/d {h + datetime.timedelta(days=30)}): {len(n30)} acara")
    for a in sorted(n30, key=lambda x: x["mulai"]):
        print(f"  {a['mulai'].day}/{a['mulai'].month}  {a['judul'][:70]}")


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            acara = parse_agenda(AGENDA)
        except SystemExit:
            acara = []
        body = html_dashboard(acara, datetime.datetime.now()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {fmt % args}\n")


def main():
    if "--check" in sys.argv:
        jalankan_check()
        return
    if "--port" in sys.argv:
        global PORT
        PORT = int(sys.argv[sys.argv.index("--port") + 1])
    acara = parse_agenda(AGENDA)
    print(f"Dashboard Sekretaris — {len(acara)} acara dimuat.")
    print(f"Buka: http://localhost:{PORT}  (Ctrl+C untuk stop)")
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard dihentikan.")


if __name__ == "__main__":
    main()