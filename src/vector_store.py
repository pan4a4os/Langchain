import os
import typing

from chunks import get_chunks
from embeddings import set_embeddings, get_embeddings_documents
from langchain.vectorstores import Chroma
from loaders import get_document


def set_vector_store(document: list[float], embeddings: "OpenAIEmbeddings") -> Chroma:
    """Setting Chrome's vector database for future reference."""

    chroma_db: Chroma = Chroma.from_documents(document, embeddings)

    return chroma_db


def get_answer_from_vector_store(query: str) -> str or None:
    """Get matches from Chroma vector database by human request."""


    _chunks: list[str] = get_chunks()
    _embeddings: OpenAIEmbeddings = set_embeddings()
    _embeddings_documents: list[float] = get_embeddings_documents(embeddings=_embeddings, chunks=_chunks)
    _chroma_db: Chroma = set_vector_store(document=_embeddings_documents, embeddings=_embeddings)

    _search_results: list[str] = _chroma_db.similarity_search(query=query)
    result: str or None = _search_results[0].page_content

    return result

