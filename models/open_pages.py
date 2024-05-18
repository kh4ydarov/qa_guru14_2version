import allure

from selene import browser, be, command


class OpenPage:
    with allure.step("Открывается сайт"):
        def open_site(self):
            browser.open("")
            return self


    with allure.step("Переход на страницу авторизации"):
        def auth(self):
            browser.element("//*[@id='__next']/div[2]/nav/div/div[3]/div/a[1]").click()
            return self

    with allure.step("Переход на страницу О нас"):
        def about_us(self):
            browser.element('//a[contains(text(), "О нас")]').click()
            browser.element('.text-title').should(be.visible)
            return self

    with allure.step("Переход на страницу О комманде"):
        def teachers(self):
            browser.element('//a[contains(text(), "Команда")]').click()
            browser.element('.style_wrapper__N8x_i').should(be.visible)
            return self

    with allure.step("Переход на страницу Цена"):
        def prices(self):
            browser.element('//a[contains(text(), "Цены")]').click()
            browser.element('.style_content___t0BC').should(be.visible)
            return self

    with allure.step("Переход на страницу Галерея"):
        def gallery(self):
            browser.element('//a[contains(text(), "Галерея")]').click()
            browser.element('.style_textSide__fwkMw h2.text-title').should(be.visible)
            return self

    with allure.step("Публичная оферта"):
        def public_document(self):
            browser.element('//a[contains(text(), "Публичная оферта")]').click()
            return self

    with allure.step("Переход на страницу вакансии"):
        def vacancies(self):
            browser.element('//a[contains(text(), "Вакансии")]').click()
            return self

    with allure.step("Открываем модальное окно записаться"):
        def modal_submitting(self):
            browser.element('.style_btn__b5YdX').perform(command.js.scroll_into_view).click()
            return self

open = OpenPage()