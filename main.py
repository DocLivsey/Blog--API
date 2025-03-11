from api.main import create_app
from api.routes.posts import router as posts_router

app = create_app(posts_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
