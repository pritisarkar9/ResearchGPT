# ResearchGPT — Question Answering over Research Papers (RAG + Llama3)

ResearchGPT is a full-stack Generative AI application that allows users to upload research papers (PDF) and ask natural-language questions.  
The system retrieves the most relevant passages using vector search and generates grounded answers using Llama3 via Groq.

Unlike a normal chatbot, this system uses **Retrieval Augmented Generation (RAG)** to prevent hallucinations and provide answers strictly from the document.

---

## Problem Statement

Large Language Models often hallucinate when answering domain-specific questions because they rely only on training data.

ResearchGPT solves this by:

1. Converting research papers into embeddings
2. Retrieving relevant sections at query time
3. Forcing the model to answer using only retrieved context

This makes responses reliable and explainable.

---

## Demo Workflow

Upload Paper → Ask Question → Retrieve Context → Generate Answer → Show Citations

(Place screenshots inside `/screenshots` folder)

---

## Key Features

- Upload and index research PDFs
- Semantic search using embeddings
- Retrieval Augmented Generation (RAG)
- Grounded answers (no hallucinations)
- Page-level citations
- Groq Llama3 ultra-fast inference
- Modular production-style backend
- Docker ready

---

## System Architecture

            ┌─────────────────────┐
            │      User Query      │
            └──────────┬──────────┘
                       ↓
            ┌─────────────────────┐
            │     FastAPI API      │
            └──────────┬──────────┘
                       ↓
            ┌─────────────────────┐
            │   Vector Retriever   │
            │  (FAISS Similarity)  │
            └──────────┬──────────┘
                       ↓
            ┌─────────────────────┐
            │   Top-K Chunks       │
            └──────────┬──────────┘
                       ↓
            ┌─────────────────────┐
            │ Prompt + Context     │
            └──────────┬──────────┘
                       ↓
            ┌─────────────────────┐
            │   Llama3 (Groq)      │
            └──────────┬──────────┘
                       ↓
            ┌─────────────────────┐
            │ Grounded Answer +    │
            │ Source Citations     │
            └─────────────────────┘

---

## Tech Stack

### AI / GenAI
- Retrieval Augmented Generation (RAG)
- LangChain
- Llama3 via Groq API
- Sentence Transformers Embeddings
- FAISS Vector Database

### Backend
- FastAPI
- Python
- Pydantic
- Modular service architecture

### Infra
- Docker
- Environment configuration
- Scalable API design

---

## How RAG Works in This Project

### Step 1 — Ingestion
- PDF loaded using PyPDFLoader
- Text split into overlapping chunks
- Metadata preserved (page numbers)

### Step 2 — Embeddings
Each chunk converted into vector embeddings using Sentence Transformers.

### Step 3 — Storage
Vectors stored in FAISS index for similarity search.

### Step 4 — Retrieval
User question converted into embedding → top-k similar chunks retrieved.

### Step 5 — Generation
LLM receives only retrieved context with strict prompt:

> "Answer only using the provided context. If not found, say not found."

This eliminates hallucinations.

---

## Project Structure

research-gpt/
├── backend/
│ ├── app/
│ │ ├── api/ # API routes
│ │ ├── core/ # Config & LLM provider
│ │ ├── db/ # Vector database logic
│ │ ├── services/ # RAG pipeline
│ │ ├── schemas/ # Request/response models
│ │ └── main.py
│ ├── requirements.txt
│ └── .env
│
├── data/papers # Uploaded documents
├── screenshots # Demo images
├── docker-compose.yml
└── README.md


---

## Setup Guide

### 1. Clone Repo
```bash
git clone https://github.com/yourusername/ResearchGPT
cd research-gpt/backend
2. Create Virtual Environment
Windows

python -m venv venv
venv\Scripts\activate
Mac/Linux

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables
Create .env inside backend:

GROQ_API_KEY=your_api_key_here
LLM_MODEL=llama3-70b-8192
Get API key from:
https://console.groq.com/keys

5. Run Application
uvicorn app.main:app --reload
Open:

http://127.0.0.1:8000/docs
API Usage
Upload Research Paper
POST /api/upload

Upload PDF file via Swagger UI.

Ask Question
POST /api/ask

Example request:

{
  "question": "What problem does this paper solve?"
}
Example response:

{
  "answer": "The paper proposes a novel transformer architecture...",
  "sources": ["page 2", "page 5"]
}
Design Decisions
Why RAG instead of fine-tuning?

Works with private documents

No retraining needed

Cheaper and scalable

Why FAISS?

Fast local similarity search

No external DB dependency

Why Groq?

Ultra-low latency inference

Free developer tier

Production-grade performance

Future Enhancements
Streaming responses

Multi-document QA

Hybrid search (BM25 + vectors)

Reranking models

Frontend chat UI

AWS S3 document storage

Kubernetes deployment

Skills Demonstrated
LLM application engineering

Retrieval Augmented Generation

Prompt engineering

Embedding search

API design

Production architecture

License
MIT


---

