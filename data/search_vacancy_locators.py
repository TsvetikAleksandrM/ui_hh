from selenium.webdriver.common.by import By


class SearchVacancyLocators:
    """
    Локаторы страницы 'Поиск вакансий'
    """
    # Кнопка 'По соответствию'
    button_by_conformity = (By.XPATH, "//div[2]/div[1]/select")
    # Кнопка 'Весь период'
    button_all_period = (By.XPATH, "//div[2]/div[2]/select")
    # Блок вакансий
    block_vacancy = (By.XPATH, "//div[contains(@class,'bloko-gap bloko-gap_s-top')]")
    # Первая из блока вакансия
    button_vacancy_one = (By.XPATH, "//div[@class='vacancy-serp-item'][1]")
    # Кнопка 'Название первой из блока вакансии'
    button_name_vacancy_one = (By.XPATH, "//div[@class='vacancy-serp-item'][1]/descendant::span[@class='g-user-content']")
