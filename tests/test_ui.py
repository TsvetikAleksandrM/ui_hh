import allure
import pytest
from storing_tests.vacancy_storing import VacancyStoring
from storing_tests.vacancy_profile_storing import VacancyProfileStoring


@pytest.mark.ui
@allure.story('Проверка интерфейса')
class TestDoRegisterPassword:

    @allure.title("Проверка интерфейса страницы 'Вакансии'")
    def test_interface_vacancy(self, driver):
        VacancyStoring(driver).interface_vacancy()

    @allure.title("Проверка интерфейса страницы 'Профиль вакансии'")
    def test_interface_vacancy_profile(self, driver):
        VacancyProfileStoring(driver).interface_vacancy_profile()
