import allure

from selene import browser, be


class Submitting:
    with allure.step("Отправка формы"):
        def fill_submitting_page(self):
            browser.element('#name').set_value('John')
            browser.element('#main_phone').set_value('917177778')
            return self

submitting = Submitting()
