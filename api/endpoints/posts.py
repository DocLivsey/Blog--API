from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.post import PostCreate, PostResponse
from models.post import Post
from services.cache import get_post_cache, set_post_cache

router = APIRouter()

@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    set_post_cache(db_post)
    return Response(
        {'msg': 'successfully created post'},
        status_code=status.HTTP_201_CREATED
    )

@router.get("/{post_id}", response_model=PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    cached_post = get_post_cache(post_id)
    if cached_post:
        return cached_post

    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        set_post_cache(post)
    return post