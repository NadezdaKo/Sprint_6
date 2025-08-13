import pytest
import allure
from page_objects.faq_page import FaqPage
from urls import URLs
from locators.faq_page_locators import FaqPageLocators 
from test_data import FAQ_TEST_DATA

class TestFaq:
    @allure.title('Тест-что ответы на вопросы верены')
    @allure.description('Тест-что ответы на восемь вопросов верены')
    @pytest.mark.parametrize("question_index, expected_answer", FAQ_TEST_DATA)
    def test_faq_answers(self, driver, question_index, expected_answer):

        # Инициализируем страницу FAQ
        faq_page = FaqPage(driver)
        
        faq_page.open()

        # Кликаем на вопрос и проверяем ответ
        faq_page.click_question(question_index)
        assert faq_page.is_answer_visible(question_index), f"Ответ на вопрос {question_index+1} не отобразился"
        assert expected_answer in faq_page.get_answer_text(question_index), "Текст ответа не совпадает"