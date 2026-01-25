from fastapi import FastAPI
from fastapi.responses import HTMLResponse 

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


@app.get("/", response_class= HTMLResponse)
def home():
    return f"<h1>{posts[0]["title"]}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts
