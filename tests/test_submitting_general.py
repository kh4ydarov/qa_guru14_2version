from models.open_pages import open
from models.submitting_general_english import submitting_general


def test_submitting_general_english():
    open.open_site()
    open.prices()
    submitting_general.fill_modal_submitting()
