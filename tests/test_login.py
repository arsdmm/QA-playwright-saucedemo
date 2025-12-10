from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(page: Page, base_url: str):
    login_page = LoginPage(page, base_url)
    inventory_page = InventoryPage(page, base_url)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded(), "Inventory page should be visible after login"

    assert inventory_page.get_items_count() > 0, "There should be at least one item in inventory"
