# Feature Requests

Capabilities requested by the user.

---

## [FEAT-20260509-002] time_awareness_system

**Logged**: 2026-05-09
**Priority**: high
**Status**: implemented
**Area**: config

### Requested Capability
Sistem waktu yang jalan terus biar aku tahu berapa lama jeda antar sesi chat.

### User Context
Aku gak bisa deteksi waktu berlalu karena per-sesi. User bisa chat berhari-hari kemudian tapi aku pikir masih session sama.

### Complexity Estimate
simple

### Suggested Implementation
PowerShell script via Task Scheduler tiap 1 menit → log timestamp ke `.ticker/ticker.log`. Pas user chat, aku baca log itu buat tahu selisih waktu.

### Metadata
- Frequency: first_time
- Related Features: self_improving_agent

---

## [FEAT-20260509-001] self_improving_agent

**Logged**: 2026-05-09
**Priority**: high
**Status**: implemented
**Area**: config

### Requested Capability
Self-learning system — kemampuan untuk belajar dari pengalaman lintas sesi.

### User Context
User lihat openclaw punya self-improving agent skill dan ingin sistem yang sama di VS Code instance.

### Complexity Estimate
simple

### Suggested Implementation
Buat `.learnings/` directory dengan 3 file: LEARNINGS.md, ERRORS.md, FEATURE_REQUESTS.md. Migrasi data dari COMMON/docs. Integrasi workflow ke AGENTS.md.

### Metadata
- Frequency: first_time
- Related Features: memory_system

---

