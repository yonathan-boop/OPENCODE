# Backup 3-2-1 untuk Data Sekolah: Strategi Murah, Efektif, dan Cara Tes Restore

## Ringkasan

Strategi **3-2-1** adalah standar backup data yang direkomendasikan oleh CISA (badan siber AS), NCSC (badan siber UK), dan NIST CSF. Intinya: simpan **3 salinan** data, di **2 jenis media** berbeda, dengan **1 salinan offsite** (terpisah secara geografis). Dikembangkan oleh fotografer Peter Krogh (2005) dan tetap relevan di 2026 — bahkan versi modern 3-2-1-1-0 menambah 1 backup immutable (tidak bisa diubah/dihapus) dan 0 error saat tes restore.

Untuk sekolah kecil, strategi ini sangat layak — biaya bisa mulai dari Rp 0 (Google Drive gratis) sampai ~Rp 1-2 juta/tahun (cloud + HDD eksternal).

## Poin Praktis untuk Admin Sekolah

### Apa yang Wajib Di-backup
- Data siswa & guru (rapor, absensi, Nilai, data demografi)
- File dokumen (RPP, silabus, soal ujian, surat menyurat)
- Data keuangan (gaji, pembayaran SPP)
- Website sekolah
- Email & dokumen kolaborasi (OneDrive/Google Drive/SharePoint)
- Sistem informasi manajemen (Dapodik, E-Rapor, dst)

### Implementasi 3-2-1 Murah untuk Sekolah

| Salinan | Media | Contoh Gratis/Murah | Biaya |
|---------|-------|---------------------|-------|
| 1 (Original) | Komputer/server lokal | File di laptop/guru | Rp 0 |
| 2 (Backup lokal) | HDD eksternal / NAS | HDD 2TB (Rp 500-800rb) + robocopy terjadwal | Rp 0-800rb (sekali) |
| 3 (Backup offsite) | Cloud | Google Drive (15GB gratis), OneDrive (5GB), atau IDrive (5TB, ~Rp 750rb/tahun) | Rp 0-750rb/tahun |

**Tier untuk sekolah sangat kecil (budget nol):**
1. File guru → simpan langsung di Google Drive/OneDrive (otomatis cloud)
2. HDD bekas → backup folder penting via robocopy/Windows File History
3. Cloud backup dokumen kritis → Google Drive / OneDrive (sudah 3-2-1 kalau file asli di lokal)

**Tier untuk sekolah menengah:**
1. Server lokal → NAS (Synology DS220+ ~Rp 4 juta + HDD) atau HDD besar
2. Robocopy/rsync terjadwal ke NAS → backup harian
3. Cloud (Google Workspace for Education biasanya sudah termasuk unlimited Drive untuk sekolah)

### Jadwal Backup yang Direkomendasikan

| Data | Frekuensi | Metode |
|------|-----------|--------|
| Data absensi/rapor | Harian | Robocopy terjadwal (Task Scheduler) |
| File dokumen guru | Harian (incremental) | File History / rsync |
| Full server backup | Mingguan | robocopy /E /XO |
| Offsite (cloud) | Harian atau mingguan | rclone (gratis) ke Google Drive |

### Tools Gratis/Murah

| Tool | Fungsi | Platform |
|------|--------|----------|
| **robocopy** (bawaan Windows) | Backup lokal increment, multithread | Windows |
| **rsync** (Linux) | Backup incremental, kompresi | Linux |
| **rclone** | Sync ke cloud (Google Drive, S3, dll) | Cross-platform |
| **Windows File History** | Backup otomatis folder user | Windows 10/11 |
| **Google Drive for Desktop** | Sync folder ke cloud | Windows/Mac |
| **IDrive** | Cloud backup unlimited device | Cross-platform (~$80/thn 5TB) |
| **Backblaze** | Cloud backup unlimited | Windows/Mac (~$99/thn) |

### Strategi Air-Gapped (Penting untuk Ransomware)

