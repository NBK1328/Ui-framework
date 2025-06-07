import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def checking_an_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "The cart contains items"

        
