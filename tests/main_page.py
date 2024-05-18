import allure

from selene import browser, be

with allure.step("Отправка формы"):
    def test_main():
        browser.open('')
        browser.element('#name').set_value('John')
        browser.element('#main_phone').set_value('917177778')

with allure.step("О нас"):
    def test_about_us():
        browser.open('')
        browser.element('//a[contains(text(), "О нас")]').click()
        browser.element('.text-title').should(be.visible)


with allure.step("О нас"):
    def test_public_doc():
        browser.open('')
        browser.element('//a[contains(text(), "Публичная оферта")]').click()

with allure.step("О нас"):
    def test_changelanguage():
        browser.open('')
        browser.element('.style_rounded__Z8tL_').click()
        browser.element("//span[text()='English']").click()

