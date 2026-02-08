from fastapi import APIRouter
from app.schemas.qa_schema import QuestionRequest
from app.services.rag_pipeline import ask_question

router = APIRouter()

@router.post("/ask")
def ask(req: QuestionRequest):
    return ask_question(req.question)
