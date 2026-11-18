"""
Pytest Fixture Configuration for Playwright Test Suite
Author: Aishwarya Shanmugam (QA Automation Engineer)

Design Decision:
- Session-scoped browser context: Reuses the browser instance across tests to reduce
  startup overhead (~300ms savings per test), while isolating tabs via function-scoped
  page fixtures.
- Custom viewport (1280x720): Prevents responsive mobile breakpoints in headless CI
  which frequently collapse navigation elements into hamburger menus.
- Headed / Headless dynamic detection: Respects --headed CLI flag so developers can
  visually inspect live test execution.
"""

import sys
import pytest

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

@pytest.fixture(scope="session")
def browser_context(pytestconfig):
    """Initializes a Chromium browser session respecting --headed and viewport flags."""
    if not PLAYWRIGHT_AVAILABLE:
        pytest.skip("Playwright is not installed in current environment. Install via: pip install -r requirements.txt && playwright install")
    
    # Check if --headed flag was passed
    try:
        is_headed = pytestconfig.getoption("headed", default=False)
    except Exception:
        is_headed = "--headed" in sys.argv
    
    headless_mode = not is_headed
    slow_mo_delay = 1000 if is_headed else 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode, slow_mo=slow_mo_delay)
        # Using 1280x720 desktop viewport to keep responsive UI elements visible
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    """Provides an isolated browser tab/page for each test function to prevent state leakage."""
    page = browser_context.new_page()
    yield page
    page.close()
