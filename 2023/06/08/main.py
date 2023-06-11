from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    date_published: datetime | None = None


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/posts")
def get_posts():
    return {"data": "Here're your posts."}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post.dict()}
