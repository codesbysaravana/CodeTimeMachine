import os
from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI

load_dotenv()

# Initialize clients
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("cobol-code-index")

# Get embedding for query
def get_query_embedding(text):
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

# Query Pinecone
def query_index(query):
    vector = get_query_embedding(query)
    results = index.query(vector=vector, top_k=3, include_metadata=True)
    return results

if __name__ == "__main__":
    user_query = input("🔎 Ask a COBOL-related question: ")
    matches = query_index(user_query)

    print("\n📄 Top Matching Files:")
    for match in matches['matches']:
        print(f"➡️  {match['id']} with score {match['score']}")
