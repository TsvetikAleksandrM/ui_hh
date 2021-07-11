from selenium.webdriver.common.by import By


class VacancyProfileLocators:
    """
    Локаторы страницы 'Профиль вакансии'
    """

    # Кнопка 'Откликнуться'
    button_filters = (By.CLASS_NAME, "vacancy-action vacancy-action_stretched")
    # Кнопка 'Звёздочка'
    button_by_conformity = (By.CLASS_NAME, "bloko-button bloko-button_minor bloko-button_icon-only")
