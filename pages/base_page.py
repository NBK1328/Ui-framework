from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from .locators import LoginPageLocators

import math

class BasePage():
    
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        
        return True
    

    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    # Проверка, что какой-то элемент исчезает. Следует воспользоваться явным ожиданием вместе с функцией until_not, 
    # в зависимости от того, какой результат мы ожидаем
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except:
            return False
        
        return True
    
    
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        login_link = self.browser.find_element(By. CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_page(self):
        form_email_login = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN)
        form_email_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        assert form_email_login and form_email_register, "This is not a login page, there are no required elements"

    def go_to_basket_page(self):
        button_go_to_basket_page = self.browser.find_element(*BasePageLocators.BASKET_LINK_BUTTON)
        button_go_to_basket_page.click()


