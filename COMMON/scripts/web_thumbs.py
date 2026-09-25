#!/usr/bin/env python3
"""web_thumbs.py — buat thumbnail responsif untuk gambar website sekolah (Pillow).

Tujuan: galeri foto sekolah (puluhan ratus foto WhatsApp) sekarang memuat file
1600px penuh untuk tiap thumb. Di HP itu boros kuota. Script ini membuat varian
480/800/1200px (WebP + fallback JPEG) sehingga halaman bisa pakai <picture>.

Contoh:
  py web_thumbs.py "COMMON\\rancangan-website-v2\\assets\\images"
  py web_thumbs.py "<folder>" --apply
  py web_thumbs.py "<folder>" --html assets/images/galeri/imlek/imlek-001.jpg
  py web_thumbs.py "<folder>" --min-savings 5        # hanya yang untung >=5%

Default = DRY RUN (tidak menulis apa pun). Wajib --apply untuk menulis.
"""
import argparse
import os
import sys
from PIL import Image

IMG_EXT = {".jpg", ".jpeg", ".png", ".webp"}
SKIP_DIR = {"thumbs"}
WIDTHS = (480, 800, 1200)
WEBP_Q = 74
JPG_Q = 78


def human(n):
    for unit in ("B", "KB", "MB"):
        if n < 1024 or unit == "MB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def variants(im, widths):
    w, h = im.size
    return [(x, round(h * x / w)) for x in widths if x < w]


def build(path, outdir, apply=False):
    src = os.path.getsize(path)
    made = []
    with Image.open(path) as im:
        im.load()
        rgb = im.convert("RGB")
        w0, h0 = rgb.size
        for w, h in variants(rgb, WIDTHS):
            small = rgb.resize((w, h), Image.LANCZOS)
            wp = os.path.join(outdir, f"{w}-{os.path.splitext(os.path.basename(path))[0]}.webp")
            jp = os.path.join(outdir, f"{w}-{os.path.splitext(os.path.basename(path))[0]}.jpg")
            if apply:
                small.save(wp, "WEBP", quality=WEBP_Q, method=4)
                small.save(jp, "JPEG", quality=JPG_Q, optimize=True, progressive=True)
            made.append((w, h, wp, jp))
    return src, (w0, h0), made


def html_snippet(path, base_rel, sizes="(max-width: 640px) 100vw, 33vw", alt=""):
    """Markup <picture> yang benar: webp via <source>, jpeg di <img> (fallback)."""
    with Image.open(path) as im:
        w0, h0 = im.size
    vs = [x for x in WIDTHS if x < w0]
    if not vs:
        vs = [w0]
    stem = os.path.splitext(base_rel)[0]
    srcset = ", ".join(f"/assets/images/thumbs/{x}-{os.path.basename(stem)}.webp {x}w" for x in vs)
    jset = ", ".join(f"/assets/images/thumbs/{x}-{os.path.basename(stem)}.jpg {x}w" for x in vs)
    big = max(vs)
    bh = round(h0 * big / w0)
    return (
        f'<picture>\n'
        f'  <source type="image/webp" srcset="{srcset}" sizes="{sizes}">\n'
        f'  <img src="/assets/images/thumbs/{big}-{os.path.basename(stem)}.jpg" srcset="{jset}"\n'
        f'       sizes="{sizes}" width="{big}" height="{bh}" alt="{alt}" loading="lazy"\n'
        f'       decoding="async" style="aspect-ratio:{big}/{bh}">\n'
        f'</picture>'
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--apply", action="store_true", help="tulis file (default dry-run)")
    ap.add_argument("--out", default="thumbs", help="subfolder output (default: thumbs)")
    ap.add_argument("--html", help="path gambar, cetak markup <picture>")
    ap.add_argument("--min-savings", type=float, default=0, help="skip bila hemat < N%%")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    if a.html:
        print(html_snippet(a.html, a.html, alt=os.path.splitext(os.path.basename(a.html))[0]))
        return 0

    root = os.path.abspath(a.folder)
    if not os.path.isdir(root):
        print(f"FOLDER TIDAK ADA: {root}")
        return 1
    outdir = os.path.join(root, a.out)
    if a.apply:
        os.makedirs(outdir, exist_ok=True)

    files = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIR]
        for f in fn:
            if os.path.splitext(f)[1].lower() in IMG_EXT:
                files.append(os.path.join(dp, f))
    files.sort()
    if a.limit:
        files = files[: a.limit]

    print(f"Mode: {'APPLY -> ' + outdir if a.apply else 'DRY-RUN (tidak menulis file)'}")
    print(f"{len(files)} gambar\n")
    total_src = 0
    total_new = 0
    skipped = 0
    for i, f in enumerate(files, 1):
        try:
            src, dim, made = build(f, outdir, a.apply)
        except Exception as e:
            print(f"  GAGAL {os.path.basename(f)}: {e}")
            continue
        if not made:
            skipped += 1
            continue
        newsize = 0
        for w, h, wp, jp in made:
            newsize += (os.path.getsize(wp) if a.apply else 0) or 0
            newsize += (os.path.getsize(jp) if a.apply else 0) or 0
        total_src += src
        total_new += newsize
        pct = (100 - 100 * newsize / src) if (a.apply and newsize) else None
        flag = ""
        if pct is not None and pct < a.min_savings:
            flag = f"  (hemat {pct:.0f}% < {a.min_savings}% -> skip)"
        print(f"[{i}/{len(files)}] {os.path.relpath(f, root)}  {dim[0]}x{dim[1]} {human(src)}"
              + (f" -> varian {human(newsize)} (-{pct:.0f}%){flag}" if pct is not None else ""))
    print()
    if a.apply and total_new:
        print(f"TOTAL asal {human(total_src)} -> varian (webp+jpeg) {human(total_new)}"
              f"  (-{100 - 100 * total_new / total_src:.0f}%)")
        print("Catatan: browser hanya ambil 1 format per <source>, jadi angka asli")
        print("yg dilihat user ~50% dari total (yaitu sisi WebP saja).")
    else:
        print("Jalankan ulang dengan --apply untuk menulis file.")
    if skipped:
        print(f"{skipped} gambar dilewati (ukuran asal sudah <= lebar varian terkecil).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
