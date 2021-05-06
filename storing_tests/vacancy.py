from page_objects.main_page import MainPage
from page_objects.search_vacancy_page import SearchVacancyPage
from page_objects.base_page import BasePage
from page_objects.vacancy import VacancyPage


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver

    def find_work(self):
        """
        1. Проверяем отображение элементов на главной странице 'hh.ru'
        2. Вводим текст в поле 'Профессия, должность или компания'
        3. Нажимаем кнопку 'Найти работу'
        4. Проверяем переход на страницу результата поиска
        """
        main_page = MainPage(self.driver, self.url)
        vacancy_page = SearchVacancyPage(self.driver)
        main_page.verify_main_page()
        main_page.input_work("python")
        main_page.click_find_job()
        vacancy_page.verify_search_vacancy_page()

    def open_vacancy(self):
        """
        1. Ищем вакансию по ключевому слову 'python'
        2. Переходим в первую подходящую анкету
        3. Переключаемся на новую вкладку
        4. Проверяем переход на страницу результата поиска
        """
        vacancy_page = SearchVacancyPage(self.driver)
        base_page = BasePage(self.driver)
        vacancy = VacancyPage(self.driver)
        self.find_work()
        vacancy_page.click_vacancy_one()
        base_page.switch_to_new_tab()
        vacancy.verify_vacancy_page()

