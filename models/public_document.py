import allure

from selene import browser


class PublicDocs:

    def public_document(self):
        with allure.step("Публичная оферта"):
            browser.element('//a[contains(text(), "Публичная оферта")]').click()
        return self


public_docs = PublicDocs()