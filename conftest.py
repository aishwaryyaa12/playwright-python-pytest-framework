import pytest

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

@pytest.fixture(scope="session")
def browser_context():
    """Initializes a headless Chromium browser session with standard viewport."""
    if not PLAYWRIGHT_AVAILABLE:
        pytest.skip("Playwright is not installed in current environment. Install via: pip install playwright && playwright install")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    """Provides an isolated browser tab/page for each test function."""
    page = browser_context.new_page()
    yield page
    page.close()
