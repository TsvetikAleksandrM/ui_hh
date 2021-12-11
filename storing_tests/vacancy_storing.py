from page.base_page import BasePage
from page.main_page import MainPage
from page.search_vacancy_page import SearchVacancyPage


class VacancyStoring:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, driver):

        self.driver = driver
        self.base_page = BasePage(self.driver)
        self.main_page = MainPage(self.driver)
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

