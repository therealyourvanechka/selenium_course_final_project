from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        
    
    def should_be_product_added_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Сообщение о добавлении товара отсутствует"
        
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, \
            f"Название товара не совпадает. Ожидалось: {product_name}, получено: {message_product_name}"
    
    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Сообщение со стоимостью корзины отсутствует"
        
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price == basket_total, \
            f"Цена товара не совпадает со стоимостью корзины. Товар: {product_price}, корзина: {basket_total}"
        
    # НОВЫЕ МЕТОДЫ ДЛЯ ОТРИЦАТЕЛЬНЫХ ПРОВЕРОК
    def should_not_be_success_message(self):
        """Проверяет, что НЕТ сообщения о добавлении товара в корзину"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе присутствует, но не должно быть"
    
    def should_be_success_message_disappeared(self):
        """Проверяет, что сообщение о добавлении товара в корзину ИСЧЕЗЛО"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе не исчезло, но должно было"