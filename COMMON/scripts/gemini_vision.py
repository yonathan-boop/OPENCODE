#!/usr/bin/env python3
"""Gemini sebagai 'mata' AI — analisa gambar/screenshot, atau jawab teks.

Cara pakai:
  python3 gemini_vision.py <gambar.png|jpg> ["pertanyaan"]      # lihat gambar
  python3 gemini_vision.py --text "pertanyaan"                  # teks saja (tanpa gambar)
  python3 gemini_vision.py --models                               # daftar model yang dipakai

Kunci API dibaca dari $GEMINI_API_KEY atau file /root/.config/gemini-api-key
(di luar git, aman). Model default: $GEMINI_MODEL atau gemini-2.5-flash.
Output = jawaban model sebagai teks di stdout.
"""
import base64
import json
import mimetypes
import os
import sys
import urllib.request
import urllib.error

KEY_FILE = "/root/.config/gemini-api-key"
FALLBACK_MODELS = ["gemini-3.6-flash", "gemini-2.5-flash", "gemini-2.0-flash"]


def get_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key and os.path.exists(KEY_FILE):
        key = open(KEY_FILE).read().strip()
    if not key:
        sys.exit("[ERROR] GEMINI_API_KEY tidak ditemukan (env atau {}".format(KEY_FILE))
    return key


def call_gemini(parts, model, key):
    body = {"contents": [{"parts": parts}]}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           "{}:generateContent?key={}".format(model, key))
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        code = e.code
        if code in (400, 404):
            return None, e.read().decode()[:200]
        raise
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"], None
    except (KeyError, IndexError):
        return None, json.dumps(data)[:300]


def main():
    args = sys.argv[1:]
    if not args or "--help" in args or "-h" in args:
        print(__doc__)
        sys.exit(0)
    if args[0] == "--models":
        key = get_key()
        for m in FALLBACK_MODELS:
            print(m)
        sys.exit(0)
    if args[0] == "--text":
        prompt = " ".join(args[1:]) or "Jawab singkat."
        key = get_key()
        model = os.environ.get("GEMINI_MODEL", FALLBACK_MODELS[0])
        txt, err = call_gemini([{"text": prompt}], model, key)
        if txt is None and err is not None:
            for alt in FALLBACK_MODELS[1:]:
                if alt == model:
                    continue
                txt, _ = call_gemini([{"text": prompt}], alt, key)
                if txt:
                    break
        if not txt:
            sys.exit("[ERROR] Gemini gagal: " + (err or "tanpa output"))
        print(txt)
        sys.exit(0)

    img_path = args[0]
    prompt = " ".join(args[1:]) or "Jelaskan isi gambar ini."
    if not os.path.exists(img_path):
        sys.exit("[ERROR] File gambar tidak ada: " + img_path)
    mime = mimetypes.guess_type(img_path)[0] or "image/png"
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    key = get_key()
    model = os.environ.get("GEMINI_MODEL", FALLBACK_MODELS[0])
    parts = [
        {"inline_data": {"mime_type": mime, "data": b64}},
        {"text": prompt},
    ]
    txt, err = call_gemini(parts, model, key)
    if txt is None and err is not None:
        for alt in FALLBACK_MODELS[1:]:
            txt, _ = call_gemini(parts, alt, key)
            if txt:
                break
    if not txt:
        sys.exit("[ERROR] Gemini gagal: " + (err or "tanpa output"))
    print(txt)


if __name__ == "__main__":
    main()