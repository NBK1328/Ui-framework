import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # Инициализация PageObj, передаем экземпляр драйвера и урла
    page.open()  # Открытие страницы, из BasePage, наследование в MainPage
    page.go_to_login_page # Переход на страницу логина, метод MainPage
    time.sleep(10)
    

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

    



