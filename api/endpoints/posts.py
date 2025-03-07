from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.post import PostCreate, PostResponse, PostUpdate
from models.post import Post
from services.cache import get_post_cache, set_post_cache

router = APIRouter()

@router.post("/", response_model=Response)
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

@router.put("/{post_id}", response_model=Response)
def update_post(updated_post: PostUpdate, db: Session = Depends(get_db)):
    cached_post = get_post_cache(updated_post.id)
    if cached_post:
        return cached_post

    post = db.query(Post).filter(Post.id == updated_post.id).first()
    if post:
        set_post_cache(post)

    post.title = updated_post.title
    post.content = updated_post.content
    db.commit()
    db.refresh(post)
    return Response(
        {'msg': 'successfully updated post'},
        status_code=status.HTTP_200_OK
    )
