import pytest
from pages.jamoona_home_page import JamoonaHomePage
from pages.jamoona_search_page import JamoonaSearchPage

@pytest.mark.ui
@pytest.mark.smoke
def test_jamoona_homepage_loads(page):
    """Verifies that the Jamoona German homepage loads successfully with branding."""
    home_page = JamoonaHomePage(page).load()
    
    title = home_page.get_title()
    assert "Jamoona" in title, f"Expected 'Jamoona' in title, got: {title}"
    assert "Indischer Online-Shop" in title or "Jamoona" in title

@pytest.mark.ui
@pytest.mark.regression
def test_jamoona_search_product(page):
    """Verifies searching for 'Sona Masoori' returns active grocery product listings."""
    home_page = JamoonaHomePage(page).load()
    home_page.search_for("Sona Masoori")
    
    # Assert URL transitioned to search results
    current_url = page.url
    assert "search?q=Sona Masoori" in current_url, f"Expected search query in URL, got {current_url}"
    
    # Verify product items returned on the search page
    search_page = JamoonaSearchPage(page)
    products = search_page.get_product_titles()
    
    assert len(products) > 0, "Expected search results for 'Sona Masoori' to be non-empty."
    
    # Assert relevant search keywords appear in the top results
    top_matches = [p.lower() for p in products[:5]]
    assert any("Sona Masoori" in p or "reis" in p for p in top_matches), f"Top results did not contain expected terms: {top_matches}"
