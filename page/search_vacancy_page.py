import time

import allure
from allure_commons.types import AttachmentType as AT
from data.search_vacancy_locators import SearchVacancyLocators
from page.base_page import BasePage
from page.vacancy_profile_page import VacancyProfilePage


class SearchVacancyPage(BasePage):
    """
    Класс для работы со страницей 'Поиск вакансий'
    """

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.sv_locators = SearchVacancyLocators()
        self.vacancy = VacancyProfilePage(driver)

    def verify_search_vacancy_page(self):
        with allure.step("Проверка наличия элементов на странице 'Поиск вакансий'"):
            allure.attach(self.do_screenshot(), "Страница 'Поиск вакансий'", attachment_type=AT.PNG)
            assert self.check_element_visibility(self.sv_locators.button_by_conformity, "Кнопка 'По соответствию'")
            assert self.check_element_visibility(self.sv_locators.button_all_period, "Кнопка 'За всё время'")

    def click_vacancy_one(self):
        with allure.step("Кликнуть на первую из блока вакансию"):
            self.click_button(self.sv_locators.button_name_vacancy_one, "Первая из блока вакансия")
