import pyautogui
import time
from PIL import ImageGrab
import pytesseract

# Klik profile Chrome (biasanya profil pertama)
pyautogui.click(400, 400)  # Klik di area profil
time.sleep(3)

# Sekarang sudah di Chrome, minimize dulu jika ada menu lain
pyautogui.press('f11')  # Fullscreen
time.sleep(1)

# Buka YouTube langsung
pyautogui.typewrite('youtube.com')
pyautogui.press('enter')
time.sleep(5)

# Search Gadgetin
pyautogui.typewrite('gadgetin')
pyautogui.press('enter')
time.sleep(3)

# Ambil screenshot
img = ImageGrab.grab()
img.save(r'C:\Users\Advan\Desktop\screenshot.png')
print("Screenshot saved")

# OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img, lang='eng+ind')
print(text)