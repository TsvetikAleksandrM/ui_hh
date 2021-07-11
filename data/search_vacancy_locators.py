from selenium.webdriver.common.by import By


class SearchVacancyLocators:
    """
    Локаторы страницы 'Поиск вакансий'
    """

    # Кнопка 'По соответствию'
    button_by_conformity = (By.XPATH, "//div[@data-qa='serp__settings']//option[text()='по соответствию']")
    # Кнопка 'Весь период'
    button_all_period = (By.XPATH, "//div[@data-qa='serp__settings']//option[text()='весь период']")
    # Блок вакансий
    block_vacancy = (By.CLASS_NAME, "bloko-gap bloko-gap_s-top bloko-gap_m-top bloko-gap_l-top")
    # Первая из блока вакансия
    button_vacancy_one = (By.XPATH, "(//div[@class='vacancy-serp-item'])[1]")
    # Кнопка 'Название первой из блока вакансии'
    button_name_vacancy_one = (By.XPATH, "(//div[@class='vacancy-serp-item'])[1]/descendant::span[@class='g-user-content']")
