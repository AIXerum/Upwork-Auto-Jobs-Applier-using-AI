"""
Test the Upwork scraper to diagnose why it's returning 0 jobs
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_scraper():
    print("\n🔍 DIAGNOSING UPWORK SCRAPER")
    print("="*70)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        search_query = "AI Agent Developer"
        url = f'https://www.upwork.com/nx/search/jobs?q={search_query}&sort=recency&page=1&per_page=10'

        print(f"\n1. Testing URL: {url}")
        driver.get(url)

        print("2. Waiting 5 seconds for page load...")
        time.sleep(5)

        # Save screenshot
        screenshot_path = './debug_screenshot.png'
        driver.save_screenshot(screenshot_path)
        print(f"3. Screenshot saved to: {screenshot_path}")

        # Check page title
        print(f"4. Page title: {driver.title}")

        # Try to find jobs with old selector
        print("\n5. Testing OLD CSS selector: article[data-test=\"JobTile\"]")
        jobs_old = driver.find_elements(By.CSS_SELECTOR, 'article[data-test="JobTile"]')
        print(f"   Found: {len(jobs_old)} jobs")

        # Try alternative selectors
        print("\n6. Testing alternative selectors:")

        selectors_to_try = [
            'article.job-tile',
            'div.job-tile',
            'section.job-tile',
            'article',
            'div[data-ev-label="search_result"]',
            'div.up-card-section',
            'section[data-test="JobTile"]'
        ]

        for selector in selectors_to_try:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                if len(elements) > 0:
                    print(f"   ✅ {selector}: Found {len(elements)} elements")
                else:
                    print(f"   ❌ {selector}: 0 elements")
            except Exception as e:
                print(f"   ❌ {selector}: Error - {str(e)}")

        # Check page source for clues
        print("\n7. Checking page source for 'job' keywords...")
        page_source = driver.page_source.lower()

        if 'sign up' in page_source or 'log in' in page_source:
            print("   ⚠️  LOGIN REQUIRED - Upwork is blocking anonymous access!")

        if 'robot' in page_source or 'captcha' in page_source:
            print("   ⚠️  CAPTCHA/BOT DETECTION - Upwork detected automation!")

        if 'job-tile' in page_source:
            print("   ✅ Page contains 'job-tile' text")
        else:
            print("   ❌ Page doesn't contain 'job-tile' text")

        # Save page source
        with open('./debug_page_source.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        print("\n8. Full page source saved to: debug_page_source.html")

    finally:
        driver.quit()

    print("\n" + "="*70)
    print("📊 DIAGNOSIS COMPLETE")
    print("="*70)

if __name__ == "__main__":
    test_scraper()
