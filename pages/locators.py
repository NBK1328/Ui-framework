from selenium.webdriver.common.by import By


class LoginPageLocators():

    LOGIN_FORM = (By.NAME, "login-username")
    PASSWORD_FORM = (By.NAME, "login-password")
    BUTTON_LOGIN = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_FORM = (By.NAME, "registration-password1")
    REPEAT_REGISTRATION_PASSWORD_FORM = (By.NAME, "registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")

class ProductPageLocators():
    button_add_to_cart = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    product_name = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    price = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    message_name_product = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    message_price_product = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')


class BasketPageLocators():
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")



