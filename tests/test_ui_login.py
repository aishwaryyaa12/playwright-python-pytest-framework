import pytest
from pages.base_page import BasePage

@pytest.mark.ui
@pytest.mark.regression
def test_swag_labs_login_success(page):
    base_page = BasePage(page)
    base_page.navigate("https://www.saucedemo.com/")
    
    base_page.fill("#user-name", "standard_user")
    base_page.fill("#password", "secret_sauce")
    base_page.click("#login-button")
    
    title_text = base_page.get_text(".title")
    assert title_text.upper() == "PRODUCTS"

@pytest.mark.ui
def test_swag_labs_invalid_login(page):
    base_page = BasePage(page)
    base_page.navigate("https://www.saucedemo.com/")
    
    base_page.fill("#user-name", "invalid_user")
    base_page.fill("#password", "wrong_password")
    base_page.click("#login-button")
    
    error_msg = base_page.get_text("[data-test='error']")
    assert "Username and password do not match" in error_msg
