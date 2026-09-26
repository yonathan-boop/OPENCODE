# PERMANENT POLICY — Simple, Human, Logical Way + Window Close Rules

Status: PERMANEN (berlaku di semua PC, tidak boleh dilanggar)
Tanggal Penetapan: 26 September 2026
Sumber: arahan langsung user

---

## RULE 1 — SELALU CARA PALING SEDERHANA & LOGIS (SEPERTI MANUSIA)

Default cara kerja AI untuk setiap task di PC:

1. **Pakai cara paling sederhana yang logis** — seperti yang dilakukan manusia biasa.
2. **Utamakan jalan pintas standar** yang sudah umum dikenal orang:
   - pintasan keyboard standar Windows / browser
   - klik pada tombol yang jelas
   - dialog bawaan aplikasi
3. **Jangan buat mekanisme rumit** (script bertingkat, koordinat pixel, wait/sleep panjang, bypass, langkah bertele-tele) kalau ada cara sederhana yang berhasil.
4. **Satu kebutuhan = satu aksi.** Kalau 3 langkah sederhana berhasil, berhenti di situ.
5. **Verifikasi sekali, lalu lapor.** Jangan cek berulang kalau hasilnya sudah jelas.

Contoh benar:
- butuh buka aplikasi -> pakai FlaUI / windows-mcp secara semantik, JANGAN Windows key
- butuh tutup jendela   -> **Alt+F4**
- butuh tutup 1 tab     -> **Ctrl+W**

---

## RULE 2 — WAJIB Alt+F4 untuk menutup jendela/aplikasi SECARA UTUH

**Alt+F4 = satu-satunya cara WAJIB untuk menutup jendela atau aplikasi secara utuh.**

Berlaku untuk:
- Jendela aplikasi native Windows (Notepad, Calculator, File Explorer, Word, Excel, dll)
- Jendela browser (menutup browser secara utuh)
- Dialog/popup yang sedang aktif
- Proses yang diaktifkan ke foreground lalu harus ditutup total

Aturan teknis:
- Sebelum Alt+F4: pastikan jendela target **sudah fokus** (RULE 1 — fokus dulu secara semantik, lalu tekan Alt+F4).
- Setelah Alt+F4: **verifikasi jendela benar-benar hilang** (`windows_list_windows`), baru lapor.
- Kalau muncul dialog "Save / Unsaved changes" -> tangani dialognya (pilih Save atau Don't Save sesuai konteks; jangan menggantung).
- **DILARANG** menutup jendela dengan:
  - Klik kanan taskbar -> Close window (kecuali tidak ada cara lain)
  - `Stop-Process` / `taskkill` untuk aplikasi yang sedang TERBUKA oleh user
  - Script yang menutup semua jendela sekaligus secara massal
  - Ctrl+W atau Ctrl+F4 untuk menutup seluruh aplikasi

---

## RULE 3 — Ctrl+W HANYA untuk menutup SATU TAB BROWSER

**Ctrl+W = HANYA untuk menutup satu tab browser.**

Berlaku untuk:
- Menutup satu tab di Chrome / Edge / Firefox
- Membersihkan tab yang tidak perlu dibuka lagi
- Membebaskan resource browser (tab berat / hang) tanpa menutup browser

Aturan teknis:
- Browser yang aktif = **WAJIB**. Jangan pakai Ctrl+W untuk aplikasi non-browser (Notepad, Word, Explorer).
- Kalau user minta "tutup tab" -> **1 tab saja**. Kalau tab yang tersisa penting atau baru dibuka, tutup tab yang paling tidak penting / duplikat.
- Kalau user minta "tutup browser" -> pakai **Alt+F4** (RULE 2), bukan Ctrl+W berulang.
- Kalau dialog "Save page?" muncul -> pilih **Don't Save** (kecuali user minta disimpan).

---

## HUBUNGAN DENGAN POLICY LAIN (tidak bertentangan)

| Policy | Isi | Relasi |
|---|---|---|
| `WINDOWS_SHELL_CONTROL_CORRECTION.md` | Larangan total semua kombinasi **Windows key** (Win, Win+D, Win+R, dll) via windows-mcp Shortcut / BatchKeys | **TETAP berlaku.** Alt+F4 & Ctrl+W BUKAN kombinasi Windows key -> tidak dilarang. |
| `TOOL_PRIORITY_POLICY.md` | Playwright -> FlaUI -> Windows-MCP (3 tier) | **TETAP berlaku** untuk fokus, klik, isi field. |
| `STRICT_UI_RECOVERY_POLICY.md` | Recovery UI yang ketat | **TETAP berlaku** kalau UI rusak. |
| `VISIBLE_WORK_PROGRESS_POLICY.md` | User melihat progres | **TETAP berlaku** — progres dikirim, bukan ditutup diam-diam. |

Inti combo yang benar:

1. **Fokus** jendela target secara semantik (Playwright untuk web, FlaUI untuk native) -> BUKAN Windows key, BUKAN koordinat pixel.
2. **Tutup** dengan keyboard standar manusia: **Alt+F4** untuk utuh, **Ctrl+W** untuk 1 tab.
3. **Verifikasi** hilang -> lapor ringkas.

---

## PELANGGARAN = ERROR

Kalau AI memakai cara yang lebih rumit dari simplest-human-way, atau salah menutup (Ctrl+W untuk aplikasi, Alt+F4 untuk 1 tab, taskkill untuk aplikasi milik user), itu **error operasional** -> catat ke `COMMON/docs/MEMORY-ERRORS.md`.
