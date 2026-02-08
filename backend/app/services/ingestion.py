from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.db.vector_store import save_vectorstore
from app.core.config import get_settings

settings = get_settings()

def ingest_pdf(path: str):
    loader = PyPDFLoader(path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )

    docs = splitter.split_documents(documents)
    return save_vectorstore(docs)
