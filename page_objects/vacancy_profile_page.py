import allure
from allure_commons.types import AttachmentType as AT
from data.profile_vacancy_locators import VacancyProfileLocators
from page_objects.base_page import BasePage


class VacancyProfilePage(BasePage):
    """
    Класс для работы со страницей 'Профиль вакансии'
    """

    def __init__(self, driver, url=None):
        BasePage.__init__(self, driver, url)
        self.vacancy_locators = VacancyProfileLocators()

    def verify_vacancy_profile_page(self):
        with allure.step("Проверка отображения элементов на странице 'Профиль вакансии'"):
            allure.attach(self.do_screenshot(), "Страница 'Профиль вакансии'", attachment_type=AT.PNG)
            assert self.check_element_visibility(self.vacancy_locators.button_filters, "Кнопка 'Откликнуться'")
            assert self.check_element_visibility(self.vacancy_locators.button_by_conformity, "Кнопка 'Звёздочка'")

