import pytest
import requests

@pytest.mark.api
def test_get_products_list_api():
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    assert response.status_code == 200
    
    data = response.json()
    assert "products" in data
    assert len(data["products"]) > 0

@pytest.mark.api
def test_single_product_details_api():
    url = "https://dummyjson.com/products/1"
    response = requests.get(url)
    assert response.status_code == 200
    
    product = response.json()
    assert product["id"] == 1
    assert "title" in product
    assert product["price"] > 0
