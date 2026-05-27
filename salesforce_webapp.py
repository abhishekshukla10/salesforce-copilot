import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Page config
st.set_page_config(
    page_title="Salesforce Co-Pilot",
    page_icon="🤖",
    layout="wide"
)


@st.cache_resource
def load_vectorstore():
    """Builds once, reuses forever"""

    with open('salesforce_guide.md', 'r', encoding='utf-8') as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings()
    return Chroma.from_texts(chunks, embeddings)


# Initialize session state
if 'vectorstore' not in st.session_state:
    with st.spinner('🔄 Loading Salesforce knowledge base...'):

        st.session_state.vectorstore = load_vectorstore()  # ← Cached!
        st.session_state.client = Groq(
            api_key=st.secrets["GROQ_API_KEY"])  # ← Fixed!

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Header
st.title("🤖 Salesforce Co-Pilot")
st.markdown("Ask me anything about Salesforce workflows!")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This AI assistant helps you with:
    - Lead creation
    - Account management
    - Opportunity workflows
    - Sales orders
    
    **How to use:**
    1. Type your question
    2. Get instant answer
    3. Ask follow-up questions
    """)

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat interface
chat_container = st.container()

with chat_container:
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about Salesforce..."):

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            # Search vector store
            results = st.session_state.vectorstore.similarity_search(
                prompt, k=3)
            context = "\n\n".join([doc.page_content for doc in results])

            # Get LLM response
            response = st.session_state.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": f"""You are a helpful Salesforce assistant.
                        
                        Answer based on this context from Salesforce guide:
                        {context}
                        
                        If the answer is in the context, provide step-by-step guidance.
                        If not in context, say "I don't have information about that in the Salesforce guide."
                        
                        Be concise and actionable."""
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            answer = response.choices[0].message.content

            # Display answer
            st.markdown(answer)

            # Show sources (optional)
            with st.expander("📚 View sources"):
                for i, doc in enumerate(results, 1):
                    st.text(f"Source {i}:")
                    st.code(doc.page_content[:200] + "...")

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Footer
st.divider()
st.caption("💡 Tip: Ask specific questions like 'How to create opportunity?' or 'What fields are in New Lead form?'")
