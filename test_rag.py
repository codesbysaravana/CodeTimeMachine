import os
from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI

# Step 1: Load environment variables
load_dotenv()

# Step 2: Initialize OpenAI and Pinecone clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Step 3: Connect to your Pinecone index
index = pinecone_client.Index("cobol-code-index")

# Step 4: Define your question
question = "How is file handling done in COBOL?"

# Step 5: Get embedding for the question
embed_response = openai_client.embeddings.create(
    input=[question],
    model="text-embedding-ada-002"
)
question_embedding = embed_response.data[0].embedding

# Step 6: Query Pinecone
query_response = index.query(
    vector=question_embedding,
    top_k=3,
    include_metadata=True
)

# Step 7: Build context from retrieved results
matches = query_response.get("matches", [])
if not matches:
    print("⚠️ No matches found in Pinecone.")
    exit()

context = "\n\n---\n\n".join(
    [match["metadata"].get("text", "") for match in matches]
)

# Step 8: Use OpenAI GPT to generate answer using the context
chat_response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a COBOL expert helping a developer."},
        {"role": "user", "content": f"Given this COBOL code:\n\n{context}\n\nAnswer this question:\n{question}"}
    ]
)

# Step 9: Print the answer
print("\n🧠 GPT Answer:\n", chat_response.choices[0].message.content)
