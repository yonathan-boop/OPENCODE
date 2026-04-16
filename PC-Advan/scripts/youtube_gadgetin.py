from playwright.sync_api import sync_playwright
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout, encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Buka YouTube cari Gadgetin
    page.goto("https://youtube.com/results?search_query=gadgetin")
    time.sleep(3)
    
    # Klik channel Gadgetin
    try:
        channel = page.locator("a[href*='/channel/']").first
        channel.click()
        time.sleep(3)
    except:
        print("Tidak ketemu channel, lanjut ke search result")
    
    # Scroll untuk lihat video
    page.evaluate("window.scrollBy(0, 500)")
    time.sleep(2)
    
    # Ambil info video terbaru
    videos = page.query_selector_all("ytd-grid-video-renderer")
    print(f"Ditemukan {len(videos)} video")
    
    if videos:
        latest = videos[0]
        title = latest.query_selector("#video-title")
        views = latest.query_selector("#metadata-line")
        print(f"Video terbaru: {title.inner_text() if title else 'Unknown'}")
        if views:
            print(f"Views: {views.inner_text()}")
        
        # Klik video terbaru
        latest.click()
        time.sleep(5)
        
        # Scroll ke komentar
        page.evaluate("window.scrollBy(0, 500)")
        time.sleep(2)
        
        # Ambil komentar
        comments = page.query_selector_all("ytd-comment-thread-renderer")
        print(f"\nKomentar teratas ({len(comments)} ditampilkan):")
        for i, comment in enumerate(comments[:3]):
            author = comment.query_selector("#author-text")
            text = comment.query_selector("#content-text")
            if author and text:
                print(f"{i+1}. {author.inner_text()}: {text.inner_text()[:100]}")
    
    browser.close()