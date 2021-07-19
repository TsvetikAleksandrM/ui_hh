from selenium.webdriver.common.by import By


class VacancyProfileLocators:
    """
    Локаторы страницы 'Профиль вакансии'
    """

    # Кнопка 'Откликнуться'
    button_filters = (By.XPATH, "//a[contains(@class,'bloko-button bloko-button_secon')]/span[text()='Откликнуться']")
    # Кнопка 'Звёздочка'
    button_by_conformity = (By.CLASS_NAME, "bloko-button__icon")
