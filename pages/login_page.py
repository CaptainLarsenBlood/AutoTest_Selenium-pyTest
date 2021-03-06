from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "No correct url"
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Form Login is not presented"
  

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Form registration is not presented"
        