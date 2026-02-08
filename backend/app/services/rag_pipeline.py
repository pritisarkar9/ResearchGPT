from langchain.prompts import PromptTemplate
from app.db.vector_store import get_vectorstore
from app.core.llm_provider import get_llm
from app.core.config import get_settings

settings = get_settings()

PROMPT = PromptTemplate(
    template="""
You are a research assistant.
Answer ONLY using the context below.
If answer not found say: "Not found in document".

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)

def ask_question(question: str):
    db = get_vectorstore()
    if not db:
        return {"answer": "No document uploaded", "sources": []}

    docs = db.similarity_search(question, k=settings.TOP_K)
    context = "\n\n".join([d.page_content for d in docs])

    llm = get_llm()
    response = llm.invoke(PROMPT.format(context=context, question=question))

    sources = [f"page {d.metadata.get('page', '?')}" for d in docs]

    return {
        "answer": response.content,
        "sources": sources
    }
