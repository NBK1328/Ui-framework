import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # Инициализация PageObj, передаем экземпляр драйвера и урла
    page.open()  # Открытие страницы, из BasePage, наследование в MainPage
    page.go_to_login_page # Переход на страницу логина, метод MainPage



    