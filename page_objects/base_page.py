from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings.logger import logger


class BasePage(object):
    """
    Базовый класс
    """

    def __init__(self, driver, url=None):
        self.driver = driver
        self.timeout = 10
        self.driver.maximize_window()
        if url:
            self.open(url)

    def open(self, url):
        """
        Проверяем загрузку главной страницы hh.ru
        :param url: url ресурса
        :return:
        """
        logger.info(f"Open URL: {url}")
        self.driver.get(url)
        assert self.driver.find_elements_by_xpath(
            "//input[contains(@class,'bloko-input HH-Supernova')]").__len__() == 1, f"Страница {url} не открылась."

    def check_element_visibility(self, locator, text):
        """
        Ожидание проверки элемента на видимость
        :param locator: локатор
        :param text: название элемента
        :return: элемент
        """
        logger.info(f" The page displays: {text}")
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def check_element_clickable(self, locator, text):
        """
        Ожидание проверки на видимость и кликабельность элемента
        :param locator: локатор
        :param text: название элемента
        :return: элемент
        """
        logger.info(f" The page displays: {text}")
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def click_button(self, locator, button_text):
        """
        Кликнуть по кнопке
        :param locator: локатор
        :param button_text: кнопка для клика
        :return:
        """
        element = self.check_element_clickable(locator, button_text)
        logger.info(f"Click Button: {button_text}")
        element.click()

    def click_button_visibility(self, locator, button_text):
        """
        Кликнуть по кнопке
        :param locator: локатор
        :param button_text: кнопка для клика
        :return:
        """
        element = self.check_element_visibility(locator, button_text)
        logger.info(f"Click Button {button_text}")
        element.click()

    def textbox_input(self, locator, value, textbox_text):
        """
        Вводим данные в поле ввода
        :param locator: локатор
        :param value: значение для ввода
        :param textbox_text: поле для ввода
        :return:
        """
        textbox = self.check_element_clickable(locator, textbox_text)
        logger.info(f"Click textbox: {textbox_text} and enter value {value}")
        textbox.click()
        textbox.clear()
        textbox.send_keys(value)

    def do_screenshot(self):
        """
        Делаем скриншот страницы
        :return: скриншот
        """
        img = self.driver.get_screenshot_as_png()
        return img

    def switch_to_new_tab(self):
        """
        Переключиться на новую вкладку
        :return:
        """
        logger.info(f"Switch to new tab")
        self.driver.switch_to.window(self.driver.window_handles[-1])


