# SEO & Google Search Console — Website Methodist-11

Di-update: 21 September 2026 (linux-tablet / Poco X7 Pro)

---

## Status

| Item | Status |
|------|--------|
| Website live (methodist-11.my.id → 200) | ✅ |
| sitemap.xml (17 URL) | ✅ live |
| robots.txt (blokir /rpp/, rujuk sitemap) | ✅ live |
| Title + meta description per halaman | ✅ |
| Canonical URL | ✅ all |
| Open Graph + Twitter card | ✅ all |
| JSON-LD (School + EducationalOrganization) | ✅ index.html |
| Google Search Console verifikasi | ⏳ BELUM — butuh login Google user |
| Submit sitemap di GSC | ⏳ BELUM |

---

## Yang Sudah Dikerjakan (21 Sept 2026)

### 1. sitemap.xml
- `COMMON/project-sd-methodist-11/sitemap.xml` — 17 URL (index, pages/, sub-pages kegiatan/pengumuman/galeri). Prioritas 1.0–0.5, lastmod 2026-09-21.
- `/rpp/` sengaja TIDAK masuk sitemap (alasan keamanan, ada Gemini key tertanam di halaman itu).

### 2. robots.txt
- Allow semua, `Disallow: /rpp/`, referensi `Sitemap: https://methodist-11.my.id/sitemap.xml`.

### 3. SEO on-page
- **index.html**: title jadi `SD Methodist 11 Medan | TK-SD-SMP Swasta Kristen Methodist Titus` + meta description, robots, canonical, theme-color, OG, Twitter card, JSON-LD School (alamat Medan Johor, geo 3.5271/98.6891, sosial media Facebook/Instagram/YouTube).
- **16 halaman** pages/ (kalender, kegiatan, galeri, pengumuman + semua sub): description + canonical + OG + Twitter card.
- Sitemap/robots diserve langsung dari folder project → nggak perlu reload server (serve8090.js baca file per request).

### 4. Verifikasi live
- `localhost:8090` dan `https://methodist-11.my.id` semua 200.
- Deployment: file langsung nempel di folder project, nginx/cloudflared tidak perlu restart.

---

## CARA FINISH GSC (butuh user — wajib login Google)

Google Search Console **tidak bisa diverifikasi 100% otomatis** — butuh akses akun Google pemilik.
Sisanya (upload file, cek status) bisa dibantu. Langkah paling cepat:

1. Buka **https://search.google.com/search-console** → login Google.
2. Klik **Add property** → pilih **URL prefix** → ketik `https://methodist-11.my.id`.
3. Pilih metode **HTML file** — Google kasih nama file `google-site-verification-XXXX.html`.
4. **Copy token itu ke asisten** → asisten buat file `google-site-verification-XXXX.html` di `COMMON/project-sd-methodist-11/` (langsung live).
5. Klik **Verify** di GSC (status bisa di-cek asisten: `curl https://methodist-11.my.id/google-site-verification-XXXX.html` → 200).
6. Buka **Sitemaps** di menu (URL prefix property) → submit `sitemap.xml`.
7. Cek **URL Inspection** → masukkan `https://methodist-11.my.id/` → Request Indexing.

Alternatif verifikasi:
- **DNS TXT**: butuh dashboard Cloudflare (record TXT dari GSC) — arahkan user ke Cloudflare.
- **Service Account API**: kalau mau full-otomatis, user generate JSON service account + aktifkan Search Console API, extend asisten dengan Google API scope.

---

## Keyword Target (search intent user)

- `sd methodist 11 medan`
- `sekolah kristen medan`
- `ppdb sd medan 2026`
- `tk sd smp swasta medan johor`
- `penerimaan murid baru medan 2026`

Semua keyword sudah direfleksikan di title + meta description halaman utama.

---

## Catatan Teknis
- Server: serve8090.js (Node, port 8090) → nginx 8081 → cloudflared tunnel (name "Linux HP" → 8090).
- RPP generator (rpp/) sengaja diblokir dari indeks (GFE secret key tertanam di HTML). Lihat `GENERATOR-RPP-METHODIST.md`.