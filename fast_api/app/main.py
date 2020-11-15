from typing import Optional
from fastapi import FastAPI
from models import Post

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/posts")
def get_all_posts():
	result = []
	for p in Post.objects: 
		result.append({
				"title": p['title'],
				"content": p['content'],
				"author": p['author'],
				"published": p['published'],
			})
	return result