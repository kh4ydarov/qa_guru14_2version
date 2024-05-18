import allure

from selene import browser


class SubmittingGeneral:

    def fill_modal_submitting(self):
        with allure.step("Отправка формы через модальное окно 'Записаться' "):
            browser.element('#name').set_value('John')
            browser.element('#main_phone').set_value('917177778')
        return self


submitting_general = SubmittingGeneral()
