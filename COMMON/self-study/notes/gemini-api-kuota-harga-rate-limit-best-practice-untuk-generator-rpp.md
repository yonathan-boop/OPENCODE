# Gemini API: Kuota, Harga, Rate Limit & Best Practice untuk GENERATOR-RPP

**Tanggal riset:** 17 September 2026 (SERVER, self-study)
**Sumber primer:** ai.google.dev docs (pricing, rate-limits, models, free-tier) + verifikasi ai-api-hub.com 14/9/2026.

Model yang relevan untuk GENERATOR-RPP saat ini: **`gemini-3.6-flash`** (dipakai GENERATOR-RPP.html & skrip vision). Update Juli 2026, stable.

## Ringkasan

- **Harga Gemini 3.6 Flash (per 1 juta token, USD):**
  - **Free tier:** input & output GRATIS. Cocok untuk sekolah kecil / percobaan.
  - **Paid:** input **$0.75** (sampai 31/12/2026) → **$1.50** mulai 1/1/2027. Output (termasuk token thinking) **$3.75** → **$7.50** per 1/1/2027. Context caching input $0.075→$0.15, penyimpanan $0.50/1jt token/jam → $1.00. Batch input $0.375 / output $1.875 (diskon ~50%, tapi **tidak tersedia di free tier**).
  - Naik harga berlaku 1 Januari 2027 — kalau mau hemat, perkirakan biaya saat beralih ke paid.
- **Rate limit:** diukur per **proyek** (bukan per API key; bikin key baru TIDAK menambah kuota). Tiga dimensi: **RPM** (request/menit), **TPM** (token input/menit), **RPD** (request/hari, reset tengah malam Pacific). Limit per model + per usage tier; angka pasti lihat di AI Studio → Projects (limit spesifik tidak dijamin statis & bisa berubah otomatis).
- **Usage tier (naik otomatis):** Free (proyek aktif) → Tier 1 (link billing, cap $250) → Tier 2 (bayar ≥$100 + 3 hari) → Tier 3 (bayar ≥$1.000 + 30 hari). Cap billing: $250 / $2.000 / $20.000–100.000+.
- **Spend-based limit** (rolling 10 menit): Tier 1 = $10, Tier 2 = $50, Tier 3 = $200. Free: N/A. Jika kena → `429 RESOURCE_EXHAUSTED`.
- **Token limit model:** input 1.048.576 (1M), output 65.536. Cukup untuk prompt RPP.
- **Batch API (3.6 Flash):** enqueued tokens per tier — Tier 1: 3M, Tier 2: 400M, Tier 3: 1B. Untuk pekerjaan massal tidak-urgent (mis. bikin 50 RPP sekaligus), batch = setengah harga + kuota lebih nyaman.
- **Data usage:** free tier → data dipakai Google untuk meningkatkan produk ("Ya"); paid tier → tidak. Untuk data pribadi sekolah, pertimbangkan paid jika sensitif.

## Poin praktis untuk admin sekolah

- `gemini-3.6-flash` + **free tier cukup untuk pemakaian GENERATOR-RPP** (bikin beberapa RPP/hari, sekali klik per RPP — jauh di bawah RPM/TPD). Tidak perlu bayar dulu.
- **Jangan embed API key di HTML/JS frontend** (GENERATOR-RPP.html) — key bisa ke-extract dari source, dan pernah kena blokir Google "leaked" (lihat LRN-20260917-001). Best practice untuk prod: key di sisi **server** (backend/script Python) + proxy endpoint, atau baca dari env var / file di luar git (`~/.config/opencode/secrets/gemini.env` di PC; `/root/.config/gemini-api-key` di server).
- **Limit per proyek:** kalau GENERATOR-RPP dan skrip vision (check_visual.py / gemini_vision.py) pakai key di proyek yang sama, mereka **share kuota** — total pemakaian digabung.
- Cek kuota real-time: https://aistudio.google.com/projects → pilih proyek → lihat rate limit per model.
- Kalau suatu saat butuh banyak RPP sekaligus → pakai **Batch API** (50% biaya, kuota lebih besar) atau naik tier.
- Grounding Google Search: 500 RPD gratis (Flash/Flash-Lite) di free; Gemini 3: 5.000 pencarian/bulan gratis (akumulasi semua model Gemini 3), lalu $14/1.000. Maps grounding tidak tersedia gratis di 3.6 Flash.
- Simpan tanggal riset ini: harga berubah (naik besar 1/1/2027), limit bisa berubah — teliti ulang sebelum memutuskan paid.

## Jebakan / error umum

- **`429 RESOURCE_EXHAUSTED`** = kuota/rate limit tersisa. Bukan bug script. Solusi: tunggu & retry (exponential backoff + jitter, bounded), kecilkan context/output, atau naik tier. Jangan membabi buta ganti API key — kuota scope-nya proyek.
- **403 "API key leaked"** = key pernah masuk repo/commit → Google blokir permanen. Tidak bisa dibuka lagi; bikin key baru & pastikan tidak pernah masuk git/git history (Push Protection).
- **Jangan retry error 400/403 (permission)** — perbaiki dulu konfigurasi/kunci; retry hanya untuk error temporer.
- Mengejar RPM dengan menambah worker/key baru di proyek yang sama **tidak menambah throughput** — kuota shared.
- Free tier tapi kirim **data pribadi siswa** = data bisa dipakai Google untuk training. Hindari data sensitif di free tier.
- Model preview/experimental punya rate limit lebih ketat — pakai model **stable** (`gemini-3.6-flash`, bukan preview) untuk produksi RPP.

## Sumber

- https://ai.google.dev/gemini-api/docs/pricing (harga per model; diakses 17/9/2026)
- https://ai.google.dev/gemini-api/docs/rate-limits (mekanisme RPM/TPM/RPD, usage tier, spend limit; last updated 2/9/2026)
- https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash (token limit 1M input / 65K output)
- https://ai-api-hub.com/providers/google/rate-limits/ (verifikasi batch token per tier, 14/9/2026)
- https://ai-api-hub.com/providers/google/free-tier/ (eligibilitas free per model, 14/9/2026)
- LRN-20260917-001 (key Gemini pernah bocor → pola penyimpanan key aman)