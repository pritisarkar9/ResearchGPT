from fastapi import APIRouter
from pydantic import BaseModel
from app.core.groq_client import get_llm

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/ask-llm")
def ask_llm(q: Question):
    llm = get_llm()
    response = llm.invoke(q.question)

    return {
        "question": q.question,
        "answer": response.content
    }
