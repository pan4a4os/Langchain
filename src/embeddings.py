import os

from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings


def set_embeddings(_model: str = "gpt-3.5-turbo", _chunk_size: int = 1000, _max_retries: int = 10) -> OpenAIEmbeddings:
    """Set the OpenAIEmbeddings embedding model."""

    load_dotenv()
    embeddings: OpenAIEmbeddings = OpenAIEmbeddings(
        openai_api_key=os.environ["OPENAI_API_KEY"], model=_model, chunk_size=_chunk_size, max_retries=_max_retries
    )

    return embeddings


def get_embeddings_documents(embeddings: OpenAIEmbeddings, chunks: list[str]) -> list[float]:
    """Get embedding documents from chunks."""

    embeddings_documents: list[float] = embeddings.embed_documents(chunks)

    return embeddings_documents
