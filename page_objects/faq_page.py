from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_page_locators import FaqPageLocators
from page_objects.base_page import BasePage

class FaqPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = FaqPageLocators

    def click_question(self, index):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.QUESTIONS[index])
        )
        self.driver.execute_script("arguments[0].click();", element)

    def is_answer_visible(self, index):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ANSWERS[index])
        ).is_displayed()
    
    def get_answer_text(self, index):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ANSWERS[index])
        ).text