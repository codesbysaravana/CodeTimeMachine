#Start FIle - 5
# Uses Open APIs to generate the embeddings for the inputted COBOL code

#Upserts (updates/inserts) these embeddings into Pinecone
#Contains functions for getting embeddings and a main processing function

import os
from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI

# Step 1: Load API keys from .env file
load_dotenv()

# ✅ Proper client initialization
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Add this right after load_dotenv()
print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')[:5]}...")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Step 3: Connect to your Pinecone index
index = pc.Index("cobol-code-index")

# Step 4: Path to your cleaned COBOL code folder
CLEANED_DIR = "cleaned_cobol"

# Step 5: Function to get OpenAI embedding
def get_embedding(text):
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

# Step 6: Main function to process each file and upsert to Pinecone
def main():
    for filename in os.listdir(CLEANED_DIR):
        if filename.endswith(".cbl"):
            filepath = os.path.join(CLEANED_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read()
                vector = get_embedding(code)

                doc_id = filename.replace(".cbl", "")
                index.upsert(vectors=[(doc_id, vector)])

                print(f"✅ Upserted {doc_id} to Pinecone.")

# Step 7: Run it!
if __name__ == "__main__":
    main()
