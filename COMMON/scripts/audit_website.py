#!/usr/bin/env python3
"""audit_website.py — audit cepat website sekolah statis (READ-ONLY, tidak mengubah apa pun).

Cek yang dilaporkan per halaman .html:
  - bobot gambar yang direferensikan (KB) +的图片 utama tanpa loading="lazy"
  - <img> tanpa width/height  -> penyebab layout bergeser (CLS)
  - <img> tanpa alt
  - <picture>/srcset (apakah sudah pakai format modern)
  - JSON-LD schema.org, og:image, canonical, title, description
Bonus:
  - celah MIME di serve8090.js (mis. .avif belum terdaftar)
  - pola path traversal di server statis (path.join tanpa guard)

Contoh:
  py audit_website.py "COMMON\\rancangan-website-v2"
  py audit_website.py "COMMON\\project-sd-methodist-11" --server serve8090.js
"""
import argparse
import os
import re
import sys

IMG_RE = re.compile(r"<img\b[^>]*>", re.I | re.S)
SRC_RE = re.compile(r'(?:src|data-src)="([^"]+\.(?:jpg|jpeg|png|webp|avif|gif|svg))"', re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"', re.I)
CANON_RE = re.compile(r'<link\s+rel="canonical"', re.I)
OGIMG_RE = re.compile(r'property="og:image"', re.I)
JSONLD_RE = re.compile(r'application/ld\+json', re.I)


def human(n):
    for unit in ("B", "KB", "MB"):
        if n < 1024 or unit == "MB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def audit_html(path, root):
    txt = open(path, "r", encoding="utf-8", errors="replace").read()
    rel = os.path.relpath(path, root)
    imgs = IMG_RE.findall(txt)
    weight = 0
    missing = []
    for src in SRC_RE.findall(txt):
        p = src.split("?")[0]
        if p.startswith(("http://", "https://", "//", "data:")):
            continue
        fp = os.path.normpath(os.path.join(os.path.dirname(path), p.lstrip("/")))
        if os.path.isfile(fp):
            weight += os.path.getsize(fp)
    for tag in imgs:
        prob = []
        if not re.search(r'\bwidth=', tag, re.I):
            prob.append("no-width")
        if not re.search(r'\bheight=', tag, re.I):
            prob.append("no-height")
        if not re.search(r'\balt=', tag, re.I):
            prob.append("no-alt")
        if not re.search(r'loading="lazy"', tag, re.I):
            prob.append("eager")
        if prob:
            missing.append((tag[:110], prob))
    return {
        "rel": rel,
        "imgs": len(imgs),
        "weight": weight,
        "problems": missing,
        "title": bool(TITLE_RE.search(txt)),
        "desc": bool(DESC_RE.search(txt)),
        "canon": bool(CANON_RE.search(txt)),
        "ogimg": bool(OGIMG_RE.search(txt)),
        "jsonld": bool(JSONLD_RE.search(txt)),
        "picture": "<picture" in txt.lower(),
    }


def audit_server(server_path):
    notes = []
    try:
        js = open(server_path, "r", encoding="utf-8", errors="replace").read()
    except OSError as e:
        return [f"tidak bisa baca {server_path}: {e}"]
    for ext in (".avif", ".webp", ".woff2", ".woff", ".mp4", ".m4a"):
        if ext not in js:
            notes.append(f"MIME untuk '{ext}' tidak terdaftar di server")
    if not re.search(r"startsWith\(\s*ROOT", js) and not re.search(r"\.startsWith\(", js):
        notes.append("tidak ada guard path (tidak startsWith(ROOT)) -> path traversal Risk")
    if "path.join(ROOT" in js and "startsWith" not in js:
        notes.append("path.join(ROOT, p) tanpa pemeriksaan batas -> path traversal Risk")
    if "ETag" not in js:
        notes.append("tidak ada ETag/Last-Modified -> browser tak bisa 304, unduh ulang tiap kunjungan")
    if "Cache-Control" not in js:
        notes.append("tidak ada Cache-Control")
    if "nosniff" not in js:
        notes.append("tidak ada X-Content-Type-Options: nosniff")
    if "createReadStream" not in js:
        notes.append("file dibaca fs.readFile (penuh ke RAM) — ganti createReadStream")
    return notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--server", default="", help="path ke serve8090.js untuk audit server")
    ap.add_argument("--min-weight", type=int, default=800, help="ambang peringatan bobot gambar (KB)")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    root = os.path.abspath(a.root)
    if not os.path.isdir(root):
        print(f"FOLDER TIDAK ADA: {root}")
        return 1
    pages = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in {"assets", "node_modules", ".git", "thumbs"}]
        for f in fn:
            if f.lower().endswith(".html"):
                pages.append(os.path.join(dp, f))
    pages.sort()
    if not pages:
        print("Tidak ada .html ditemukan")
        return 0

    print(f"AUDIT {root}  ({len(pages)} halaman)\n")
    hdr = f"{'halaman':<44}{'img':>5}{'bobot':>10}{'masalah':>9}  seo"
    print(hdr)
    print("-" * len(hdr))
    total_w = 0
    total_p = 0
    for p in pages:
        r = audit_html(p, root)
        total_w += r["weight"]
        total_p += len(r["problems"])
        seo = "".join([
            "T" if r["title"] else "-",
            "D" if r["desc"] else "-",
            "C" if r["canon"] else "-",
            "O" if r["ogimg"] else "-",
            "J" if r["jsonld"] else "-",
        ])
        wflag = "*" if r["weight"] / 1024 >= a.min_weight else " "
        print(f"{r['rel'][:43]:<44}{r['imgs']:>5}{human(r['weight']):>9}{wflag}{len(r['problems']):>6}  {seo}")
    print("-" * len(hdr))
    print(f"{'TOTAL':<44}{'':>5}{human(total_w):>9}{'':>7}  {total_p} masalah tag <img>")

    print("\nDETAIL (10 contoh masalah tag <img>):")
    shown = 0
    for p in pages:
        r = audit_html(p, root)
        for tag, prob in r["problems"]:
            if shown >= 10:
                break
            print(f"  {r['rel']}  [{','.join(prob)}]")
            print(f"    {tag}...")
            shown += 1
    if total_p == 0:
        print("  (nihil — semua <img> punya width/height/alt/lazy)")

    print("\nSEO: T=title D=description C=canonical O=og:image J=JSON-LD schema.org")
    print("Catatan: gambar tanpa width/height = layout bergeser (CLS) saat gambar masuk.")
    print("Bobot gambar = total byte file yang direferensikan halaman tsb (belum dipotong lazy-load).")

    if a.server:
        print(f"\nSERVER {a.server}:")
        notes = audit_server(a.server)
        print("  semua OK" if not notes else "\n".join("  - " + n for n in notes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
