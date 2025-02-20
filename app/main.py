from fastapi import FastAPI
from app.users.router import router as users_router
from app.posts.router import router as posts_router
from app.comments.router import router as comment_router
from app.likes.router import router as likes_router
from app.followers.router import router as followers_router
from contextlib import asynccontextmanager


app = FastAPI()


app.include_router(users_router)
app.include_router(posts_router)
app.include_router(comment_router)
app.include_router(likes_router)
app.include_router(followers_router)