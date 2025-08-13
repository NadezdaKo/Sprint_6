import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage

class TestLogoNavigation:
    @allure.title("Переход на главную страницу по логотипу Самоката")
    def test_scooter_logo_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button_top()  # Переход на страницу заказа
        main_page.click_scooter_logo()
        assert main_page.get_current_url(), "Не произошел переход на главную страницу Самоката"

    @allure.title("Переход на Дзен по логотипу Яндекса")
    def test_yandex_logo_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        assert main_page.get_current_url(), "Не произошел переход на главную страницу Дзена"