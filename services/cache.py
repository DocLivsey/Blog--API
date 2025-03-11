import json
import redis.asyncio as redis
from core.config import settings
from schemas.post import PostResponse

redis_client = redis.Redis.from_url(settings.REDIS_URL)


async def get_post_cache(post_id: int):
    post = await redis_client.get(f"post_{post_id}")
    if post:
        return PostResponse(**json.loads(post))
    return None

def set_post_cache(post):
    redis_client.setex(
        f"post_{post.id}",
        300,
        json.dumps(post.dict())
    )