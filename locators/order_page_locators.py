from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локаторы формы заказа
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_OPTION = (By.XPATH, "//li[@class='select-search__row']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы второй страницы заказа
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DAY_FIELD = (By.CLASS_NAME, "react-datepicker__day--selected")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    PERIOD_OPTION = (By.CSS_SELECTOR, 'div.Dropdown-option:nth-child(2)')
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    
    BUTTON_COOCIE = (By.XPATH, "//button[text()='да все привыкли']")