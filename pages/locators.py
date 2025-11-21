from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")