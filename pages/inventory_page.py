from playwright.sync_api import Page
from .base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_SIDEBAR_LINK = "#logout_sidebar_link"

    ADD_TO_CART_BUTTON = "button.btn_inventory"
    CART_LINK = ".shopping_cart_link"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.INVENTORY_CONTAINER)

    def get_items_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEM).count()

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def logout(self):
        self.page.click(self.BURGER_MENU)
        self.page.click(self.LOGOUT_SIDEBAR_LINK)
