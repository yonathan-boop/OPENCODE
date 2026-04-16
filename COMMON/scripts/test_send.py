import requests

TOKEN = "8356106029:AAGQbwB38ZFFt4EwdIxslBR5NaQAwIQ-jlI"
USER_ID = "5508090479"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": USER_ID, "text": "Halo Admin! Saya balas dari OpenCode - pesan dari Telegram berhasil diterima!"}

resp = requests.post(url, data=data)
print("OK" if resp.ok else "GAGAL")
print(resp.text)
