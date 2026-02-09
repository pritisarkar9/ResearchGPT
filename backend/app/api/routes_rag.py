from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_pipeline import ask_document

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/ask-doc")
def ask_doc(q: Question):
    return ask_document(q.question)
