import json
import allure
from allure import step
from allure_commons.types import AttachmentType as AT
from data.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    """
    Класс для работы с главной страницей 'hh.ru'
    """

    def __init__(self, driver, url=None):
        BasePage.__init__(self, driver, url)
        self.main_locators = MainPageLocators()

    def verify_main_page(self):
        with allure.step("Главная страница hh.ru"):
            allure.attach(self.do_screenshot(), "Главная страница hh.ru", attachment_type=AT.PNG)
            self.check_element_visibility(self.main_locators.textbox_profession, "Поле ввода 'Профессия, должность или компания'")
            self.check_element_visibility(self.main_locators.button_find_job, "Кнопка 'Найти работу'")

    def input_work(self, email):
        with step("Ввод текста в поле 'Профессия, должность или компания'"):
            self.textbox_input(self.main_locators.textbox_profession, email, "Поле ввода 'email'")
            allure.attach(json.dumps(email, ensure_ascii=False), 'Ввод текста')

    def click_find_job(self):
        with step("Нажатие кнопки 'Найти работу'"):
            self.click_button(self.main_locators.button_find_job, "Найти работу")
