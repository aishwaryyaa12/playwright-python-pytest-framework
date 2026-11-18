import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_swag_labs_login_success(page):
    """Verifies that a valid user can successfully log in and see the inventory."""
    login_page = LoginPage(page).load()
    login_page.login(Config.STANDARD_USER, Config.STANDARD_PASSWORD)
    
    inventory_page = InventoryPage(page)
    assert inventory_page.get_page_title().upper() == "PRODUCTS"
    
    products = inventory_page.get_product_names()
    assert len(products) > 0, "Inventory should contain at least one product."

@pytest.mark.ui
@pytest.mark.negative
def test_swag_labs_invalid_login(page):
    """Verifies that an invalid password produces the expected error banner."""
    login_page = LoginPage(page).load()
    login_page.login(Config.STANDARD_USER, "wrong_password_123")
    
    error_msg = login_page.get_error_message()
    assert "Username and password do not match" in error_msg

@pytest.mark.ui
@pytest.mark.regression
def test_add_product_to_cart(page):
    """Verifies that adding a product increases the shopping cart badge count."""
    login_page = LoginPage(page).load()
    login_page.login(Config.STANDARD_USER, Config.STANDARD_PASSWORD)
    
    inventory_page = InventoryPage(page)
    initial_count = inventory_page.get_cart_count()
    assert initial_count == 0
    
    inventory_page.add_first_product_to_cart()
    assert inventory_page.get_cart_count() == 1
