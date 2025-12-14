from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_flow(inventory_page, base_url):
    cart_page = CartPage(inventory_page.page, base_url)
    checkout_page = CheckoutPage(inventory_page.page, base_url)
    overview_page = CheckoutOverviewPage(inventory_page.page, base_url)
    complete_page = CheckoutCompletePage(inventory_page.page, base_url)

    inventory_page.add_first_item_to_cart()
    inventory_page.open_cart()

    assert cart_page.get_items_count() == 1, "Cart should have 1 item before checkout"

    cart_page.checkout()

    checkout_page.fill_information("Dmytro", "Litvinov", "M1W2S8")
    checkout_page.continue_next()

    overview_page.finish()

    assert complete_page.is_success(), "Checkout should finish successfully"
    assert "THANK YOU" in complete_page.success_text().upper()