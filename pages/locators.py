from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TEXT_ADD_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    TITLE_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")

