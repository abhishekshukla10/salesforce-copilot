from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# read the knowledge file
with open('salesforce_guide.md', 'r', encoding='utf-8') as f:
    text = f.read()

# test
# print(f"Loaded {len(text)} characters")

# PIECE 3: SPLIT TEXT INTO CHUNKS
# Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_text(text)
print(f"Split into {len(chunks)} chunks")

# PIECE 4: CREATE EMBEDDINGS & STORE IN CHROMA
# Create embeddings and vector store
print("Creating embeddings (first time = slow)...")
embeddings = HuggingFaceEmbeddings()

vectorstore = Chroma.from_texts(chunks, embeddings)
print("✅ Vector database created!")


# PIECE 5: QUERY THE RAG SYSTEM (Type these lines)

# Initialize Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Ask a question
question = "What is Machine Learning?"

# Search vector database
results = vectorstore.similarity_search(question, k=2)
context = "\n\n".join([doc.page_content for doc in results])

print(f"\n📚 Found relevant chunks:\n{context[:200]}...\n")

# Ask LLM with context
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": f"Answer based on this context:\n{context}"},
        {"role": "user", "content": question}
    ]
)

print(f"🤖 Answer: {response.choices[0].message.content}")

# NOW LET'S MAKE IT INTERACTIVE:

# Interactive mode
print("\n💬 Ask questions! (type 'quit' to exit)\n")

while True:
    question = input("You: ")
    if question.lower() == 'quit':
        break

    # Search
    results = vectorstore.similarity_search(question, k=2)
    context = "\n\n".join([doc.page_content for doc in results])

    # Answer
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"Answer based on this context:\n{context}"},
            {"role": "user", "content": question}
        ]
    )

    print(f"🤖 {response.choices[0].message.content}\n")
