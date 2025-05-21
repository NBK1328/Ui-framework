from selenium.webdriver.common.by import By

class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():

    LOGIN_FORM = (By.NAME, "login-username")
    PASSWORD_FORM = (By.NAME, "login-password")
    BUTTON_LOGIN = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_FORM = (By.NAME, "registration-password1")
    REPEAT_REGISTRATION_PASSWORD_FORM = (By.NAME, "registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")