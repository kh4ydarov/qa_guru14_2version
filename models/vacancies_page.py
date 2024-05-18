import allure

from selene import browser, be, command


class VacanciesPage:
    with allure.step("Переход на страницу вакансии"):
        def vacancies(self):
            browser.element('//a[contains(text(), "Вакансии")]').click()
            return self


vacancies_page = VacanciesPage()
