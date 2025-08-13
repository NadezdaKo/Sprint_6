import pytest
import allure
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


class TestOrderFlow:
    @pytest.mark.parametrize("name, lastname, address, metro, phone, date, period, color, comment", [
        (
            "Надежда",
            "Комиссарова",
            "ул Краснознаменская, 24",
            "Щёлковская",
            "+79273444796",
            "06.08.2025",
            "двое суток",
            "grey",
            "Позвонить за час"
        ),
        (
            "Макар",
            "Пушкин",
            "ул. Мира, 56",
            "Чистые пруды",
            "+79095555892",
            "22.11.2024",
            "трое",
            "black",
            "Оставить у двери"
        ),
    ])
    @allure.title("Заказ самоката через верхнюю кнопку 'Заказать'")
    def test_order_flow_top_button(self, driver, name, lastname, address, metro, phone, date, period, color, comment):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_order_button_top()
        order_page.fill_first_page(name, lastname, address, metro, phone)
        order_page.fill_second_page(date, period, color, comment)
        assert order_page.is_success_visible()
    
    @pytest.mark.parametrize("name, lastname, address, metro, phone, date, period, color, comment", [
        (
            "Надежда",
            "Комиссарова",
            "ул Краснознаменская, 24",
            "Щёлковская",
            "+79273444796",
            "06.08.2025",
            "двое суток",
            "grey",
            "Позвонить за час"
        ),
        (
            "Макар",
            "Пушкин",
            "ул. Мира, 56",
            "Чистые пруды",
            "+79095555892",
            "22.11.2024",
            "сутки",
            "black",
            "Оставить у двери"
        ),
    ])  
    @allure.title("Заказ самоката через нижнюю кнопку 'Заказать'")
    def test_order_flow_bottom_button(self, driver, name, lastname, address, metro, phone, date, period, color, comment):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_order_button_bottom()
        order_page.fill_first_page(name, lastname, address, metro, phone)
        order_page.fill_second_page(date, period, color, comment)
        assert order_page.is_success_visible()