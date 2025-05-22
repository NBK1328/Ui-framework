from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        check_current_url = True if "/login/" in current_url else False
        assert check_current_url, "Url page different from login url"
        

    def should_be_login_form(self):      
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not found"

    
    
    
    
    # Если нужны избыточные проверки.
    
    # def should_be_login_url(self):
    #     assert "login" in self.browser.current_url, "Url page different from login url"
    
    
    # def should_be_login_form(self):
    #     assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    # def should_be_password_form(self):
    #     assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM, "Password form is not found")

    # def should_be_login_buttom(self):
    #     assert self.is_element_present(*LoginPageLocators.BUTTON_LOGIN), "Button login is not found"

    # def should_be_registration_form(self):
    #     assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not found"
    
    # def should_be_registration_password_form(self):
    #     assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FORM), "Registration password form is not found"

    # def should_be_registration_button(self):
    #     assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTRATION), "Button registration is not found"
