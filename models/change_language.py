import allure

from selene import browser, be


class ChangeLanguage:
    with allure.step("Изменение языка пользователя на Английский"):
        def change_language_english(self):
            browser.element('.style_rounded__Z8tL_').click()
            browser.element("//span[text()='English']").click()
            return self

    with allure.step("Изменение языка пользователя на Русский"):
        def change_language_russian(self):
            browser.element('.style_rounded__Z8tL_').click()
            browser.element("//span[text()='Русский']").click()
            return self

    with allure.step("Изменение языка пользователя на Узбекский"):
        def change_language_uzbek(self):
            browser.element('.style_rounded__Z8tL_').click()
            browser.element("//span[text()='O`zbek']").click()
            return self


change_language = ChangeLanguage()
