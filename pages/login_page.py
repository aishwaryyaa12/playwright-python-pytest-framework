from typing import Any
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for the SauceDemo Login Page."""

    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Any):
        super().__init__(page)

    def load(self):
        self.navigate(self.URL)
        return self

    def enter_username(self, username: str):
        self.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        self.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
