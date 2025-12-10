from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = ""):
        url = self.base_url + path
        self.page.goto(url)

    def wait_for_url_contains(self, fragment: str):
        self.page.wait_for_url(f"**{fragment}*")