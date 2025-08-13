import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_page_locators import FaqPageLocators
from page_objects.base_page import BasePage

class FaqPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = FaqPageLocators

    @allure.step('Метод клика на вопрос')
    def click_question(self, index):
        self.scroll_to_end()
        self.click_to_element(self.locators.QUESTIONS[index])

    @allure.step('Метод вывода ответа на вопрос')
    def is_answer_visible(self, index):
        return self.find_element_with_wait(self.locators.ANSWERS[index]).is_displayed()
    
    @allure.step('Метод вывода текста ответа')
    def get_answer_text(self, index):
        return self.find_element_with_wait(self.locators.ANSWERS[index]).text    
    