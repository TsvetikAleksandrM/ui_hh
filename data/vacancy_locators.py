from selenium.webdriver.common.by import By


class VacancyLocators:
    """
    Локаторы страницы 'Вакансия'
    """
    # Кнопка 'Откликнуться'
    button_filters = (By.XPATH, "//div[@class='vacancy-action vacancy-action_stretched']")
    # Кнопка 'Звёздочка'
    button_by_conformity = (By.XPATH, "//button[@class='bloko-button bloko-button_minor bloko-button_icon-only']")
