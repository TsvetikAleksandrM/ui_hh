from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Локаторы главной страницы 'hh.ru'
    """
    # Кнопка 'Найти работу'
    button_find_job = (By.CLASS_NAME, "supernova-search-submit-text")
    # Поле ввода 'Профессия, должность или компания'
    textbox_profession = (By.XPATH, "//input[contains(@class,'bloko-input HH-Supernova')]")
