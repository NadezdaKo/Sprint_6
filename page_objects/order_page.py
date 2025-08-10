import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = OrderPageLocators

    @allure.step('Нажимаем на кнопку "Заказать" вверху страницы')
    def click_order_button_top(self):
        self.click_to_element(self.locators.ORDER_BUTTON_TOP)
        return self

    @allure.step('Нажимаем на кнопку "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        self.click_to_element(self.locators.BUTTON_COOCIE)
        self.click_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        return self

    @allure.step('Заполняем первую страницу заказа самоката')
    def fill_first_page(self, name, lastname, address, metro, phone):
        self.send_keys_to_element(self.locators.NAME_FIELD, name)
        self.send_keys_to_element(self.locators.LASTNAME_FIELD, lastname)
        self.send_keys_to_element(self.locators.ADDRESS_FIELD, address)
        self.send_keys_to_element(self.locators.METRO_FIELD, metro)
        self.click_to_element(self.locators.METRO_OPTION)
        self.send_keys_to_element(self.locators.PHONE_FIELD, phone)
        self.click_to_element(self.locators.NEXT_BUTTON)

    @allure.step('Заполняем вторую страницу заказа самоката')
    def fill_second_page(self, date, period, color, comment):
        self.send_keys_to_element(self.locators.DATE_FIELD, date)
        self.click_to_element(self.locators.DAY_FIELD)
        if color == "black":
            self.click_to_element(self.locators.COLOR_BLACK_CHECKBOX)
        elif color == "grey":
            self.click_to_element(self.locators.COLOR_GREY_CHECKBOX)
        self.click_to_element(self.locators.RENTAL_PERIOD)
        self.click_to_element(self.locators.PERIOD_OPTION)  # Исправлен выбор периода
        self.send_keys_to_element(self.locators.COMMENT_FIELD, comment)
        self.click_to_element(self.locators.ORDER_BUTTON)
        self.click_to_element(self.locators.CONFIRM_BUTTON)
    
    @allure.step('Проверка успешного заказа')    
    def is_success_visible(self):
        return self.find_element_with_wait(self.locators.SUCCESS_MODAL).is_displayed()

