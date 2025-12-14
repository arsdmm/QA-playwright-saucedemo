from pages.cart_page import CartPage

def test_add_item_to_cart(inventory_page, base_url):
    cart_page = CartPage(inventory_page.page, base_url)

    inventory_page.add_first_item_to_cart()
    inventory_page.open_cart()

    assert cart_page.get_items_count() == 1, "There should be exactly one item in the cart"

