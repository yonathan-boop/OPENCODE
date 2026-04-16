import pyautogui
import time

# Focus ke Chrome (假设 Chrome 已经在运行)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

# 如果还没打开 YouTube，手动打开
# 这里假设用户已经在 Chrome 中打开了 YouTube 并登录了

# 等待用户操作：让用户自己搜索 Gadgetin 或打开频道
print("请在 Chrome 中打开 YouTube 并搜索 Gadgetin 或打开其频道")
print("准备好后告诉我，我再来截图读取信息")

# 保存当前截图供参考
from PIL import ImageGrab
img = ImageGrab.grab()
img.save(r'C:\Users\Advan\Desktop\screenshot.png')
print("Screenshot saved")