DfE Cyber Security Hub (2026) menekankan: **1 salinan harus offline/air-gapped** — artinya tidak terkoneksi jaringan secara permanen. Untuk sekolah:
- Simpan 1 HDD eksternal yang **dicabut** setelah backup, simpan di lemari/brankas
- Atau gunakan cloud dengan fitur **WORM (Write Once Read Many)** / object lock
- Update air-gapped backup minimal **1x per bulan**

## Jebakan/Error Umum

1. **Cloud sync ≠ backup** — Google Drive/OneDrive sync artinya kalau file terhapus/terenkripsi ransomware di lokal, ikut hilang di cloud. **Solusi:** pakai backup terpisah dari sync, atau aktifkan version history.

2. **Tidak pernah tes restore** — 48% tes restore perusahaan gagal (Symantec Study). Backup yang tidak pernah dites = ilusi keamanan. **Solusi:** tes restore minimal 1x per bulan.

3. **Backup hanya 1 salinan** — Banyak sekolah hanya backup ke 1 HDD tanpa offsite. Kalau HDD rusak atau kantor kebakaran, lenyap. **Solusi:** tambah cloud (gratis) atau HDD kedua di lokasi berbeda.

4. **Backup otomatis tapi tidak dimonitor** — Jadwal backup jalan tapi gagal diam-diam (disk penuh, koneksi putus, permission error). **Solusi:** cek log backup mingguan, set alert email.

5. **Semua credential backup sama** — Kalau akun admin dikompromi, backup ikut terenkripsi ransomware. **Solusi:** pakai credential terpisah untuk backup, aktifkan MFA.

6. **Backup tidak terjadwal / manual** — Sering terlupa. **Solusi:** automasi dengan robocopy terjadwal (Task Scheduler) atau rclone cron.

7. **Tidak membedakan data kritis vs non-kritis** — Backup semua = lambat & mahal. **Solusi:** identifikasi data prioritas (absensi, rapor, keuangan) vs data umum (dokumen guru yang sudah di Drive).

8. **Ransomware menghapus backup juga** — Ancaman 2026: penyerang sengaja menghapus backup sebelum enkripsi. **Solusi:** air-gapped backup (HDD offline) + immutable cloud backup.

## Sumber

1. **DfE Cyber Security Hub (UK)** — "Implementing the 3-2-1 backup strategy" (July 2026) — https://cyber-security-hub.education.gov.uk/321-backup
2. **Ministry of Education NZ** — "Backing up important school data" (Oct 2025) — https://www.education.govt.nz/education-professionals/schools-year-0-13/digital-technology/backing-important-school-data
3. **AvePoint** — "What Is the 3-2-1 Backup Rule? A Complete 2026 Guide" (Apr 2026) — https://www.avepoint.com/blog/backup/3-2-1-backup-rule
4. **TechTarget** — "Use the 3-2-1-1-0 rule for better backups" (Jan 2026) — https://www.techtarget.com/searchdatabackup/tip/How-the-3-2-1-1-0-backup-rule-reflects-modern-needs
5. **SentinelOne** — "What Is the 3-2-1 Backup Strategy?" (May 2026) — https://www.sentinelone.com/cybersecurity-101/cybersecurity/3-2-1-backup-strategy
6. **IT Brew** — "Is the 3-2-1 backup rule still the gold standard?" (Jan 2026) — https://www.itbrew.com/stories/2026/01/27/is-the-3-2-1-backup-rule-still-the-golden-standard
7. **Vision Computers** — "The 3-2-1 Backup Rule — How to Protect Your Data in 2026" (Mar 2026) — https://www.visioncomputers.com/page?page=backup-strategy-3-2-1-rule
8. **CrashPlan** — "What is the 3-2-1 Backup Rule?" (Mar 2026) — https://www.crashplan.com/resources/guide/3-2-1-backup-strategy-guide
9. **Orleans Parish School Board** — "Business Continuity and Technology Disaster Recovery" (policy reference) — https://nolapublicschools.com/CAPS/Policies/EFD_-_Business_Continuity_and_Technology_Disaster_Recovery_(Amended_12_17_20).htm
