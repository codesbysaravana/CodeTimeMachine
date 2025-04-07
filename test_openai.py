import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("🔐 OpenAI Key:", api_key[:8], "...")

client = OpenAI(api_key=api_key)

res = client.embeddings.create(
    input=["test"],
    model="text-embedding-ada-002"
)

print("✅ It works! Here's a sample embedding vector:", res.data[0].embedding[:5])
