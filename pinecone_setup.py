#Start FIle - 4
# Sets up Pinecone (Vector databases) for storing all the embeddings Uses env for config

import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

# Replace with your Pinecone credentials
PINECONE_API_KEY = "pcsk_4CjHkx_5nzVgACuiQPsiRqWFzZHQphC9jmS3SRZoEKXUScJgmatTz8W8oMFApoLRJ8zgMG"
PINECONE_ENV = "us-east1-aws"

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index
index_name = "cobol-code-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print("Index created!")
else:
    print("Index already exists.")
