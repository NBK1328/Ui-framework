from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    # Метод __init__ вызывается при создании объекта. Конструктор ниже с ключевым словом super на самом деле только вызывает конструктор класса предка 
    # и передает ему все те аргументы, которые мы передали в конструктор MainPage. 
    def  __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
        # alert = self.browser.switch_to.alert  #Это пример, что можно добавить обработку аллертов.
        # alert.accept()

        #return LoginPage(browser=self.browser, url=self.browser.current_url) 


    

    

    



