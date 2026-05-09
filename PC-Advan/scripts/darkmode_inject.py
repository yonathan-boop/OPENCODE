import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(2)

# F12 buka DevTools
pyautogui.press('f12')
time.sleep(2)

# Click Console tab (biasanya tab ke-2 atau 3)
# Fallback: Ctrl+` atau Escape
pyautogui.hotkey('ctrl', '`')
time.sleep(1)

# Inject dark mode CSS
js_code = """
(function() {
    if (document.getElementById('__darkmode_injected')) return;
    var s = document.createElement('style');
    s.id = '__darkmode_injected';
    s.textContent = `
        html { filter: invert(0.9) hue-rotate(180deg) !important; }
        img, video, iframe, canvas { filter: invert(1) hue-rotate(180deg) !important; }
    `;
    document.head.appendChild(s);
    console.log('Dark mode injected!');
})();
"""

pyautogui.write(js_code, interval=0.01)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('f12')

print("Dark mode injected!")
