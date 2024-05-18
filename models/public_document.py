import allure

from selene import browser


class PublicDocs:
    with allure.step("Публичная оферта"):
        def public_document(self):
            browser.element('//a[contains(text(), "Публичная оферта")]').click()
            return self


public_docs = PublicDocs()