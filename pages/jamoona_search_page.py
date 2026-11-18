from typing import List, Any
from pages.base_page import BasePage

class JamoonaSearchPage(BasePage):
    """Page Object for Jamoona Search Results Page."""

    # Locators
    PRODUCT_CARDS = ".card__heading, .product-card__title, .card-information a"
    PRODUCT_TITLE_LINKS = ".card__heading a"
    RESULTS_COUNT_TEXT = ".search-results-count, h1"

    def __init__(self, page: Any):
        super().__init__(page)

    def get_product_titles(self) -> List[str]:
        """Returns the list of product titles visible in the search results."""
        self.page.wait_for_selector(self.PRODUCT_CARDS, state="visible", timeout=10000)
        items = self.page.locator(self.PRODUCT_CARDS).all_inner_texts()
        return [item.strip() for item in items if item.strip()]

    def get_first_product_title(self) -> str:
        """Returns the title of the first matching product."""
        titles = self.get_product_titles()
        return titles[0] if titles else ""
