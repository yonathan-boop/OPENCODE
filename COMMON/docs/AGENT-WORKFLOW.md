# Agent Workflow

Workflow tetap setiap sesi: **LOAD → PLAN → EXECUTE → VERIFY → SAVE → STOP**

---

## Phase 1: LOAD (Awal Sesi)
1. Git pull memory (`cd memory && git pull`)
2. Baca SOUL.md, USER.md, MASTER-MEMORY.md (jika ada)
3. Baca summary & facts per PC (`PC-XX/summary.md`, `PC-XX/facts.md`)
4. Baca MEMORY-LEARNINGS.md & MEMORY-ERRORS.md
5. Cek aktivitas terbaru (file di `PC-XX/docs/` yang paling baru)
6. Set konteks sesi

## Phase 2: PLAN (Sebelum Eksekusi)
1. Parse user intent — apa yang sebenarnya diminta?
2. Cek memory relevan — apa yang sudah diketahui tentang task ini?
3. Breakdown task ke langkah-langkah
4. Pilih tool strategy — sub-agent atau langsung?
5. Presentasi plan ke user jika perlu klarifikasi

## Phase 3: EXECUTE
1. Gunakan tool yang sesuai (lihat TOOL-STRATEGY.md)
2. Prioritaskan sub-agent untuk operasi berat/batch
3. Eksekusi langkah demi langkah
4. Setiap langkah harus jelas outputnya

## Phase 4: VERIFY
1. Cek output — apakah sukses?
2. Jika error: catat error, diagnosa, tanya user jika perlu
3. Konfirmasi hasil ke user
4. Jangan lanjut sebelum verified

## Phase 5: SAVE
1. Catat aktivitas sesi ke `PC-XX/docs/SESSION-YYYY-MM-DD.md`
2. Update `PC-XX/summary.md` (session terakhir, total sesi)
3. Catat pembelajaran baru ke `COMMON/docs/MEMORY-LEARNINGS.md`
4. Catat error baru ke `COMMON/docs/MEMORY-ERRORS.md`

## Phase 6: STOP
1. Tawarkan `/savememory` untuk commit ke GitHub
2. Tanya user: ada lagi atau selesai?
3. Stop reasoning — jangan lanjut ngomong kalau udah selesai
