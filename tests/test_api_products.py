import pytest
import requests
from utils.config import Config

@pytest.mark.api
@pytest.mark.smoke
def test_get_products_list_api():
    """Validates the GET /products endpoint schema, status code, and latency."""
    url = f"{Config.BASE_API_URL}/products"
    response = requests.get(url, timeout=10)
    
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    assert response.elapsed.total_seconds() < 2.0, "API response latency exceeded 2.0s"
    
    data = response.json()
    assert "products" in data, "Response payload missing 'products' key"
    assert "total" in data, "Response payload missing 'total' count"
    assert len(data["products"]) > 0, "Products list should not be empty"
    
    first_item = data["products"][0]
    required_keys = {"id", "title", "price", "category"}
    assert required_keys.issubset(first_item.keys()), f"Item missing required keys: {required_keys - set(first_item.keys())}"

@pytest.mark.api
@pytest.mark.regression
def test_single_product_details_api():
    """Validates retrieving a specific product by ID with accurate pricing and data types."""
    url = f"{Config.BASE_API_URL}/products/1"
    response = requests.get(url, timeout=10)
    
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert isinstance(product["title"], str) and len(product["title"]) > 0
    assert isinstance(product["price"], (int, float)) and product["price"] > 0

@pytest.mark.api
@pytest.mark.negative
def test_get_nonexistent_product_returns_404():
    """Validates negative API behavior: non-existent ID returns 404 Not Found."""
    url = f"{Config.BASE_API_URL}/products/999999"
    response = requests.get(url, timeout=10)
    
    assert response.status_code == 404
