from fastapi import FastAPI
from pydantic import BaseModel

from ..rag import ask
from ..rag_engine import index, model, chunks

app = FastAPI(
    title="DefenceDocs AI"
)


class Question(BaseModel):
    question: str


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.post("/ask")
def ask_question(request: Question):

    result = ask(
        request.question,
        index,
        model,
        chunks
    )

    return result