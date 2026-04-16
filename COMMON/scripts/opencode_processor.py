import subprocess
import time
import os

INBOX_FILE = "C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_inbox.txt"
OUTBOX_FILE = "C:/Users/Admin/Desktop/memory/COMMON/scripts/telegram_outbox.txt"

print("OpenCode processor started...")

last_content = ""

while True:
    if os.path.exists(INBOX_FILE):
        with open(INBOX_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
        
        if content and content != last_content:
            last_content = content
            
            # Extract message (remove "Nggak: " prefix if present)
            message = content
            if ": " in content:
                message = content.split(": ", 1)[1]
            
            print("[PROCES] Processing: {}".format(message))
            
            # Call OpenCode
            try:
                result = subprocess.run(
                    ["opencode", "-c", message],
                    capture_output=True,
                    text=True,
                    timeout=120,
                    cwd="C:/Users/Admin/Desktop/memory"
                )
                response = result.stdout.strip() if result.stdout else result.stderr.strip()
                if not response:
                    response = "No response from OpenCode"
            except subprocess.TimeoutExpired:
                response = "Timeout - OpenCode takes too long"
            except Exception as e:
                response = "Error: {}".format(str(e))
            
            # Write response to outbox
            with open(OUTBOX_FILE, "w", encoding="utf-8") as f:
                f.write(response)
            print("[DONE] Response written to outbox")
            
            # Clear inbox to prevent reprocessing
            with open(INBOX_FILE, "w", encoding="utf-8") as f:
                f.write("")
    
    time.sleep(2)
