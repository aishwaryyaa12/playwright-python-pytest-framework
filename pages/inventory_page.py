from typing import List, Any
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object for the SauceDemo Inventory (Products) Page."""

    TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ADD_TO_CART_BTN = "button[id^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def __init__(self, page: Any):
        super().__init__(page)

    def get_page_title(self) -> str:
        return self.get_text(self.TITLE)

    def get_product_names(self) -> List[str]:
        self.page.wait_for_selector(self.ITEM_NAME)
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def add_first_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        return self

    def get_cart_count(self) -> int:
        if self.is_visible(self.CART_BADGE):
            text = self.get_text(self.CART_BADGE)
            return int(text) if text.isdigit() else 0
        return 0
