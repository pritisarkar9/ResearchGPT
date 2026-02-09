# from pydantic_settings import BaseSettings
# from functools import lru_cache

# class Settings(BaseSettings):
#     GROQ_API_KEY: str
#     LLM_MODEL: str = "llama3-70b-8192"

#     EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
#     VECTOR_DB_PATH: str = "data/vector_store"

#     CHUNK_SIZE: int = 800
#     CHUNK_OVERLAP: int = 150
#     TOP_K: int = 4

#     class Config:
#         env_file = ".env"

# @lru_cache
# def get_settings():
#     return Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )

    GROQ_API_KEY: str
    LLM_MODEL: str = "llama3-70b-8192"

@lru_cache
def get_settings():
    return Settings()

