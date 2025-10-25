"""
Upwork job scraper using Puppeteer MCP server for browser automation
This allows us to use a real Chrome browser with authentication
"""
import json
import time


def scrape_upwork_with_puppeteer(search_query, num_jobs=10, mcp_tools=None):
    """
    Scrape Upwork jobs using Puppeteer MCP server

    Args:
        search_query: Job search query (e.g., "AI Developer")
        num_jobs: Number of jobs to scrape
        mcp_tools: Dictionary of MCP tool functions

    Returns:
        List of job dictionaries
    """
    if not mcp_tools:
        raise ValueError("MCP tools not provided. This scraper requires Puppeteer MCP.")

    job_listings = []

    try:
        # Construct Upwork search URL
        url = f'https://www.upwork.com/nx/search/jobs?q={search_query}&sort=recency&page=1&per_page={num_jobs}'

        print(f"\n🌐 Navigating to: {url}")

        # Navigate to Upwork search page
        nav_result = mcp_tools['puppeteer_navigate'](url=url)
        print(f"✅ Page loaded")

        # Wait a bit for the page to fully load
        time.sleep(3)

        # Take a snapshot to see the current state
        snapshot_result = mcp_tools['puppeteer_snapshot']()
        print(f"\n📸 Page snapshot captured")

        # Check if we need to login
        if 'sign in' in str(snapshot_result).lower() or 'log in' in str(snapshot_result).lower():
            print("\n⚠️  Login required!")
            print("Please login to Upwork in the browser window that just opened.")
            print("After logging in, the scraper will continue automatically.")

            # Wait for user to login manually
            input("\n👉 Press ENTER after you've logged in to Upwork...")

            # Navigate again after login
            mcp_tools['puppeteer_navigate'](url=url)
            time.sleep(3)
            snapshot_result = mcp_tools['puppeteer_snapshot']()

        # Now extract job listings from the page
        # The snapshot contains accessibility tree with all page elements
        page_content = str(snapshot_result)

        # Parse job tiles from the accessibility snapshot
        # This is a simplified parser - you may need to adjust based on actual Upwork structure
        jobs = parse_jobs_from_snapshot(page_content)

        if jobs:
            print(f"\n✅ Found {len(jobs)} jobs")
            job_listings = jobs[:num_jobs]
        else:
            print("\n⚠️  No jobs found. The page structure may have changed.")
            print("You can manually extract jobs from the browser window.")

    except Exception as e:
        print(f"\n❌ Error during scraping: {e}")
        print("Falling back to manual extraction...")

    return job_listings


def parse_jobs_from_snapshot(snapshot_content):
    """
    Parse job listings from Puppeteer accessibility snapshot

    This is a basic parser - you may need to enhance it based on
    the actual structure of Upwork's job listings
    """
    jobs = []

    # For now, return empty list
    # You would need to parse the accessibility tree here
    # The snapshot contains structured data about all page elements

    # TODO: Implement parser based on actual Upwork page structure
    # This would involve finding job tile elements and extracting:
    # - title
    # - link
    # - description
    # - job_type
    # - experience_level
    # - budget

    return jobs


def scrape_upwork_manual_assist(search_query, num_jobs=10, mcp_tools=None):
    """
    Interactive scraper that opens browser and guides user through manual extraction

    This is the most reliable approach for Upwork scraping since their structure
    changes frequently and they have anti-bot measures.
    """
    if not mcp_tools:
        raise ValueError("MCP tools not provided. This scraper requires Puppeteer MCP.")

    print("\n🚀 Starting interactive Upwork job scraper...")
    print(f"📝 Searching for: {search_query}")
    print(f"🎯 Target: {num_jobs} jobs\n")

    # Construct Upwork search URL
    url = f'https://www.upwork.com/nx/search/jobs?q={search_query}&sort=recency&page=1&per_page={num_jobs}'

    # Open Upwork in browser
    print(f"🌐 Opening Upwork: {url}")
    mcp_tools['puppeteer_navigate'](url=url)
    time.sleep(2)

    # Take screenshot
    print("📸 Taking screenshot...")
    screenshot_result = mcp_tools['puppeteer_screenshot'](
        name='upwork_jobs_page',
        width=1920,
        height=1080
    )

    print("\n" + "="*60)
    print("MANUAL SCRAPING ASSISTANCE")
    print("="*60)
    print("\nI've opened Upwork in a browser window.")
    print("If you're not logged in, please login now.")
    print("\nOnce logged in and you can see job listings:")
    print("1. You can manually copy job details")
    print("2. Or use browser DevTools to inspect job elements")
    print("3. Or take screenshots of jobs you're interested in")
    print("\nThe browser will stay open for you to review jobs.")
    print("="*60 + "\n")

    # Return empty for now - user can manually collect jobs
    return []


# Example usage function
def example_usage():
    """
    Example of how to use the Puppeteer-based scraper
    """
    # Note: In actual usage, you would need to pass MCP tool functions
    # This is just an example structure

    mcp_tools = {
        'puppeteer_navigate': lambda url: None,
        'puppeteer_snapshot': lambda: None,
        'puppeteer_screenshot': lambda **kwargs: None,
    }

    jobs = scrape_upwork_manual_assist(
        search_query="AI Developer",
        num_jobs=10,
        mcp_tools=mcp_tools
    )

    return jobs
