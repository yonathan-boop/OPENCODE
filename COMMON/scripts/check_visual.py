#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_visual.py - Gemini vision sebagai "mata" untuk memeriksa hasil render dokumen.
Kegunaan: validasi visual hasil edit docx/xlsx/pdf yang tidak bisa kita lihat langsung,
persis seperti yang dilihat mata manusia.

Cara pakai:
  py check_visual.py "path\gambar.png" ["pertanyaan tambahan"]
  py check_visual.py --dir "path\folder"    # pakai semua gambar di folder

API key dibaca dari:  ~/.config/opencode/secrets/gemini.env  (di luar git, jangan pernah di-commit)
Model default: gemini-3.6-flash  (bisa ganti via env GEMINI_MODEL)

Exit code 0 = sukses, 1 = error.
"""

import base64, glob, json, os, sys, time, urllib.request, urllib.error

def load_key():
    candidates = [
        os.path.join(os.path.expanduser("~"), ".config", "opencode", "secrets", "gemini.env"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "secrets", "gemini.env"),
    ]
    for p in candidates:
        try:
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("GEMINI_API_KEY="):
                        v = line.split("=", 1)[1].strip().strip('"').strip("'")
                        if v:
                            return v
        except OSError:
            continue
    return None

def ask_vision(key, image_path, prompt, model="gemini-3.6-flash"):
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    mime = "image/png"
    if image_path.lower().endswith((".jpg", ".jpeg")):
        mime = "image/jpeg"
    elif image_path.lower().endswith((".png",)):
        mime = "image/png"
    payload = {"contents": [{"parts": [
        {"text": prompt},
        {"inline_data": {"mime_type": mime, "data": img_b64}},
    ]}]}
    url = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent?key=%s" % (model, key)
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    import time
    for attempt in range(4):
        try:
            resp = urllib.request.urlopen(req, timeout=90)
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and attempt < 3:
                time.sleep(6 * (attempt + 1))
                continue
            return None, "HTTP %d: %s" % (e.code, e.read().decode()[:400])
    else:
        resp = None
    if resp is None:
        return None, "Gagal setelah 4 percobaan (rate limit/overload)"
    data = json.loads(resp.read().decode())
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"], None
    except (KeyError, IndexError):
        return None, "Format respons tidak dikenal: %s" % json.dumps(data)[:300]

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass  # Python lama tanpa reconfigure
    key = load_key()
    if not key:
        print("ERROR: GEMINI_API_KEY tidak ditemukan. Isi dulu ~/.config/opencode/secrets/gemini.env")
        return 1
    model = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")
    args = sys.argv[1:]
    prompt = args[-1] if args and (" " in args[-1] or "?" in args[-1] or "periksa" in args[-1] or "baca" in args[-1]) else None
    files = []
    if not args:
        print("Cara pakai: py check_visual.py <gambar> [prompt]")
        return 1
    if args[0] == "--dir":
        if len(args) < 2:
            print("Butuh folder: py check_visual.py --dir <folder>")
            return 1
        d = args[1]
        files = sorted(glob.glob(os.path.join(d, "*.png")) + glob.glob(os.path.join(d, "*.jpg")) + glob.glob(os.path.join(d, "*.jpeg")))
        prompt = args[2] if len(args) > 2 else None
    else:
        files = [a for a in args if not a.startswith("-") and os.path.exists(a)]
        prompt = args[-1] if args and not os.path.exists(args[-1]) else None
    if not files:
        print("Tidak ada gambar valid.")
        return 1
    default_prompt = "Periksa gambar ini sebagai penyemak kualitas. Sebutkan semua teks yang terlihat secara urut. " \
                     "Tandai bila ada masalah: teks terpotong, tumpang tindih, nomor soa dobel, tabel rusak, font aneh, posisi tidak rapi. " \
                     "Pertahankan penilaian menjadi: OK atau MASALAH + daftar detail."
    for f in files:
        print("=" * 60)
        print("GAMBAR:", os.path.basename(f))
        ans, err = ask_vision(key, f, prompt or default_prompt, model)
        if err:
            print("ERROR:", err)
            return 1
        print(ans)
    return 0

if __name__ == "__main__":
    sys.exit(main())