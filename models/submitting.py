import allure

from selene import browser


class Submitting:

    def fill_submitting_page(self):
        with allure.step("Отправка формы"):
            browser.element('#name').set_value('John')
            browser.element('#main_phone').set_value('917177778')
        return self


submitting = Submitting()
