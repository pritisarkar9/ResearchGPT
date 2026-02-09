import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_PATH = "data/vector_store"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_vectorstore():
    if os.path.exists(VECTOR_PATH):
        return FAISS.load_local(
            VECTOR_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )
    return None

def create_vectorstore(documents):
    db = FAISS.from_documents(documents, embedding_model)
    db.save_local(VECTOR_PATH)
    return db
