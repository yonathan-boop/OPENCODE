# Setup - Linux Tablet

Di-update: 28 April 2026

---

## 📋 Identitas

- **Device:** Red Magic Tab Astra 3 Pro
- **OS:** Android 15 (via Termux)
- **RAM:** 12 GB
- **Path:** /data/data/com.termux/files/home/Desktop/New Folder/memory

---

## 📋 Layer Sistem

```
Android 15
    │
    ▼ (proot-distro)
Ubuntu Linux (VNC) ←── Akses lewat VNC viewer
    │
    ▼ (QEMU)
Windows 11 ARM64 ←── Bisa booting!
```

---

## 📋 Cara Akses

### 1. Akses Linux (yang sekarang)
- Connect ke VNC: localhost:5901 (atau port sesuai VNC server)
- Username & password sesuai setup VNC

### 2. Akses Windows 11 ARM
- Saat ini QEMU belum otomatis jalan
- Jalanin manual:

```bash
# Masuk ke Linux (VNC), lalu:
cd /root/vm

# Jalanin QEMU:
xvfb-run -a qemu-system-aarch64 -M virt -m 4 -cpu max -bios QEMU_EFI.fd -cdrom /storage/emulated/0/Download/Win11_25H2_English_Arm64_v2.iso -boot d
```

- Connect ke VNC port 5900 buat lihat Windows

---

## 📋 Installasi yang Sudah Selesai

- QEMU ARM (`qemu-system-arm`) ✅
- Xvfb (`xvfb`) ✅
- UEFI Firmware (`QEMU_EFI.fd` 2MB) ✅
- File ISO: `Win11_25H2_English_Arm64_v2.iso` (7.9GB)

---

## 📋 Command Penting

```bash
# Cek QEMU process
ps aux | grep qemu

# Kill QEMU
pkill -9 qemu-system-aarch64

# Jalanin Windows ARM
cd /root/vm && xvfb-run -a qemu-system-aarch64 -M virt -m 4 -cpu max -bios QEMU_EFI.fd -cdrom /storage/emulated/0/Download/Win11_25H2_English_Arm64_v2.iso -boot d
```

---

## 📋 Catatan

- Emulasi via TCG (tanpa KVM) = LAMBAT
- Lebih baik install emulator lain (Limbo, AWVx) untuk performa
- EFI firmware di `/root/vm/QEMU_EFI.fd`

---