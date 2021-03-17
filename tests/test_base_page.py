from pages.base_page import BasePage


def test_base_page(browser):
    bp = BasePage(browser)
    bp.open_base_page()
