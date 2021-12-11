import json
import allure
from allure import step
from allure_commons.types import AttachmentType as AT
from settings import config
from data.main_page_locators import MainPageLocators
from page.base_page import BasePage


class MainPage(BasePage):
    """
    Класс для работы с главной страницей 'hh.ru'
    """

    def __init__(self, driver):
        self.url = config["url"]
        BasePage.__init__(self, driver, self.url)
        self.main_locators = MainPageLocators()

    def verify_main_page(self):
        with allure.step("Главная страница hh.ru"):
            allure.attach(self.do_screenshot(), "Главная страница hh.ru", attachment_type=AT.PNG)
            assert self.check_element_visibility(self.main_locators.textbox_profession, "Поле ввода 'Профессия, должность или компания'")
            assert self.check_element_visibility(self.main_locators.button_search, "Кнопка 'Найти'")

    def close_message(self):
        with allure.step("Закрыть всплывающее сообщение о регионе"):
            self.click_button(self.main_locators.button_close_message, "Кнопка 'Закрыть' сообщение о регионе")

    def input_work(self, email):
        with step("Ввод текста в поле 'Профессия, должность или компания'"):
            self.textbox_input(self.main_locators.textbox_profession, email, "Поле ввода 'email'")
            allure.attach(json.dumps(email, ensure_ascii=False), 'Ввод текста')

    def click_search_vacancy(self):
        with step("Кликнуть по кнопке 'Найти'"):
            self.click_button(self.main_locators.button_search, "Найти")
