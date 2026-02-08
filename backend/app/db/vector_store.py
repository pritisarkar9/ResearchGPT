import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.core.config import get_settings

settings = get_settings()

embedding_model = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL
)

def get_vectorstore():
    if os.path.exists(settings.VECTOR_DB_PATH):
        return FAISS.load_local(settings.VECTOR_DB_PATH, embedding_model, allow_dangerous_deserialization=True)
    return None

def save_vectorstore(docs):
    db = FAISS.from_documents(docs, embedding_model)
    db.save_local(settings.VECTOR_DB_PATH)
    return db
