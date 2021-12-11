from selenium.webdriver.common.by import By


class SearchVacancyLocators:
    """
    Локаторы страницы 'Поиск вакансий'
    """

    # Кнопка 'По соответствию'
    button_by_conformity = (By.XPATH, "//div[text()='По соответствию']")
    # Кнопка 'За всё время'
    button_all_period = (By.XPATH, "(//div[@class='bloko-custom-select__placeholder'])[2]")
    # Блок вакансий
    block_vacancy = (By.CLASS_NAME, "bloko-column bloko-column_xs-4 bloko-column_s-8 bloko-column_m-9 bloko-column_l-13")
    # Первая из блока вакансия
    button_vacancy_one = (By.XPATH, "(//div[@class='vacancy-serp-item vacancy-serp-item_premium'])[1]")
    # Кнопка 'Название первой из блока вакансии'
    button_name_vacancy_one = (By.XPATH, "(//div[@class='vacancy-serp-item vacancy-serp-item_premium'])[1]/descendant::span[@class='g-user-content']")
