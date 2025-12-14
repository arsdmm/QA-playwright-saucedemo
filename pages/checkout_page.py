from playwright.sync_api import Page
from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)

    def continue_next(self):
        self.page.click(self.CONTINUE_BUTTON)