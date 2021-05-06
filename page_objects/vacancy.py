import allure
from allure_commons.types import AttachmentType as AT
from data.vacancy_locators import VacancyLocators
from page_objects.base_page import BasePage


class VacancyPage(BasePage):
    """
    Класс для работы со страницей 'Вакансия'
    """

    def __init__(self, driver, url=None):
        BasePage.__init__(self, driver, url)
        self.vacancy_locators = VacancyLocators()

    def verify_vacancy_page(self):
        with allure.step("Проверка наличия элементов на странице 'Поиск вакансий'"):
            allure.attach(self.do_screenshot(), "Страница 'Поиск вакансий'", attachment_type=AT.PNG)
            assert self.check_element_visibility(self.vacancy_locators.button_filters, "Кнопка 'Откликнуться'")
            assert self.check_element_visibility(self.vacancy_locators.button_by_conformity, "Кнопка 'Звёздочка'")

