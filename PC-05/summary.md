# Memory Summary - PC-05 (PC Guru)

Terakhir diupdate: 2026-08-13

## User Info
- **Nama**: PC-05
- **Panggilan AI**: PC Guru
- **Bahasa**: Indonesia
- **OS**: Windows
- **Folder memory**: C:\Users\PC-05\Desktop\memory

## Setup PC-05 (10 Agustus 2026)
1. Git v2.55.0.3 diinstall via winget
2. Memory repo di-clone ke C:\Users\PC-05\Desktop\memory
3. Token GitHub disimpan di Windows Credential Manager (auto pull & push)
4. Folder PC-05 dibuat di repo memory (IDENTITY, facts, summary)
5. Nama AI di PC ini ditetapkan: **PC Guru**
6. Config global opencode di-update agar auto-load memory

## Project Aktif
1. **Memory System** - Sistem memory lintas PC (aktif)

## Session Terakhir
Tanggal: 2026-08-13
Topik: PC lelet — matikan semua proses selain Chrome & Word; RAM bebas naik 0.8 → 1.78 GB
Status: Selesai

## Debloat PC-05 (10 Agustus 2026)
- Diuninstall: McAfee Security Scan Plus, 19 app Store (Xbox, Solitaire, Clipchamp, Bing, Skype, dll), SHAREit, AIdea, Winamp, KMPlayer, Audiograbber, Any Video Converter, Total Video Converter, Sony Xperia Flash Tool, Sony Mobile Update Drivers, Gordon's Gate, Universal ADB, MINA Overwatch blocker, VLC, Audacity, OneDrive, Epson Software Updater, Epson Manuals, Dynamic App Loader, Intel Trusted Connect, MyEpson Portal (entry yatim), PaperCut Mobility Print (residual)
- Startup dimatikan: OneDrive, Epson monitor (EPLTarget x2, EPPCCMON), Adobe Acrobat Synchronizer, Chrome/Edge autolaunch, McAfee
- Service dimatikan (Disabled): chromoting (Chrome Remote Desktop), isaHelperSvc (Intel Security Assist), MyEpson Portal Service, GoogleUpdater*
- Service manual: VeyonService (bisa dibuka manual)
- Auto-cleanup tiap login: scheduled task "PC-Guru-Cleanup" → jalankan PC-05/scripts/pc-guru-cleanup.ps1
- Edge: jarang dipakai → auto-mati tiap login (proses msedge di-kill di pc-guru-cleanup.ps1), tetap bisa dibuka manual
- RAM bebas naik ~2.0 → 2.9 GB (dari 7.8 GB)

## Cleanup Tambahan (13 Agustus 2026) — hanya Chrome & Word
- Masalah: PC lelet, user mau pakai Chrome + Word saja, yang lain dimatikan
- Ditambahkan ke pc-guru-cleanup.ps1 (permanen, jalan tiap login elevated):
  - Kill proses: msedgewebview2, SearchHost, SnippingTool, TiWorker, WidgetService
  - Service Disabled: **wuauserv** (Windows Update — update memang dikunci user, wuauserv masih jalan & bikin TiWorker 775 MB), **WSearch** (Windows Search — biang webview2/SearchHost yang bangkit lagi)
  - Widgets dimatikan permanen via policy `HKLM\SOFTWARE\Policies\Microsoft\Dsh` → AllowNewsAndInterests=0
- Hasil: RAM bebas 0.8 → 1.78 GB, TiWorker/Widgets/SnippingTool mati permanen, Chrome & Word tetap jalan
- Catatan: msedgewebview2/SearchHost bisa muncul lagi saat Start menu / search box dibuka — wajar, cuma seumur dipakai
