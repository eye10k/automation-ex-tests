import pytest

from pages.home_page import HomePage

def test_add_to_cart(page):
    home_page = HomePage(page)
    home_page.navigate_to_home()

    home_page.add_product_to_cart()
    home_page.go_to_cart()

    assert page.url == "https://automationexercise.com/view_cart", "Страница корзины не открыта"