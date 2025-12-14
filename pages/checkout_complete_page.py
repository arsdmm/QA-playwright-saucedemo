from playwright.sync_api import Page
from .base_page import BasePage

class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = ".complete-header"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def is_success(self) -> bool:
        return self.page.is_visible(self.COMPLETE_HEADER)

    def success_text(self) -> str:
        return self.page.inner_text(self.COMPLETE_HEADER)
