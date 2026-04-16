import requests
import time
import os
from pathlib import Path

TOKEN = "8356106029:AAGQbwB38ZFFt4EwdIxslBR5NaQAwIQ-jlI"
USER_ID = "5508090479"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

MESSAGE_FILE = Path("C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_inbox.txt")
OUTBOX_FILE = Path("C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_outbox.txt")

def get_updates(offset=None):
    url = f"{API_URL}/getUpdates"
    params = {"timeout": 1}
    if offset:
        params["offset"] = offset
    try:
        resp = requests.get(url, params=params, timeout=5)
        return resp.json().get("result", [])
    except Exception as e:
        print(f"Error getUpdates: {e}")
        return []

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    try:
        resp = requests.post(url, data=data)
        return resp.ok
    except Exception as e:
        print(f"Error sendMessage: {e}")
        return False

def read_outbox():
    if OUTBOX_FILE.exists():
        with open(OUTBOX_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(OUTBOX_FILE, "w", encoding="utf-8") as f:
            f.write("")
        return [line.strip() for line in lines if line.strip()]
    return []

def main():
    print("Telegram Bot Started!")
    print(f"Token: {TOKEN[:20]}...")
    print(f"User ID: {USER_ID}")
    print("\nCara pakai:")
    print("  - Kirim pesan ke @Qksusb_bot dari HP kamu")
    print("  - Ketik pesan di terminal ini untuk dikirim ke Telegram")
    print("  - Ketik 'exit' untuk keluar\n")
    
    offset = None
    
    while True:
        updates = get_updates(offset)
        
        if updates:
            for update in updates:
                offset = update["update_id"] + 1
                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"].get("text", "")
                    from_name = update["message"]["chat"].get("first_name", "User")
                    
                    if str(chat_id) == str(USER_ID):
                        print(f"\n[IN] Pesan dari {from_name}: {text}")
                        with open(MESSAGE_FILE, "w", encoding="utf-8") as f:
                            f.write(f"{from_name}: {text}")
        
        outbox = read_outbox()
        for msg in outbox:
            success = send_message(USER_ID, msg)
            if success:
                print(f"[OUT] Terkirim ke Telegram: {msg}")
            else:
                print(f"❌ Gagal kirim: {msg}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
