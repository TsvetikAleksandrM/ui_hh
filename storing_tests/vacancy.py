from settings import config
from page_objects.main_page import MainPage
from page_objects.search_vacancy_page import SearchVacancyPage
from page_objects.base_page import BasePage
from page_objects.vacancy_profile_page import VacancyProfilePage


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, driver):
        self.url = config["url"]
        self.driver = driver
        self.base_page = BasePage(self.driver)
        self.vacancy = VacancyProfilePage(self.driver)
        self.main_page = MainPage(self.driver, self.url)
        self.vacancy_page = SearchVacancyPage(self.driver)

    def interface_vacancy(self):
        """
        1. Закрыть всплывающее сообщение о регионе
        1. Проверяем отображение элементов на главной странице 'hh.ru'
        2. Вводим текст в поле 'Профессия, должность или компания'
        3. Нажимаем кнопку 'Найти работу'
        4. Проверяем отображение элементов на странице 'Результат поиска'
        """
        self.main_page.close_message()
        self.main_page.verify_main_page()
        self.main_page.input_work("python")
        self.main_page.click_search_vacancy()
        self.vacancy_page.verify_search_vacancy_page()

    def interface_vacancy_profile(self):
        """
        1. Переходим на страницу 'Результат поиска' вакансий
        2. Переходим в первую анкету
        3. Переключаемся на новую вкладку
        4. Проверяем отображение элементов на странице 'Профиль вакансии'
        """
        self.interface_vacancy()
        self.vacancy_page.click_vacancy_one()
        self.base_page.switch_to_new_tab()
        self.vacancy.verify_vacancy_profile_page()

