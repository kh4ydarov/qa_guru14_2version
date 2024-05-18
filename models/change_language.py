import allure

from selene import browser


class ChangeLanguage:

    def change_language_english(self):
        with allure.step("Изменение языка пользователя на Английский"):
            browser.element('.style_rounded__Z8tL_').click()
            browser.element("//span[text()='English']").click()
        return self

    def change_language_russian(self):
        with allure.step("Изменение языка пользователя на Русский"):
            browser.element('.style_rounded__Z8tL_').click()
            browser.element("//span[text()='Русский']").click()
        return self

    def change_language_uzbek(self):
        with allure.step("Изменение языка пользователя на Узбекский"):
            browser.element('.style_rounded__Z8tL_').click()
            browser.element("//span[text()='O`zbek']").click()
        return self


change_language = ChangeLanguage()
