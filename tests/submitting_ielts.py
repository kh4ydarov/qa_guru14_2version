from models.open_pages import open
from models.submitting_ielts_groups import submitting_ielts

def test_submitting_application():
    open.open_site()
    open.prices()
    submitting_ielts.fill_ielts()
