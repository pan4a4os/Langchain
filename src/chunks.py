from langchain.text_splitter import RecursiveCharacterTextSplitter
from loaders import get_document, get_document_contents
from tokenizer import tiktoken_length


def set_splitter(_chunk_size: int = 1000, _chunk_overlap: int = 10) -> RecursiveCharacterTextSplitter:
    """Splitting the content into chunks using RecursiveCharacterTextSplitter."""

    splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
        chunk_size=_chunk_size,
        chunk_overlap=_chunk_overlap,
        length_function=tiktoken_length,
        separators=["\n\n", "\n", " ", ""]
    )

    return splitter


def get_chunks() -> list[str]:
    """Get chunks from document contents."""

    _document: list[str] = get_document()
    _document_contents: str = get_document_contents(document=_document)

    splitter: RecursiveCharacterTextSplitter = set_splitter()
    chunks: list[str] = splitter.split_text(_document_contents)

    return chunks
