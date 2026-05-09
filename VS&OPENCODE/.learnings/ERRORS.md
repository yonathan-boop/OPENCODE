# Errors

Command failures and integration errors.

---

## [ERR-20260509-001] vs_code_instance_scope

**Logged**: 2026-05-09
**Priority**: high
**Status**: resolved
**Area**: config

### Summary
VS Code instance awalnya dilarang edit file di luar VS&OPENCODE/, membatasi kemampuan bantu user.

### Error
Boundary terlalu ketat — tidak bisa edit file PC-06/, COMMON/, atau file proyek lain saat user minta.

### Context
- VS Code instance hanya boleh edit `Desktop\memory\VS&OPENCODE\`
- User ingin bisa menyuruh edit file di folder lain
- Solusi: read-only default + izin dulu kalau disuruh

### Suggested Fix
Telah diimplementasi: boundary diubah jadi read-only default, dengan izin user bisa edit.

### Metadata
- Reproducible: no
- Related Files: SOUL.md, AGENTS.md

---

