import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def inventory_page(page, base_url):
    login_page = LoginPage(page, base_url)
    inventory = InventoryPage(page, base_url)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert inventory.is_loaded(), "Inventory page should be visible after login"
    return inventory
