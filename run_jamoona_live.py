"""
Live Visual Demo: Jamoona.com (DE) Product Search
Run this script directly to watch Playwright open the browser on your screen!
"""

import time
from playwright.sync_api import sync_playwright

def run():
    print("Launching visible Chromium browser on your desktop...")
    with sync_playwright() as p:
        # headless=False opens the visible browser window on your screen
        browser = p.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        print("[1/3] Navigating to https://www.jamoona.com/de ...")
        page.goto("https://www.jamoona.com/de", wait_until="domcontentloaded")
        time.sleep(1)

        # Handle cookie banner if present
        cookie_btn = page.locator("#onetrust-accept-btn-handler, button:has-text('Alle akzeptieren')")
        if cookie_btn.is_visible():
            print("  Dismissing cookie banner...")
            cookie_btn.click()
            time.sleep(0.5)

        print("[2/3] Searching for 'Basmati Rice' in the search bar...")
        search_box = page.locator("input[name='q']").first
        search_box.click()
        search_box.fill("Basmati")
        search_box.press("Enter")

        print("[3/3] Waiting for search results to load...")
        page.wait_for_load_state("domcontentloaded")
        time.sleep(2)

        # Extract top product titles
        titles = page.locator(".card__heading, .card-information a, h3").all_inner_texts()
        clean_titles = [t.strip() for t in titles if t.strip() and "basmati" in t.lower()]
        
        print("\n--- Live Search Results Found on Jamoona ---")
        for idx, t in enumerate(clean_titles[:5], 1):
            print(f"  {idx}. {t}")

        print("\nKeeping browser open for 5 seconds so you can see it...")
        time.sleep(5)
        browser.close()
        print("Done!")

if __name__ == "__main__":
    run()
