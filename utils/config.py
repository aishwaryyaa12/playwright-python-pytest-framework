import os

class Config:
    """Central configuration for test environments and credentials."""

    BASE_UI_URL = os.getenv("BASE_UI_URL", "https://www.saucedemo.com/")
    BASE_API_URL = os.getenv("BASE_API_URL", "https://dummyjson.com")
    
    STANDARD_USER = os.getenv("TEST_USER", "standard_user")
    STANDARD_PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")
    
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
