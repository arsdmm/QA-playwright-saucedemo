from playwright.sync_api import Page
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CHECKOUT_BUTTON = "#checkout"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.CART_ITEM)

    def get_items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    def get_item_names(self) -> list[str]:
        elements = self.page.locator(self.CART_ITEM_NAME)
        return [elements.nth(i).inner_text() for i in range(elements.count())]
    
    def checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)