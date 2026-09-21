# Errors

Command failures and integration errors.

---

## [ERR-20260921-001] tunnel_unauthorized_tunnel_not_found

**Logged**: 2026-09-21
**Priority**: high
**Status**: resolved
**Area**: website-infra

### Summary
Server linux (linux-hp) yang sebelumnya host website SD Methodist-11 down. Dipindah ke tablet Termux, tapi Cloudflare tunnel menolak dengan `Unauthorized: Tunnel not found`.

### Error
`cloudflared tunnel run --token <TOKEN>` → web server lokal OK (HTTP 200 di localhost:8090), tapi domain methodist-11.my.id → HTTP 530. Log tunnel:
`ERR Register tunnel error from server side error="Unauthorized: Tunnel not found"`

### Context
- Tunnel named "Linux HP" id `912a22fa-051a-4891-897a-f2ff20f2d5f2` tidak dikenali lagi Cloudflare.
- Penyebab paling mungkin: tunnel terhapus dari dashboard Zero Trust (saat bersih-bersih PC lama).
- Web server tetap bisa jalan sendiri di port 8090 — ini bukan masalah server, murni masalah tunnel.

### Suggested Fix
1. Recreate named tunnel di Zero Trust dashboard (Networks → Tunnels → Create tunnel → Cloudflared).
2. Ambil token baru (awalan `eyJhIjoi...`), update variabel TOKEN di `linux-tablet/scripts/start-website.sh`.
3. Pasang Public Hostname: `methodist-11.my.id` → `http://localhost:8090`.
4. DNS A record proxied tidak perlu diubah.
5. Restart: `bash linux-tablet/scripts/start-website.sh`.

### Metadata
- Reproducible: yes
- Related Files: linux-tablet/scripts/start-website.sh, linux-tablet/docs/WEBSITE-METHODIST11.md
- Tags: cloudflare, tunnel, methodist-11, website

---

## [ERR-20260921-002] tunnel_service_down_file

**Logged**: 2026-09-21
**Priority**: high
**Status**: resolved
**Area**: website-infra

### Summary
Domain methodist-11.my.id kembali HTTP 530 walaupun nginx/server 8090 jalan (200) dan runsv cloudflared hidup. Penyebab bukan token/tunnel, tapi service cloudflared dalam state `down`.

### Error
- `ps` menunjukkan `runsv cloudflared` + `svlogd` jalan, tapi proses `cloudflared tunnel run` tidak ada.
- Service dir `/data/data/com.termux/files/usr/var/service/cloudflared/` berisi file `down` → runit tidak menjalankan/men-restart service.
- Log svlogd tetap kosong.

### Context
- Token valid tersimpan di `$HOME/.cloudflared/token` (format `eyJhIjoi...`, 184 byte).
- Run script: `exec cloudflared tunnel run --token-file "$HOME/.cloudflared/token"`.

### Fix
1. `rm /data/data/com.termux/files/usr/var/service/cloudflared/down` (biar auto-restart saat boot).
2. `SVDIR=/data/data/com.termux/files/usr/var/service sv up cloudflared`
3. Verifikasi: `pgrep -af "cloudflared tunnel"` muncul, `curl https://methodist-11.my.id` → 200.

### Metadata
- Reproducible: yes
- Related Files: /data/data/com.termux/files/usr/var/service/cloudflared/run
- Tags: cloudflare, tunnel, runit, termux, methodist-11

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

