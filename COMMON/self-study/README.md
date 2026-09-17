# SELF-STUDY — Sistem Belajar Mandiri AI

Sistem agar asisten terus mengembangkan diri secara otomatis, tanpa diminta.
Ide inti dari user (17/9/2026): "kamu jelajah sendiri, berkembang, supaya bisa
membantu lebih banyak hal nantinya" — token murah, manfaatkan.

## Cara Kerja
1. **Queue topik** di `topics.md` — daftar hal yang berguna untuk pekerjaan user
   (admin sekolah). Tambah/kurang bebas, diproses urut dari atas.
2. **Runner** `SERVER-LINUX/scripts/self-study.sh` dijalankan cron (tiap **Senin 03:00**).
   - Ambil topik pertama yang belum `[x]`
   - Spawn `opencode run --auto`: riset via web → tulis catatan ke `notes/` → tandai topik `[x]` → commit+push
   - Log: `/var/log/self-study.log`, detail: `/root/SERVER-LINUX/logs/self-study-*.md`
3. **Hasil** = catatan ringkas (Ringkasan / Poin praktis / Jebakan / Sumber) di `notes/`.

## Manual Run (kapan saja)
```bash
bash /root/SERVER-LINUX/scripts/self-study.sh
```
File di `notes/` ikut ke-sync lewat repo memory ke semua PC.

## Aturan
- Topik harus praktis & relevan kerja user (bukan hiburan/teori murni).
- Catatan ditulis Bahasa Indonesia, ringkas, fokus "biar bisa langsung dibantu".
- Jangan sentuh service/kredensial/data user dalam proses riset.