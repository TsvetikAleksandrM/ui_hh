from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Локаторы главной страницы 'hh.ru'
    """

    # Кнопка 'Закрыть' сообщение о регионе
    button_close_message = (By.XPATH, "//div[@class='Bloko-Notification-Close bloko-notification__close']/span")
    # Поле ввода 'Профессия, должность или компания'
    textbox_profession = (By.XPATH, "//input[@placeholder='Профессия, должность или компания']")
    # Кнопка 'Найти'
    button_search = (By.XPATH, "//span[text()='Найти работу']")
