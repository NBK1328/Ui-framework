import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # Инициализация PageObj, передаем экземпляр драйвера и урла
    page.open()  # Открытие страницы, из BasePage, наследование в MainPage
    page.go_to_login_page() # Переход на страницу логина, метод MainPage
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page  # Один из подходов который происходит неявно, инициализация происходит в теле теста.
    
    # login_page = page.go_to_login_page()  # Один из подходов инициализации страницы при переходе между страницами. 
    # login_page.should_be_login_page()     # Файл main_page.py строка с return часть этой инициализации.
    
    # Проверка страницы login в теле теста проверки страницы main - неправильно. Но для прохождения курса,
    # буду следовать этой логики. Лучше все проверки разделять и не допускать совмещения.


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.checking_an_empty_cart()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.checking_an_empty_cart()

         
    
    
    
    






    



