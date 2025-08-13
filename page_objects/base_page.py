import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import URLs


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        
    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(f'{URLs.BASE_URL}')
        
    @allure.step("Ожидание появления элемента")
    def find_element_with_wait(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Метод для ввода текста")
    def send_keys_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Метод для получения текста")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    @allure.step("Нажатие на элемент")
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()
        
    @allure.step("Метод скролла до элемента")
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))
        
    @allure.step("Ожидание загрузки сайта")
    def wait_loading_site(self, url):
        WebDriverWait(self.driver,10).until(expected_conditions.url_to_be(url))
    
    @allure.step('Скролл до конца страницы')
    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    @allure.step('Метод ожидания определенного количества открытых окон')
    def wait_numbers_of_window_to_be(self, number):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(number))
    
    @allure.step('Метод смены вкладки браузера')
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
    
    @allure.step('Метод ожидания загрузки страницы')    
    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(EC.url_contains(text))

    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url  