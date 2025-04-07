import os
from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("cobol-code-index")

def get_query_embedding(text):
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def search_codebase(query, top_k=3):
    query_vector = get_query_embedding(query)
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=False)
    
    matches = []
    for match in results['matches']:
        matches.append({
            "id": match['id'],
            "score": match['score']
        })

    return matches
