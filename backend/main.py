import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ARTICLES = []

class Citation(BaseModel):
    id: str
    title: str
    creators: list
    issued: dict
    type: str

class Article(BaseModel):
    id: str
    title: str
    content: str
    citations: List[Citation]

@app.get("/")
def read_root():
    return {"message": "Juris.js Article Submission API"}

@app.post("/api/articles")
def submit_article(article: Article):
    ARTICLES.append(article)
    return {"message": "Article stored", "id": article.id}

@app.get("/api/articles")
def list_articles():
    return ARTICLES

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

