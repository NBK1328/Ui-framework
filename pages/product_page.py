import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
 

class ProductPage(BasePage):

    def click_button_add_to_cart(self):
        
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.button_add_to_cart)
        button_add_to_cart.click()

    def find_name_product(self):
        self.browser.find_element(*ProductPageLocators.product_name)

    def find_price_product(self):
        self.browser.find_element(*ProductPageLocators.price)
    
    def verify_product_name_match(self):
        element_actual_name_product = self.browser.find_element(*ProductPageLocators.message_name_product)
        actual_name_product = element_actual_name_product.text
        element_expected_name_product = self.browser.find_element(*ProductPageLocators.product_name)
        expected_name_product = element_expected_name_product.text

        assert actual_name_product == expected_name_product, "Actual name does not match the expected name"

    def verify_product_price_match(self):
        element_actual_price = self.browser.find_element(*ProductPageLocators.message_price_product)
        actual_price = element_actual_price.text
        element_expected_price = self.browser.find_element(*ProductPageLocators.price)
        expected_price = element_expected_price.text
        assert actual_price == expected_price, "Actual price does not match the expected price"

    


