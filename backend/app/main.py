from fastapi import FastAPI
from app.api.routes_llm import router as llm_router
from app.api.routes_upload import router as upload_router
from app.api.routes_rag import router as rag_router

app = FastAPI(title="ResearchGPT")

app.include_router(llm_router, prefix="/api")
app.include_router(upload_router, prefix="/api")
app.include_router(rag_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "running"}
