from fastapi import APIRouter

from api.endpoints.posts import router as posts_router

router = APIRouter()

router.include_router(
    posts_router,
    prefix="/posts",
    tags=["posts"],
    responses={
        404: {"description": "Not found"},
        400: {"description": "Bad Request"}
    },
)
