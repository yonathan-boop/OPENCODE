# Backlog

## Done ✅
- [x] **Absensi workflow** — workflow step-by-step untuk absensi (WORKFLOW-ABSENSI.md)
- [x] **Agent Workflow** — pola LOAD→PLAN→EXECUTE→VERIFY→SAVE→STOP (AGENT-WORKFLOW.md)
- [x] **Tool Strategy** — tool reference + sub-agent triggers (TOOL-STRATEGY.md)
- [x] **Decision Framework** — 10 poin preferensi user (facts.md)
- [x] **Context Management** — strategi filter memory (CONTEXT-MANAGEMENT.md)
- [x] **Sub-agent optimization** — kapan spawn vs langsung (TOOL-STRATEGY.md)
- [x] **Stop conditions** — kapan berhenti reasoning (AGENT-WORKFLOW.md)
- [x] **Memory auto-save** — save setelah tiap task (AGENT-WORKFLOW.md)

## In Progress 🔄
- (none)

## Backlog 📋
- [ ] **Absensi otomatis lintas kelas** — fix Jocelyn-style name matching ✅ (17/9: absensi.py pakai token-matching (Levenshtein + SequenceMatcher), ambigu = skip aman, 24/24 case lulus)
- [x] **Absensi summary** — rekap bulanan otomatis dari file Excel (tool: `COMMON/scripts/rekap_absensi.py`, 6 Sept 2026)
- [ ] **Multi-PC memory sync** — pastikan memory di PC lain juga sync
- [ ] **Error auto-logging** — detect error patterns from bash output
- [x] **Session report** — template otomatis tiap akhir sesi (`COMMON/docs/SESSION-REPORT-TEMPLATE.md`, 6 Sept 2026)
- [ ] **rclone gdrive client_id** — shared client_id bakal di-retire 2026 → ikuti `COMMON/docs/RCLONE-CLIENT-ID.md` (butuh aksi user sekali, ~10 mnt) (17/9)
- [x] **Self-study system** — AI belajar mandiri mingguan (`COMMON/self-study/` + cron Senin 03:00) (17/9)

## Notes
- Tambahin item baru kalau muncul ide/request
- Update status kalau ada progress
- Hapus dari backlog kalau udah done
