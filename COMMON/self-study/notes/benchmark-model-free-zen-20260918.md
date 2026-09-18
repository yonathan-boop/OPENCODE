# Benchmark Model Free OpenCode Zen — 18 September 2026

**Tanggal tes:** 18 September 2026 (yonat-PC, model free di OpenCode Zen)
**Versi:** 1.0

## Ringkasan

Benchmark 6 model AI gratis (free tier) dengan 10 tes identik via `opencode run --auto`. Tujuannya: tahu model mana paling cocok untuk obrolan cepat, eksekusi task (executor), dan task yang butuh JSON ketat — tanpa biaya token.

## (a) Metode

- **6 model** yang diuji (semua free di OpenCode Zen): Big Pickle, Ling 3.0 Flash Fin, Muse 1.2, Muse 1.3, Nemotron 3 Ultra, Nemotron 3 Lightning.
- **10 tes identik** untuk tiap model, dijalankan via `opencode run --auto` (prompt sama persis antar model).
- **Validasi kode:** setiap output kode divalidasi lewat **exec** (jalan atau tidak), bukan cuma dilihat.
- **Timing:** diukur dengan **Stopwatch** per tes (waktu dari prompt sampai jawaban keluar).

## (b) Skor & Waktu (total 10 tes)

| Model | Skor | Rata-rata waktu |
|---|---|---|
| Big Pickle | 9.5 | 4.7 detik |
| Ling 3.0 Flash Fin | 9.5 | 4.4 detik |
| Muse 1.2 | 9.5 | 5.9 detik |
| Muse 1.3 | 9.0 | 9.2 detik |
| Nemotron 3 Ultra | 10.0 | 14.0 detik |
| Nemotron 3 Lightning | 10.0 | 14.2 detik |

Skor 10 = sempurna. Tidak ada model yang gagal total; perbedaan ada di presisi detail (terutama JSON) dan kecepatan.

## (c) Fitur Pembeda

- **JSON presisi valid:** hanya **Nemotron (keduanya)** yang menghasilkan JSON valid tanpa error validasi — jadi unggulan untuk output terstruktur ketat. Harga: paling lambat (±14 detik/tes).
- **Over-eksekusi Muse 1.3:** sekali menjalankan aksi tak diminta (**jalan `git pull`** saat tes "halo" yang seharusnya cuma chat). Ini **ancaman di agent mode** — bisa melakukan operasi yang tidak diperintahkan. Skor diturunkan ke 9.0 + waktu naik (kemungkinan eksekusi ekstra ikut dihitung).
- Big Pickle, Ling, Muse 1.2 = setara skor 9.5, beda di kecepatan: **Ling tercepat** (4.4 dtk) lalu Big Pickle (4.7 dtk).

## (d) Rekomendasi

| Kebutuhan | Model |
|---|---|
| Live / obrolan cepat (latensi penting) | **Ling 3.0 Flash Fin** (tercepat, skor sama dengan Big Pickle) |
| Otak executor (kerja/eksekusi task umum) | **Big Pickle** (stabil, cepat, skor tinggi) |
| JSON ketat / task berat butuh presisi terstruktur | **Nemotron 3 Ultra** (JSON selalu valid; terima latensi ±14 dtk) |
| Vision saja (baca gambar, bukan agent) | **Muse 1.3** — pakai dengan **waspada**: over-action (eksekusi tak diminta) + latensi lebih tinggi |

Catatan: untuk agent mode (bisa jalanin command sendiri), hindari Muse 1.3 karena riwayat over-eksekusi. Kalau toleran latensi dan butuh output struktur rapi → Nemotron 3 Ultra, bukan yang paling cepat.

## Sumber

- Hasil benchmark langsung (6 model × 10 tes, 18/9/2026, OpenCode Zen free tier)