from fastapi import FastAPI
from pydantic import BaseModel
from query_code import search_codebase
from rag_query import run_rag_pipeline

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.post("/query-code")
def query_code(input: QueryInput):
    results = search_codebase(input.query)
    return {"matches": results}

@app.post("/rag")
def query_rag(input: QueryInput):
    response = run_rag_pipeline(input.query)
    return response
