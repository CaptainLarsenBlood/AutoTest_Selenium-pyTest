from itertools import tee
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()
    
    def add_basket_check_title(self):
        text = self.browser.find_elements(*ProductPageLocators.TEXT_ADD_BASKET)
        title_product = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT)
        #print(text[0].text, "\n", title_product.text)
        assert text[0].text == title_product.text, "Добавлен не тот товар"
    
    def add_basket_check_price(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_MESSAGE)
        #print(price1.text, "\n", price2.text)
        assert price1.text == price2.text, "Цены не совпадают"

  
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_ADD_BASKET), \
        "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.TEXT_ADD_BASKET), \
            "Not disappeared"
