"""
Chrome Automation with PyAutoGUI
=================================
Gunakan cara ini - lebih simple dan TIDAK ada masalah encryption.
Login yang sudah ada di Chrome akan tetap tersimpan!

Install: pip install pyautogui
Jalankan: py chrome_automation.py
"""

import pyautogui
import time
import os

def open_chrome_and_navigate(url=""):
    """Buka Chrome dan navigasi ke URL"""
    print("1. Membuka Chrome...")
    os.startfile('chrome')
    time.sleep(3)  # Tunggu Chrome buka
    
    if url:
        print(f"2. Mengetik URL: {url}")
        pyautogui.write(url, interval=0.05)
        pyautogui.press('enter')
        time.sleep(2)
    
    print("3. Screenshot...")
    pyautogui.screenshot('C:/Users/Admin/Desktop/memory/chrome_automation.png')
    print("Done! Chrome tetap dengan login yang tersimpan.")

def focus_existing_chrome():
    """Fokus ke Chrome yang sudah terbuka"""
    print("1. Mencari Chrome di taskbar...")
    
    # Coba tekan Windows+D untuk minimize semua, lalu klik Chrome
    pyautogui.hotkey('win', 'd')
    time.sleep(1)
    
    # Cari posisi Chrome di taskbar (biasanya urutan pertama)
    # Klik start button lalu ketik chrome
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('chrome')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    
    print("2. Screenshot...")
    pyautogui.screenshot('C:/Users/Admin/Desktop/memory/chrome_focused.png')
    print("Done!")

def refresh_page():
    """Refresh halaman Chrome"""
    print("Mereshresh halaman...")
    pyautogui.hotkey('f5')
    time.sleep(2)
    pyautogui.screenshot('C:/Users/Admin/Desktop/memory/chrome_refreshed.png')

def open_new_tab():
    """Buka tab baru di Chrome"""
    print("Membuka tab baru...")
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)

def close_tab():
    """Tutup tab"""
    print("Menutup tab...")
    pyautogui.hotkey('ctrl', 'w')

# ===== MAIN =====
if __name__ == "__main__":
    print("=" * 50)
    print("CHROME AUTOMATION with PyAutoGUI")
    print("=" * 50)
    print("1. Buka Chrome + URL")
    print("2. Focus ke Chrome yang sudah terbuka")
    print("3. Refresh halaman")
    print("4. Buka tab baru")
    print("5. Exit")
    
    # Auto select option 1 - Buka Chrome dengan existing session
    print("\nOtomatis memilih: Buka Chrome...")
    open_chrome_and_navigate()
