import allure

from selene import browser, be


class SubmittingIelts:
    with allure.step("Отправка формы через модальное окно ' Записаться ' "):
        def fill_ielts(self):
            browser.element("//span[text()='IELTS']").click()
            browser.element('#name').set_value('John')
            browser.element('#main_phone').set_value('917177778')
            return self


submitting_ielts = SubmittingIelts()
