# Batch Proses Puluhan Mapel Ujian per UTS: Penamaan Konsisten "... OK Edit P", Tracking Selesai/Backlog, Cek List Putus di Tengah Jalan

- Tanggal: 2026-09-20 (klaim SERVER, self-study)
- Terkait tool internal: `COMMON/scripts/ujian_builder.py`, `kop-methodist.docx`, konvensi status LRN-20260918-010

## Ringkasan

Saat UTS/ujian datang, folder backup guru berisi puluhan dokumen mentah per mapel+kelas. Prosesnya: edit semua → validasi → cetak. Tanpa sistem, gampang terlewat atau proses dua kali. Pola yang benar (dirangkum dari riset batch processing + version control):

1. **Nama file = status berjalan** — sufiks status di nama file (`base ... OK`, `base ... Edit P`) membuat *durable state*: selesai/tidaknya bisa dibaca ulang dari folder kapan saja, tanpa ingat-ingat atau log terpisah. Ini prinsip "derive work from durable facts" — status di filename adalah kebenaran yang bertahan lewat restart.
2. **Tracking = daftar mapel dengan status** — daftar (markdown `- [ ]` / tabel status) yang memetakan tiap mapel → status (backlog / in progress / done / gagal). Backlog dibangun dari scan folder **@backup guru** (apa yang belum punya sufiks selesai = masih pending).
3. **Batch harus bisa di-resume** — kalau proses putus di tengah (crash, timeout, list putus), jangan mulai ulang dari nol. Baca ulang daftar status → lompat ke yang belum selesai. Idempoten: memproses ulang file yang sudah selesai tidak boleh merusak output.

## Poin praktis untuk admin sekolah

- **Definisikan 1 konvensi & tuliskan.** Contoh yang terpakai di sini (LRN-20260918-010): `"OK"` = sudah diperiksa, `"Edit"` = sudah diedit, `"P"` = siap cetak. Nama file yang baru diedit cukup `base + " Edit"` (jangan langsung "OK Edit P" — status ditambah bertahap sesuai tahap yang benar-benar tercapai).
- **Gunakan nama file sebagai "database status".** Loop script batch tinggal: (1) `glob` semua file mapel di folder backup, (2) skip yang namanya sudah mengandung `OK`/`Edit P`, (3) proses sisanya, (4) rename/ambil nama output sesuai konvensi. Tidak perlu DB — scan ulang folder sudah memberi daftar backlog yang akurat.
- **Backlog dari @backup guru**: jangan hardcode daftar mapel. **Scan folder** → daftar yang muncul tanpa status selesai = backlog. Ini otomatis menangkap mapel baru yang ditambah guru.
- **Cek list putus di tengah jalan**: simpan kemajuan per file (bukan satu loncatan besar). Kalau batch gagal di mapel ke-23 dari 40, laporan yang berguna = "1–22 selesai, 23 gagal (kenapa), 24–40 pending", bukan "gagal".
- **Pisahkan error dari alur**: file gagal dicatat (nama + error + percobaan) tapi batch tetap lanjut ke file berikutnya. File gagal diproses ulang terpisah, bukan mengulang semua.
- **Idempotensi output**: kalau output = file baru (base + " Edit"), memproses dua kali menghasilkan file sama, tidak korup. Kalau output menimpa, pastikan operasinya se-aman mungkin untuk diulang (mis. validasi isi dulu sebelum skip).
- **Nama konsisten supaya bisa di-sort/grep**: pisahkan kata dengan spasi/tanda jelas, jangan nama generik (`new document (2)`), hindari karakter yang rusak di shell/Windows (`< > : " / \ | ? *`).
- Pola khusus lingkungan ini: ujian_builder.py punya `--out` default = folder sumber + basename + " Edit.docx" — sudah sesuai konvensi. Untuk batch puluhan mapel tinggal lakukan per-file: build → validasi (render/visual wajib, LRN-20260725-001) → update status di nama/daftar.

## Jebakan/error umum

