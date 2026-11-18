from typing import Any
from pages.base_page import BasePage

class JamoonaHomePage(BasePage):
    """Page Object for Jamoona.com/de E-Commerce Homepage."""

    URL = "https://www.jamoona.com/de"

    # Locators
    SEARCH_INPUT = "input[name='q']"
    HEADER_LOGO = ".header__heading-logo, header a[href*='/de']"
    CART_LINK = "a[href*='/cart']"
    COOKIE_ACCEPT_BUTTON = "#onetrust-accept-btn-handler, button:has-text('Alle akzeptieren'), button:has-text('Akzeptieren')"

    def __init__(self, page: Any):
        super().__init__(page)

    def load(self):
        """Navigates to the Jamoona DE homepage and handles any cookie prompts."""
        self.navigate(self.URL)
        # Dismiss cookie banner if it appears
        if self.is_visible(self.COOKIE_ACCEPT_BUTTON):
            try:
                self.click(self.COOKIE_ACCEPT_BUTTON)
            except Exception:
                pass
        return self

    def search_for(self, query: str):
        """Types a search term into the search bar and submits."""
        self.page.wait_for_selector(self.SEARCH_INPUT, state="visible")
        search_field = self.page.locator(self.SEARCH_INPUT).first
        search_field.fill(query)
        search_field.press("Enter")
        self.page.wait_for_load_state("domcontentloaded")
        return self
