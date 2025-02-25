from fastapi import FastAPI
from app.users.router import router as users_router
from app.posts.router import router as posts_router
from app.comments.router import router as comment_router
from app.likes.router import router as likes_router
from app.followers.router import router as followers_router
from contextlib import asynccontextmanager
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from collections.abc import AsyncIterator
from sqladmin import Admin
from app.admin.view import UserAdmin, PostAdmin, LikeAdmin, FollowAdmin, CommentAdmin
from app.database import async_engine as engine
@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    print("-------начало---------")
    yield
    print("-------конец---------")
app = FastAPI(lifespan=lifespan)



admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
admin.add_view(LikeAdmin)
admin.add_view(FollowAdmin)
admin.add_view(CommentAdmin)


app.include_router(users_router)
app.include_router(posts_router)
app.include_router(comment_router)
app.include_router(likes_router)
app.include_router(followers_router)
