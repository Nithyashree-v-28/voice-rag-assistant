from fastapi import FastAPI
from pydantic import BaseModel
from src.rag_pipeline import ask_question

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Voice RAG Assistant API is running!"}


@app.post("/ask")
def ask(request: QuestionRequest):
    answer = ask_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }