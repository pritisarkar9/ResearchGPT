import os
from fastapi import APIRouter, UploadFile, File
from app.services.ingestion import ingest_pdf

router = APIRouter()

UPLOAD_DIR = "data/papers"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    ingest_pdf(file_path)

    return {"status": "document indexed"}
