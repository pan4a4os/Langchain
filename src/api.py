from fastapi import FastAPI
from vector_store import get_answer_from_vector_store
from pydantic import BaseModel
from typing import Union


app = FastAPI()


class Item(BaseModel):
    """Declare data model as a class that inherits from BaseModel."""

    answer: Union[str, None] = None


@app.post("/api/send/{query}")
def answer(query: str) -> dict:
    result: str or None = get_answer_from_vector_store(query=query)
    if result is None:
        result: str = "I don't know please contact with support by email support@nifty-bridge.com"

    response: dict[str: str] = {"answer": result}

    return response

