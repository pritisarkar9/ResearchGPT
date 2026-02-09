from app.db.vector_store import get_vectorstore
from app.core.groq_client import get_llm
from langchain_core.prompts import PromptTemplate

PROMPT = PromptTemplate(
    template="""
Answer ONLY from the provided context.
If answer not found say: Not found in document.

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)

def ask_document(question: str):
    db = get_vectorstore()

    if not db:
        return {"answer": "No document uploaded", "sources": []}

    docs = db.similarity_search(question, k=4)

    context = "\n\n".join([d.page_content for d in docs])

    llm = get_llm()
    response = llm.invoke(PROMPT.format(context=context, question=question))

    sources = [f"page {d.metadata.get('page', '?')}" for d in docs]

    return {"answer": response.content, "sources": sources}
