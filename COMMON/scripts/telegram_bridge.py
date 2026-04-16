import requests
import time
import os

TOKEN = "8356106029:AAGQbwB38ZFFt4EwdIxslBR5NaQAwIQ-jlI"
USER_ID = "5508090479"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

INBOX_FILE = "C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_inbox.txt"
OUTBOX_FILE = "C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_outbox.txt"

def get_updates(offset=None):
    url = f"{API_URL}/getUpdates"
    params = {"timeout": 1, "offset": offset}
    try:
        resp = requests.get(url, params=params, timeout=5)
        return resp.json().get("result", [])
    except Exception as e:
        # Silently ignore errors to keep bot running
        return []

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    try:
        resp = requests.post(url, data=data, timeout=5)
        return resp.ok
    except Exception:
        return False

def main():
    print("Telegram bridge started...")
    offset = None
    while True:
        # Check for incoming messages
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            if "message" in update:
                message = update["message"]
                chat_id = message["chat"]["id"]
                text = message.get("text", "")
                from_name = message["chat"].get("first_name", "User")
                # Only process messages from the authorized user
                if str(chat_id) == str(USER_ID):
                    # Write the incoming message to inbox.txt
                    with open(INBOX_FILE, "w", encoding="utf-8") as f:
                        f.write(f"{from_name}: {text}")
                    print("[IN] Received from {}: {}".format(from_name, text))
        
        # Check for outgoing responses
        if os.path.exists(OUTBOX_FILE):
            with open(OUTBOX_FILE, "r", encoding="utf-8") as f:
                response = f.read().strip()
            if response:
                # Send the response
                if send_message(USER_ID, response):
                    print("[OUT] Sent response: {}".format(response))
                # Clear the outbox file
                with open(OUTBOX_FILE, "w", encoding="utf-8") as f:
                    f.write("")
        
        time.sleep(1)

if __name__ == "__main__":
    main()