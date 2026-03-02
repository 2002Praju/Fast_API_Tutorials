from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 

app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author" : "Prajwal Vyavahare",
        "title" : "FastAPI is Awesome",
        "content" : "This framework is really easy to use and super fast. ",
        "date_posted" : "January 25, 2025",
    },
    {
        "id":2,
        "author" : "Jane Doe",
        "title" : "Python is Great for Web Developers",
        "content" : "Python is a great language for web development, and FastAPI makes it even ",
        "date_posted" : "January 25, 2025",
    },
]


@app.get("/", response_class= HTMLResponse, include_in_schema=False)    # include_in_schema=False is used to hide this endpoint from the docu
@app.get("/posts", response_class= HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts
