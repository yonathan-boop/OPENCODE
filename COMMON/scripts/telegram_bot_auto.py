import requests
import time

TOKEN = "8356106029:AAGQbwB38ZFFt4EwdIxslBR5NaQAwIQ-jlI"
USER_ID = "5508090479"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

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
    print("Telegram bot started (auto-reply mode)...")
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            if "message" in update:
                message = update["message"]
                chat_id = message["chat"]["id"]
                text = message.get("text", "")
                from_name = message["chat"].get("first_name", "User")
                # Only respond to the authorized user
                if str(chat_id) == str(USER_ID):
                    reply = f"Pesan diterima: {text}"
                    send_message(chat_id, reply)
        time.sleep(1)

if __name__ == "__main__":
    main()