from playwright.sync_api import Page
from .base_page import BasePage

class CheckoutOverviewPage(BasePage):
    FINISH_BUTTON = "#finish"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def finish(self):
        self.page.click(self.FINISH_BUTTON)
