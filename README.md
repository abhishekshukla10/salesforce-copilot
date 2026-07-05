# Salesforce RAG Copilot — Enterprise CRM Knowledge Assistant

🔗 **Live Demo:** [salesforce-copilot.streamlit.app](https://salesforce-copilot.streamlit.app)

Ask anything about Salesforce workflows — instant answers with **source citations**, built on real enterprise CRM process data.

---

## Business Problem

CRM users can't find process answers — support tickets pile up, onboarding takes weeks, and costly data entry mistakes happen daily. Process knowledge lives in spreadsheets nobody reads.

## Solution

A RAG knowledge assistant over multi-sheet Excel process documentation: semantic search retrieves the right process chunks, an LLM answers conversationally with source citations, and chat history maintains context.

## How It Works

```
Multi-sheet Excel → Markdown conversion
        ↓
Document chunking → HuggingFace sentence-transformer embeddings
        ↓
FAISS vector index
        ↓
User question → semantic search → top-3 chunks
        ↓
Groq LLM → answer + source citation
        ↓
Streamlit chat UI with session history
```

## Key Technical Decisions

- **Migrated from Chroma to FAISS** after identifying cloud deployment incompatibility on Streamlit Cloud — a real infrastructure debugging exercise, not a tutorial choice
- **Excel → Markdown pre-processing** — preserves table structure semantically so process steps stay coherent inside chunks
- **Source citation on every answer** — grounds responses and lets users verify against the original process doc, addressing hallucination risk directly
- **st.secrets for key management** — no credentials in code

## Business Impact

- Instant CRM process answers, 24/7, no human support
- Reduces onboarding time · prevents data entry errors
- Built on real Salesforce implementation data from an enterprise deployment

## Stack

`LangChain` `FAISS` `HuggingFace sentence-transformers` `Groq API` `Streamlit Cloud` `Python`

## Setup

```bash
pip install -r requirements.txt
# add GROQ_API_KEY to .streamlit/secrets.toml
streamlit run app.py
```

## Roadmap

→ Salesforce Adoption Intelligence — proactive prompts based on user behaviour, auto-generated onboarding content
