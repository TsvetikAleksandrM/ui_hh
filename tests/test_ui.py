import allure
import pytest
from storing_tests.vacancy import Vacancy


@pytest.mark.ui
@allure.title("Отображение интерфейса на странице 'Вакансии'")
@allure.story("Отображение интерфейса на странице 'Вакансии'")
def test_interface_vacancy(driver):
    Vacancy(driver).interface_vacancy()


@pytest.mark.ui
@allure.title("Отображение интерфейса на странице 'Профиль вакансии'")
@allure.story("Отображение интерфейса на странице 'Профиль вакансии'")
def test_interface_vacancy_profile(driver):
    Vacancy(driver).interface_vacancy_profile()
