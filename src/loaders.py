from langchain.document_loaders.pdf import PyPDFLoader


def get_document(_path: str = "../files/example.pdf") -> list[str]:
    """Get the document data from the PyPDFLoader."""

    document: list[str] = PyPDFLoader(_path).load()

    return document


def get_document_contents(document: list[str]) -> str:
    """Get the contents of the document."""


    document_contents: str = document[0].page_content

    return document_contents
