from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import pandas as pd

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    id: Optional[int] = None


my_posts = [
    {"title": "First post", "content": "My first post...", "id": 1},
    {"title": "Second post", "content": "My second post...", "id": 2}
]


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/posts/latest")
def get_latest_post():
    df = pd.DataFrame(my_posts).set_index('id')

    return {"post_detail": df.iloc[-1].to_dict()}


@app.get("/posts/{id}")
def get_post(id: int):
    # use indexing of dataframe to find a post by id
    df = pd.DataFrame(my_posts).set_index('id')

    try:
        post = df.loc[id].to_dict()
    except Exception:
        post = f"Post #{id} not found."
    # loc() returns a series, so we need to convert it to a dict
    return {"post_detail": post}


# @app.post("/createposts")
@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"data": new_post.dict()}
