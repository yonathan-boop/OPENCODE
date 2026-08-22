#!/usr/bin/env bash
# ============================================
# MENU TERMINAL ONLINE - server methodist-11
# Dipanggil oleh: ttyd ... bash pilih-terminal.sh
# Sesi tmux bertahan selamanya walau koneksi
# terputus / tab browser ditutup.
# Keluar dari sesi: Ctrl+B lalu D (detach).
# ============================================

mapfile -t daftar < <(tmux list-sessions -F '#S' 2>/dev/null | grep -v '^main$')

clear
echo "=========================================="
echo "   PILIH SESI TERMINAL  (server m11)"
echo "=========================================="
if [ ${#daftar[@]} -eq 0 ]; then
  echo "  (belum ada sesi tersimpan)"
else
  i=1
  for s in "${daftar[@]}"; do
    echo "  $i) $s"
    i=$((i+1))
  done
fi
echo "  0) + buat sesi baru"
echo "------------------------------------------"
read -p "Pilih nomor lalu Enter: " p

if [[ "$p" == "0" ]]; then
  read -p "Nama sesi baru: " n
  exec tmux new -A -s "${n:-baru}"
elif [[ "$p" =~ ^[0-9]+$ ]] && [ "$p" -ge 1 ] && [ "$p" -le "${#daftar[@]}" ]; then
  exec tmux attach -t "${daftar[$((p-1))]}"
else
  echo "Pilihan tidak valid. Refresh halaman untuk mencoba lagi."
  sleep 3
fi
