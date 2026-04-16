import requests
import time
import os
import json

TOKEN = "8356106029:AAGQbwB38ZFFt4EwdIxslBR5NaQAwIQ-jlI"
USER_ID = "5508090479"
API_URL = f"https://api.telegram.org/bot{TOKEN}"
OPENCODE_URL = "http://127.0.0.1:18789"

INBOX_FILE = "C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_inbox.txt"
OUTBOX_FILE = "C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_outbox.txt"

def get_updates(offset=None):
    url = f"{API_URL}/getUpdates"
    params = {"timeout": 1, "offset": offset}
    try:
        resp = requests.get(url, params=params, timeout=5)
        return resp.json().get("result", [])
    except:
        return []

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, data=data, timeout=10)
    except:
        pass

def ask_opencode(prompt):
    try:
        resp = requests.post(
            f"{OPENCODE_URL}/api/chat",
            json={"message": prompt},
            timeout=60
        )
        if resp.status_code == 200:
            return resp.json().get("response", "No response")
    except Exception as e:
        return "Error: {}".format(str(e))
    return "OpenCode not responding"

def main():
    print("Telegram-OpenCode Bridge started")
    offset = None
    
    while True:
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            if "message" in update:
                msg = update["message"]
                chat_id = msg["chat"]["id"]
                text = msg.get("text", "")
                
                if str(chat_id) == str(USER_ID) and text:
                    print("[IN] {}".format(text))
                    # Get response from OpenCode
                    response = ask_opencode(text)
                    print("[OUT] {}".format(response[:100] if len(response) > 100 else response))
                    # Send response back to Telegram
                    send_message(chat_id, response)
        time.sleep(1)

if __name__ == "__main__":
    main()
