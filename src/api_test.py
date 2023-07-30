from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
from vector_store import get_answer_from_vector_store

app = FastAPI()


@app.get("/api/send/")
def example(request: Request) -> dict:
    return {"data": "okey"}

