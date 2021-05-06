import allure
from allure_commons.types import AttachmentType as AT
from data.search_vacancy_locators import SearchVacancyLocators
from page_objects.base_page import BasePage
from page_objects.vacancy import VacancyPage


class SearchVacancyPage(BasePage):
    """
    Класс для работы со страницей 'Поиск вакансий'
    """

    def __init__(self, driver, url=None):
        BasePage.__init__(self, driver, url)
        self.sv_locators = SearchVacancyLocators()
        self.vacancy = VacancyPage(driver)

    def verify_search_vacancy_page(self):
        with allure.step("Проверка наличия элементов на странице 'Поиск вакансий'"):
            allure.attach(self.do_screenshot(), "Страница 'Поиск вакансий'", attachment_type=AT.PNG)
            assert self.check_element_visibility(self.sv_locators.button_by_conformity, "Кнопка 'По соответствию'")
            assert self.check_element_visibility(self.sv_locators.button_all_period, "Кнопка 'Весь период'")
            assert self.check_element_visibility(self.sv_locators.block_vacancy, "Блок вакансий")

    def click_vacancy_one(self):
        with allure.step("Кликнуть на первую подходящую из блока вакансию"):
            self.click_button(self.sv_locators.button_name_vacancy_one, "Первая из блока вакансия")

