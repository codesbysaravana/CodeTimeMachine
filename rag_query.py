import os
from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("cobol-code-index")

def get_query_embedding(query):
    response = client.embeddings.create(
        input=[query],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def ask_openai(question, context):
    messages = [
        {"role": "system", "content": "You are an expert COBOL code explainer."},
        {"role": "user", "content": f"Here is some COBOL code:\n\n{context}\n\nAnswer this:\n{question}"}
    ]
    res = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return res.choices[0].message.content.strip()

def run_rag_pipeline(question):
    query_vector = get_query_embedding(question)
    result = index.query(vector=query_vector, top_k=3, include_metadata=True)

    contexts = []
    for match in result['matches']:
        doc_id = match['id']
        file_path = os.path.join("cleaned_cobol", f"{doc_id}.cbl")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                contexts.append(f.read())

    full_context = "\n\n---\n\n".join(contexts)

    answer = ask_openai(question, full_context)
    return {
        "question": question,
        "context_count": len(contexts),
        "answer": answer
    }
