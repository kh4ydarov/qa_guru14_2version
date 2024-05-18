from models.open_pages import open
from models.change_language import change_language

def test_change_language():
    open.open_site()
    change_language.change_language_uzbek()
    change_language.change_language_english()
    change_language.change_language_russian()