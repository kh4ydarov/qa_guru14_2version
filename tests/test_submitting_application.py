from models.open_pages import open
from models.submitting import submitting

def test_submitting_application():
    open.open_site()
    submitting.fill_submitting_page()