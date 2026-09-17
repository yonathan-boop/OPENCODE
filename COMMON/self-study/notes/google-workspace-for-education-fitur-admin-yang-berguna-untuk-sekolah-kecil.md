# Google Workspace for Education: Fitur Admin yang Berguna untuk Sekolah Kecil

Status: selesai 2026-09-17 (server) · tags: #google-workspace #admin #sekolah #gmail #classroom

## Ringkasan

Google Workspace for Education = paket tool sekolah di satu domain (contoh `sekolah.sch.id`):
Gmail, Calendar, Meet, Classroom, Docs, Sheets, Slides, Forms, Drive, Groups, Sites, Tasks,
+ Gemini app & NotebookLM. Semua dikelola di **Admin console** (`admin.google.com`) —
pusat kendali akun, perangkat, kebijakan, dan keamanan. Edisi **Education Fundamentals
GRATIS** untuk sekolah yang memenuhi syarat (mencakup hampir semua fitur inti + 100 TB
storage pooled per institusi). Edisi berbayar (**Standard**, **Plus**, add-on **Teaching &
Learning**) hanya menambah keamanan/analitik lanjutan dan AI premium — untuk sekolah kecil
biasanya Fundamentals sudah cukup.

## Poin praktis untuk admin sekolah

1. **Edisi (per edu.google.com):**
   - **Fundamentals (gratis)** — Gmail, Meet (hingga 1000 peserta), Classroom, Assignments,
     Docs/Sheets/Slides/Forms, Drive, Sites, Groups, Tasks, Gemini app + NotebookLM,
     admin console, **100 TB storage terpool per organisasi**.
   - **Standard / Plus (bayar)** — Plus tambah security dashboard terpadu, analytics
     lanjutan, Gemini dalam Docs/Slides/Forms/Vids (pengguna 18+), dsb. Diskon 25% utk
     Plus pada pembelian 50–999 lisensi (kontrak 1 tahun).

2. **Struktur Admin console — 15 bagian top-level:** Users, Billing, Domains, Alerts,
   Groups, Devices, Organizational units, Reporting, Apps, Account settings, Support,
   Security, Buildings and resources, Rules, Storage. Bagian bisa di-*pin* biar menu
   harian di atas.

3. **Bikin akun massal:** manual per user (Admin console) atau **upload CSV** (sekali
   langsung banyak user). Untuk sekolah kecil tanpa server LDAP → CSV cukup. Daftarkan
   email **Admin/help desk** sebagai kontak recovery password user.

4. **Organizational units (OU) + Groups:** kelompokkan user (mis. `Guru`, `Siswa`,
   `Tata Usaha`) → terapkan pengaturan per OU (fitur boleh akses, kebijakan Gemini,
   dsb). Groups = milis sekolah (info, guru-siswa, komite).

5. **Classroom:** aktifkan via `Apps > Google Workspace > Classroom`. Guru harus
   **diverifikasi admin** dari grup `Classroom Teachers`. Atur izin guru (bikin/mengelola
   kelas). Aktifkan **guardian email summary** — orang tua dapat ringkasan nilai,
   deadline, tugas terlewat (opsional tiap sekolah).

6. **Keamanan e-mail wajib:** pasang **SPF, DKIM, DMARC** di DNS domain (mencegah spoof &
   email masuk spam). Enforce **2-Step Verification** utk semua admin (minimal).

7. **Peran admin (pre-built):** Super Admin, Groups Admin, User Management Admin,
   **Help Desk Admin** (reset password non-admin — cocok utk TU), Services Admin, Mobile
   Admin, Storage Admin, dsb. Ada juga peran kustom. **Best practice:** Super Admin ≥2
   account (pengaman kalau 1 terkunci), jangan dipakai utk kerja harian.

8. **Kontrol layanan tambahan:** matikan layanan Google di luar kepentingan sekolah
   (YouTube, Blogger, dll) per OU → lebih aman & hemat. Manajemen Chromebook via Device
   Hub + kebijakan 1000+ policy + *Device Restriction Schedule* (batasi jam pakai di
   rumah). Monitor via **Reporting** (audit log aktivitas user/admin).

9. **Migrasi:** impor email sistem lama pakai tool migrasi resmi. Tambahkan domain alias
   bila punya lebih dari satu nama domain.

10. **Sumber info update:** Google Workspace Updates blog
    (`workspaceupdates.googleblog.com`, label "Google Workspace for Education") — fitur
    baru rilis bertahap (Rapid/Scheduled release, bisa cek Release Calendar).

## Jebakan/error umum

- **SPF/DKIM/DMARC tidak dipasang** → email yang dikirim sekolah masuk spam/quarantine
  penerima. Ini langkah paling sering dilewati admin baru.
- **Super Admin dipakai utk kerja harian** → risiko terkunci / salah konfigurasi total.
  Gunakan role terbatas (Help Desk/User Management) utk operasional.
- **Semua pakai 1 Super Admin** → kalau 2SV hilang, akses domain ikut hilang
  (lockout safeguard = minimal 2 super admin).
- **Fitur Gemini di kelas hanya untuk 18+** — murid di bawah 18 TIDAK dapat Gemini in
  Docs/Slides/Forms walau sekolah pakai Education Plus. Sesuaikan ekspektasi.
- **Beberapa halaman resmi google berubah (404)** — mis. `workspace.google.com/industries/education`
  & `edu.google.com/workspace-for-education/features` sempat 404 saat riset (17/9). Cek
  via `edu.google.com/.../editions/overview` atau Google Workspace Updates blog.
- **Banyak layanan nyala default** — kontrol via `APPS > Additional services` per OU;
  cek rutin integrasi pihak ketiga (OAuth) yang terhubung akun sekolah.
- **Rilis fitur bertahap** — fitur "sudah dirilis" belum tentu tampil di domain sampai
  ±15 hari (Rapid) / dijadwalkan (Scheduled). Jangan panik cek berkala, bukan per hari.

## Sumber

- Google for Education — editions overview: edu.google.com/intl/.../workspace-for-education/editions/overview
- Google Workspace Help — Admin console docs: support.google.com/a/topic/9202 ; quickstart setup guide
- Google Classroom User Guide for Administrators (PDF resmi Google)
- Google Blog — "Google Workspace for Education's new safety features for IT admins" (Jan 2025)
- Google Workspace Updates — label Education & Weekly Recap (Feb/Sep 2026: Gemini di edu,
  kontrol granular NotebookLM dll)
- Dragapp — "The Admin Console Guide for 2026" (map 15 bagian console + tabel peran admin)