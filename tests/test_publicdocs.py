from models.open_pages import open
from models.public_document import public_docs


def test_publicdocs():
    open.open_site()
    public_docs.public_document()
