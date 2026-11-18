from typing import Any

class BasePage:
    """Base class for all Page Objects with common Playwright interactions."""

    def __init__(self, page: Any):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str):
        self.page.wait_for_selector(selector, state="visible")
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.wait_for_selector(selector, state="visible")
        self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        self.page.wait_for_selector(selector, state="visible")
        return self.page.inner_text(selector).strip()

    def is_visible(self, selector: str) -> bool:
        try:
            return self.page.is_visible(selector)
        except Exception:
            return False

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url
