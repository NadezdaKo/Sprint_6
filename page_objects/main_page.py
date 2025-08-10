import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = OrderPageLocators

    # Локаторы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    @allure.step('Нажимаем на кнопку "Заказать" вверху страницы')
    def click_order_button_top(self):
        self.click_to_element(self.locators.ORDER_BUTTON_TOP)
        return self

    @allure.step('Нажимаем на кнопку "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        self.click_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        return self

    @allure.step('Кликаем на логотип Самокат')
    def click_scooter_logo(self):
        self.click_to_element(self.SCOOTER_LOGO)
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))

    @allure.step('Кликаем на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_to_element(self.YANDEX_LOGO)
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))