import allure

from selene import browser, be, command


class OpenPage:

    def open_site(self):
        with allure.step("Открывается сайт"):
            browser.open("")
        return self

    def auth(self):
        with allure.step("Переход на страницу авторизации"):
            browser.element("//*[@id='__next']/div[2]/nav/div/div[3]/div/a[1]").click()
        return self

    def about_us(self):
        with allure.step("Переход на страницу О нас"):
            browser.element('//a[contains(text(), "О нас")]').click()
            browser.element('.text-title').should(be.visible)
        return self

    def teachers(self):
        with allure.step("Переход на страницу О комманде"):
            browser.element('//a[contains(text(), "Команда")]').click()
            browser.element('.style_wrapper__N8x_i').should(be.visible)
        return self

    def prices(self):
        with allure.step("Переход на страницу Цена"):
            browser.element('//a[contains(text(), "Цены")]').click()
            browser.element('.style_content___t0BC').should(be.visible)
        return self

    def gallery(self):
        with allure.step("Переход на страницу Галерея"):
            browser.element('//a[contains(text(), "Галерея")]').click()
            browser.element('.style_textSide__fwkMw h2.text-title').should(be.visible)
        return self

    def modal_submitting(self):
        with allure.step("Открываем модальное окно записаться"):
            browser.element('.style_btn__b5YdX').perform(command.js.scroll_into_view).click()
        return self


open = OpenPage()
