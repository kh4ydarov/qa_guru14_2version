from models.open_pages import open
from models.authorization_student import student_authorization


def test_authorization():
    open.open_site()
    open.auth()
    student_authorization.authorization_student()
