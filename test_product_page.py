import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()  
    page.click_button_add_to_cart()
    
    page.solve_quiz_and_get_code()
        
    page.verify_product_name_match()
    page.verify_product_price_match()
    
    



