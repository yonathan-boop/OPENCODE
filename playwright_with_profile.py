from playwright.sync_api import sync_playwright
import time

CHROME_USER_DATA = "C:/Users/Admin/AppData/Local/Google/Chrome/User Data"

def open_with_existing_profile():
    with sync_playwright() as p:
        # Gunakan launch_persistent_context untuk existing profile
        context = p.chromium.launch_persistent_context(
            user_data_dir=CHROME_USER_DATA,
            headless=False
        )
        page = context.new_page()
        print("Chrome dengan profile existing opened!")
        print("Login/cookies akan TETAP tersimpan!")
        time.sleep(5)
        context.close()

if __name__ == "__main__":
    print("Opening Chrome dengan existing profile...")
    open_with_existing_profile()
