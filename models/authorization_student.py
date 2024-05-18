import allure

from selene import browser


class AuthorizationStudent:
    with allure.step("Авторизация по некорректным данным"):
        def authorization_student(self):
            browser.element('#role1').click().press_enter()
            browser.element('#iuytqwiqrtuwy1').set_value('910101234')
            browser.element('#kjbsldbdfjklsa2').set_value('1234567')
            browser.element('.MuiButton-containedPrimary').click()
            return self


student_authorization = AuthorizationStudent()
