from models.open_pages import open
from models.vacancies_page import vacancies_page


def test_vacancies():
    open.open_site()
    vacancies_page.vacancies()
