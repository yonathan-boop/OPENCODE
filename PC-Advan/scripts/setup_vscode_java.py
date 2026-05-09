import pyautogui
import time
import subprocess

pyautogui.FAILSAFE = True
time.sleep(1)

# Buka VS Code
vscode_path = r'C:\Users\Advan\AppData\Local\Programs\Microsoft VS Code\Code.exe'
subprocess.Popen([vscode_path])
time.sleep(8)

# Ctrl+Shift+X buka Extensions
pyautogui.hotkey('ctrl', 'shift', 'x')
time.sleep(3)

# Cari Extension Pack for Java
pyautogui.write('Extension Pack for Java', interval=0.05)
time.sleep(3)

# Klik Install (enter)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)

# Tutup search bar
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)

print("VS Code Java setup done!")
