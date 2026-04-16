from playwright.sync_api import sync_playwright
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout, encoding='utf-8')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
user_data_dir = r"C:\Users\Advan\AppData\Local\Google\Chrome\User Data\Default"

with sync_playwright() as p:
    try:
        context = p.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,
            executable_path=chrome_path
        )
        
        page = context.new_page()
        
        # Buka YouTube
        page.goto("https://youtube.com")
        time.sleep(5)
        
        print("Berhasil akses YouTube!")
        
        # Cari Gadgetin
        page.goto("https://www.youtube.com/@Gadgetin")
        time.sleep(3)
        
        # Scroll dan ambil video
        page.evaluate("window.scrollBy(0, 300)")
        time.sleep(2)
        
        # Ambil video terbaru
        videos = page.query_selector_all("ytd-grid-video-renderer")
        print(f"Ditemukan {len(videos)} video")
        
        if videos:
            latest = videos[0]
            title = latest.query_selector("#video-title")
            if title:
                print(f"Video terbaru: {title.inner_text()}")
                
                # Klik video
                title.click()
                time.sleep(5)
                
                # Scroll ke komentar
                page.evaluate("window.scrollBy(0, 500)")
                time.sleep(2)
                
                # Ambil komentar
                comments = page.query_selector_all("ytd-comment-thread-renderer")[:3]
                print(f"\nKomentar teratas:")
                for i, comment in enumerate(comments):
                    author = comment.query_selector("#author-text")
                    text = comment.query_selector("#content-text")
                    if author and text:
                        print(f"{i+1}. {author.inner_text()}: {text.inner_text()[:80]}")
        
        print("\nSelesai! Browser akan tertutup otomatis...")
        time.sleep(3)
        context.close()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()