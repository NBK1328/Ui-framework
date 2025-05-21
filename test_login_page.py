import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time


def test_guest_be_on_the_login_page(browser):

    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    
    page.should_be_login_page
    
    
