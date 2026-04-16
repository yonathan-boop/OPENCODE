
from playwright.sync_api import sync_playwright
CHROME_USER_DATA = r"C:\Users\Admin\AppData\Local\Google\Chrome\User Data"
def open_with_existing_profile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, user_data_dir=CHROME_USER_DATA)
        page = browser.new_page()
        print("Chrome dengan profile existing opened!")
        input("Tekan Enter...")
        browser.close()
def open_fresh():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        print("Chrome fresh - tidak ada cookie!")
        input("Tekan Enter...")
        browser.close()
def goto(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, user_data_dir=CHROME_USER_DATA)
        page = browser.new_page()
        page.goto(url)
        print(f"Buka: {url}")
        input("Tekan Enter...")
        browser.close()
if __name__ == "__main__":
    print("1. Existing Profile (RECOMMENDED)")
    print("2. Fresh Browser")
    print("3. Buka URL tertentu")
    c = input("Pilih: ")
    if c == "1": open_with_existing_profile()
    elif c == "2": open_fresh()
    elif c == "3": goto(input("URL: "))
