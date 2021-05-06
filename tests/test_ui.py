import allure
import pytest
from settings import config
from storing_tests.vacancy import Vacancy


@pytest.mark.ui
@allure.title("Поиск вакансий по ключевому слову 'python'")
@allure.story("Поиск вакансий по ключевому слову 'python'")
def test_find_job(driver):
    Vacancy(driver, config["url"]).find_work()


@pytest.mark.ui
@allure.title("Открыть анкету")
@allure.story("Открыть анкету")
def test_open_vacancy(driver):
    Vacancy(driver, config["url"]).open_vacancy()