- **Status dobel/ambigu di nama**: `final_finalOK_absolutely-last` — jangan menumpuk kata status bebas. Tetap pada flag yang sudah disepakati (`OK`, `Edit`, `P`) dan tambah hanya jika tahap benar-benar tercapai.
- **"Sudah selesai" salah kaprah**: kata "final"/"OK" di nama sering tidak real — verifikasi isi dulu (gambar, nomor soal, kop) sebelum tandai selesai. Status di nama jangan menggantikan validasi.
- **Edit dokumen sumber sekolah langsung (in-place)**: berbahaya — kalau salah, tidak ada versi lama untuk dibandingkan/rollback. Simpan versi lama (arsip), kerja di salinan. (Pola sama dengan aturan sistem versi absensi.)
- **Batch stop di error pertama**: satu file rusak (korup, ekstensi salah, gambar rusak) menghentikan semua mapel lain. Kecualikan satu per satu sehingga yang lain tetap jalan.
- **Backlog basi**: daftar pending yang tak pernah di-review menumpuk dan menyesatkan laporan — rutin bersihkan (mapel yang tak jadi/proses lama).
- **Checkpoint yang salah urutan**: jangan tandai "selesai" SEBELUM file berhasil disimpan. Urutan benar untuk batch: tulis output sukses → baru tandai selesai. (Pola "write-then-acknowledge").
- **Proses ulang tanpa cek idempotensi**: kalau script tidak idempoten, menjalankan ulang batch bisa menggandakan output / menimpa hasil valid. Pastikan reproses aman.
- **Nama file mengandung karakter ilegal** saat rename otomatis (spasi berlebih, karakter khusus Windows) → gagal di tengah batch. Sanitasi sebelum proses.

## Sumber

- Google Cloud Run Jobs — retries & checkpoints (idempotensi, checkpoint, write ke tempat berbeda): https://docs.cloud.google.com/run/docs/jobs-retries
- Tian Pan, "The Batch LLM Pipeline Blind Spot: Queue Design, Checkpointing, Cost Attribution" (Apr 2026) — granularitas batch, checkpoint, dead letter queue, apa arti "done": https://tianpan.co/blog/2026-04-10-batch-llm-pipeline-blind-spot
- knowledgelib.io, "Batch Processing Patterns" (2026): chunk + checkpoint + idempotent upsert + DLQ; jangan muat semua ke memori: https://knowledgelib.io/software/patterns/batch-processing/2026
- Wicked Smart Data, "Checkpointing and State Management in Long-Running Data Pipelines" (2026) — tulis-dulu-baru-checkpoint, jangan sebelum: https://www.wickedsmartdata.com/articles/checkpointing-and-state-management-in-long-running-data-pipelines
- Interwebicly, "Why Restartability Is a Feature, Not a Hack" (2026) — state eksternal yang tahan restart, stable identity: https://interwebicly.com/blog/why-restartability-is-a-feature-not-a-hack
- FilesDesk, "File Naming Conventions 2026" (2026) — pola nama, karakter ilegal, versi tanggal: https://filesdesk.app/blog/file-naming-conventions
- Torihiki Techō (ISVDP, 2026) & OSU Libraries & GSE — "jangan pakai kata FINAL", status flag dari daftar tetap, versi v01/v02, arsip jangan hapus: https://torihiki.isvd.or.jp/en/direction/file-management-basics · https://library.osu.edu/sites/default/files/2021-12/guide-document-version-control-2021-v0.2.pdf · https://gse.kz/en/blog/template-versioning-storage-approval-rollback
- CoonTool & Zush (2026) — rename massal dokumen guru, konvensi `{Subjek}_{Kelas}_{Tipe}`, preview sebelum terapkan: https://www.coontool.com/blog/how-to-rename-pdf-files-bulk-guide-for-teachers · https://zushapp.com/blog/rename-scanned-documents-automatically
- python-docx (batch update docx) & docx-editor (batch_edit atomik, dry_run): https://python-docx.readthedocs.io/en/latest/ · https://github.com/pablospe/docx-editor
- Task tracking berbasis markdown (status `[ ]`/`[/]`/`[x]`, backlog bersih): Task Genius docs & tasks-ng spec — https://taskgenius.md/docs/task-status · https://github.com/0xsalt/tasks-ng

## Refleksi internal (terhubung ke memory)

- Konvensi "OK Edit P" di sini = CATATAN STATUS kerja sekolah (LRN-20260918-010). Batch tool yang sudah ada (`ujian_builder.py`) siap dipakai sebagai loop per mapel dengan pola scan → skip selesai → proses → validasi → tandai.
- Batas yang disadari: ujian dengan banyak equation/gambar tetap butuh Word COM, bukan batch penuh (LRN-20260918-005) — batch boleh di-loop tapi validasi visual tiap output tetap wajib sebelum "OK".