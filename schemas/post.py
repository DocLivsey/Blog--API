from pydantic import BaseModel


class PostScheme(BaseModel):
    title: str
    content: str

class PostCreate(PostScheme):
    pass

class PostUpdate(PostScheme):
    id: int

class PostResponse(PostScheme):
    id: int

    class Config:
        from_attributes = True