from page.base_page import BasePage
from page.vacancy_profile_page import VacancyProfilePage
from page.search_vacancy_page import SearchVacancyPage
from storing_tests.vacancy_storing import VacancyStoring


class VacancyProfileStoring:
    """
    Класс для работы с профилем вакансий
    """

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)
        self.vacancy_profile_page = VacancyProfilePage(self.driver)
        self.vacancy_page = SearchVacancyPage(self.driver)
        self.vacancy_storing = VacancyStoring(self.driver)

    def interface_vacancy_profile(self):
        """
        1. Переходим на страницу 'Результат поиска' вакансий
        2. Переходим в первую анкету
        3. Переключаемся на новую вкладку
        4. Проверяем отображение элементов на странице 'Профиль вакансии'
        """
        self.vacancy_storing.interface_vacancy()
        self.vacancy_page.click_vacancy_one()
        self.base_page.switch_to_new_tab()
        self.vacancy_profile_page.verify_vacancy_profile_page()
