import allure

from selene import browser, be

class Vacancies:
    with allure.step("Заполнение формы резюме"):
        def test_fill_cv(self):