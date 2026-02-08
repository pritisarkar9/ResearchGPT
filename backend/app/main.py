from fastapi import FastAPI
from app.api.routes_upload import router as upload_router
from app.api.routes_qa import router as qa_router

app = FastAPI(title="ResearchGPT")

app.include_router(upload_router, prefix="/api")
app.include_router(qa_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "running"}
