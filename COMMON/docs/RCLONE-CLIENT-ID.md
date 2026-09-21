# RCLONE GDRIVE — UBAH SHARED CLIENT_ID KE MILIK SENDIRI

#rclone #gdrive #backup #server-linux #auto-update #urgent

## MASALAH
rclone (remote `gdrive` di server Linux) pakai **shared client_id** bawaan rclone.
Google resmi mengumumkan shared client_id ini **di-retire & berhenti bekerja tahun 2026**
(lihat log `/var/log/gdrive-website-check.log`: *"This remote uses rclone's shared Google
Drive client_id, which is being retired and will stop working during 2026"*).

Kalau tidak diganti → **auto-update website dari Google Drive (cron tiap 15 mnt) dan backup
gdrive tar.gz (cron 21:30) MATI.** Ini prioritas sebelum itu terjadi.

## CEK STATUS
```bash
rclone config show gdrive            # lihat client_id saat ini
rclone lsd gdrive: 2>&1 | head -3    # tes koneksi
```

## SOLUSI — buat client_id sendiri (sekali saja, ~10 menit)

### Langkah 1 — Dapatkan Client ID/Secret (di browser, akun Google apa pun)
1. Buka https://console.developers.google.com → login.
2. Pilih/buat project (nama bebas, misal "rclone-server").
3. "ENABLE APIS AND SERVICES" → cari **Drive** → enable **Google Drive API**.
4. Klik **Credentials** (panel kiri).
5. Konfigurasi **OAuth consent screen**:
   - App name: `rclone` (bebas), User support email: email sendiri.
   - Audience: **External** → tambahkan diri sendiri sebagai **Test user** (wajib).
   - Tambah scope `https://www.googleapis.com/auth/drive` (supaya bisa read/write).
6. Overview → **Create Credentials → OAuth client ID** → Application type: **Desktop app** → Create.
7. Catat **Client ID** dan **Client Secret**.

### Langkah 2 — Pasang ke remote gdrive di server
```bash
rclone config
# pilih: e (edit existing) → gdrive
# client_id     → tempel Client ID di atas
# client_secret → tempel Client Secret
# opsi lain biarkan (scope drive, rooting, dst)
# Save
```

### Langkah 3 — Re-autorisasi token (client baru butuh token baru)
- **Opsi A — CARA RESMI (terbaru, paling gampang, TANPA copy-paste JSON):** setelah client_id/
  secret tersimpan di config, langsung di server (tanpa browser):
  ```bash
  rclone config reconnect gdrive:
  # saat ditanya "Already have a token - refresh?" → jawab "Y" (yes)
  ```
  rclone akan memunculkan link OAuth → buka di browser PC mana pun, login akun Google yang
  punya akses ke Drive tujuan → token baru dibuat otomatis untuk client_id milik sendiri.
- **Opsi B (fallback manual):** kalau `reconnect` bermasalah, jalankan dari PC yang ada browser:
  ```
  rclone authorize "drive" --drive-client-id=<CLIENT_ID> --drive-client-secret=<CLIENT_SECRET>
  ```
  → buka link, login akun Google, copy JSON token → di server `rclone config` → gdrive →
  `Auto config? n` → paste JSON token manual.

### Langkah 4 — Verifikasi
```bash
rclone lsd gdrive:                    # harus muncul folder "Server Linux Backup"
rclone about gdrive:                  # cek kuota
bash /root/SERVER-LINUX/scripts/gdrive-website-check.sh  # tes satu siklus, cek log
```
Setelah berhasil, log rclone TIDAK lagi memunculkan NOTICE shared client_id.

## CATATAN
- Client ID/Secret dan token masuk ke `~/.config/rclone/rclone.conf` — **JANGAN commit ke git**.
- Quota default 10 transaksi/detik per client_id — aman untuk lalu lintas sekolah.
- Remote serupa di PC lain (kalau ada) sesuaikan juga, atau biarkan saling bebas.
- Kalau flow ini berasa ribet di server, alternatif: remote `gdrive` dibuat ulang via
  `rclone config` yang jalan dari PC user lalu salin `rclone.conf` ke server (selalu ada
  opsi ini, urutan 2-3-4 tetap sama).