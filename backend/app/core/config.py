from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    GROQ_API_KEY: str
    LLM_MODEL: str = "llama3-70b-8192"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    VECTOR_DB_PATH: str = "data/vector_store"

    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150
    TOP_K: int = 4

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
