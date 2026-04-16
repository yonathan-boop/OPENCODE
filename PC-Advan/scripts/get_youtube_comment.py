import pyautogui
import time
from PIL import ImageGrab
import pytesseract

# Set the path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open Chrome and go to Gadgetin videos page
pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

# Type the URL for Gadgetin videos
pyautogui.typewrite('https://www.youtube.com/@Gadgetin/videos')
pyautogui.press('enter')
time.sleep(5)

# Click on the first video (assuming it's the first item in the grid)
# We'll click at a position that is likely to be the first video thumbnail
# Adjust these coordinates if necessary
pyautogui.click(400, 300)  # Example coordinates, may need adjustment
time.sleep(5)  # Wait for video page to load

# Scroll down to load comments
for i in range(5):
    pyautogui.scroll(-300)  # Scroll down
    time.sleep(1)

# Now try to locate the top comment area
# We'll take a screenshot of a region where the top comment is likely to be
# Adjust the region based on your screen resolution
# For example, on a 1080p screen, the comment might be around (200, 400) to (800, 600)
# But we don't know the exact position. Let's try a region and hope.

# Take a screenshot of the entire screen
img = ImageGrab.grab()
# Save the screenshot for reference (optional)
img.save(r'C:\Users\Advan\Desktop\screenshot_full.png')

# Now, let's try to crop to a region where the comment might be
# We'll try a region that is likely to contain the top comment
# This is a guess and might need adjustment
left = 200
top = 400
right = 800
bottom = 1000
img_crop = img.crop((left, top, right, bottom))
img_crop.save(r'C:\Users\Advan\Desktop\screenshot_comment.png')

# Now use OCR on the cropped image
text = pytesseract.image_to_string(img_crop, lang='eng+ind')
print("OCR Result:")
print(text)