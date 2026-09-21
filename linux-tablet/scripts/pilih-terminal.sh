#!/data/data/com.termux/files/usr/bin/bash

# pilih-terminal.sh — menu terminal online (methodist-11.my.id/opencode)
# Dipanggil oleh gotty. Pakai tmux: 1 terminal = 1 window.
# Tambah terminal lagi belakangan: dari dalam tmux ketik  Ctrl-b  lalu  c
#
# Kalau tab tertutup tidak sengaja, session tmux masih hidup.
# Buka lagi → ditawari LANJUT ke session lama, bukan buka dari awal.

TERM_TOTAL=2      # max terminal baru yang bisa dibuka
SESSION_PREFIX="web"

list_sessions() {
  tmux ls 2>/dev/null | grep -E "^$SESSION_PREFIX-" | awk -F: '{print $1}'
}

ask_continue() {
  read -r C
  case "$C" in
    '') exec "$0" ;;
    0|q) clear; echo "Sampai jumpa. Tutup halaman ini kalau selesai."; sleep 2; exit 0 ;;
    [0-9]*)
      [ "$C" -ge 1 ] 2>/dev/null || { echo "Pilihan gak valid. Ulangi."; sleep 1; exec "$0"; }
      SESSIONS=$(list_sessions)
      S=$(echo "$SESSIONS" | sed -n "${C}p")
      if [ -n "$S" ]; then
        clear
        echo "Lanjut ke session: $S"
        echo "(Isi terminal masih ada. Tutup tab = session tetap hidup.)"
        sleep 1
        exec tmux attach-session -t "$S"
      else
        echo "Nomor $C gak ada. Ulangi."; sleep 1; exec "$0"
      fi
      ;;
    *) echo "Pilihan gak valid. Ulangi."; sleep 1; exec "$0" ;;
  esac
}

clear
echo "=========================================="
echo "   TERMINAL ONLINE  SD METHODIST-11"
echo "=========================================="

SESSIONS=$(list_sessions)
COUNT=$(echo -n "$SESSIONS" | grep -c .)

if [ "$COUNT" -gt 0 ]; then
  echo ""
  echo "Ada $COUNT session lama yang masih hidup (tab ditutup tadi)."
  i=1
  echo "$SESSIONS" | while read -r s; do
    wins=$(tmux list-windows -t "$s" 2>/dev/null | wc -l)
    echo "  $i) $s  ($wins terminal)"
    i=$((i+1))
  done
  echo ""
  echo "Ketik nomor untuk LANJUT ke session tersebut."
  echo "Ketik 'b' buat buka session baru dari nol."
  echo "Ketik 0 = keluar."
  echo ""
  printf "Pilihan: "
  read -r C
  case "$C" in
    b|n|B|N) ;;
    0|q) clear; echo "Sampai jumpa. Tutup halaman ini kalau selesai."; sleep 2; exit 0 ;;
    [0-9]*)
      [ "$C" -ge 1 ] 2>/dev/null || { echo "Pilihan gak valid. Ulangi."; sleep 1; exec "$0"; }
      S=$(echo "$SESSIONS" | sed -n "${C}p")
      if [ -n "$S" ]; then
        clear
        echo "Lanjut ke session: $S"
        sleep 1
        exec tmux attach-session -t "$S"
      else
        echo "Nomor $C gak ada. Ulangi."; sleep 1; exec "$0"
      fi
      ;;
    *) echo "Pilihan gak valid. Ulangi."; sleep 1; exec "$0" ;;
  esac
else
  echo ""
  echo "Belum ada session. Buka yang baru di bawah."
  echo ""
fi

echo ""
echo "Mau buka berapa terminal? (maks $TERM_TOTAL)"
echo "  1  = 1 terminal"
echo "  2  = 2 terminal"
echo ""
echo "Tips: buka 2 kalau mau kerja barengan"
echo "      (misal nulis + lihat log bersamaan)."
echo ""
echo "Ketik 0 = keluar."
echo ""

N=""
while [ -z "$N" ]; do
  printf "Jumlah terminal [1-%s]: " "$TERM_TOTAL"
  read -r N
done

if [ "$N" = "0" ] || [ "$N" = "q" ]; then
  clear
  echo "Sampai jumpa. Tutup halaman ini kalau selesai."
  sleep 2
  exit 0
fi

case "$N" in
  ''|*[!0-9]*) echo "Bukan angka. Ulangi."; sleep 1; exec "$0" ;;
esac
[ "$N" -gt "$TERM_TOTAL" ] && N=$TERM_TOTAL

# buat session tmux unik per pembukaan
SESSION="$SESSION_PREFIX-$(date +%s)"
W=0

if [ "$N" -eq 1 ]; then
  tmux new-session -d -s "$SESSION" -x 220 -y 55
  tmux rename-window -t "$SESSION" terminal-1
  W=1
else
  tmux new-session -d -s "$SESSION" -x 220 -y 55 -n terminal-1
  W=1
  for i in $(seq 2 "$N"); do
    tmux new-window -t "$SESSION" -n "terminal-$i"
    W=$i
  done
fi

clear
echo "Siap: $N terminal dibuka (window terminal-1 s/d terminal-$W)."
echo ""
echo "NAVIGASI (dalam terminal):"
echo "  Tambah terminal    : Ctrl-b  lalu  c"
echo "  Pindah terminal    : Ctrl-b  lalu  nomor (1,2,3,...)"
echo "  Lihat daftar       : Ctrl-b  lalu  w"
echo "  Tutup 1 terminal   : ketik  exit"
echo ""
echo "Tutup tab gak selesaiin kerjaan — session tetap hidup,"
echo "buka lagi halaman ini nanti tinggal pilih LANJUT."
echo ""
sleep 2

exec tmux attach-session -t "$SESSION"