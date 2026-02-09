import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.db.vector_store import create_vectorstore

UPLOAD_DIR = "data/papers"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def ingest_pdf(path: str):
    loader = PyPDFLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    split_docs = splitter.split_documents(docs)

    return create_vectorstore(split_docs)
