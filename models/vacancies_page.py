import allure

from selene import browser


class VacanciesPage:

    def vacancies(self):
        with allure.step("Переход на страницу вакансии"):
            browser.element('//a[contains(text(), "Вакансии")]').click()
        return self


vacancies_page = VacanciesPage()
