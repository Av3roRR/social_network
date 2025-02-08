from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import *
from app.posts.schemas import PostCreate, PostUpdate, PostResponse
from app.posts.crud import (
    create_post,
    get_post,
    get_posts_feed,
    delete_post
)
from app.users.dependencies import get_current_user, get_async_session

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostResponse)
async def create_new_post(
        post_data: PostCreate,
        db: AsyncSession = Depends(get_async_session),
        current_user: User = Depends(get_current_user)
):
    try:
        return await create_post(db, post_data, current_user.id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/feed", response_model=list[PostResponse])
async def read_feed(
        db: AsyncSession = Depends(get_async_session),
        current_user: User = Depends(get_current_user),
        skip: int = 0,
        limit: int = 100
):
    posts = await get_posts_feed(db, current_user.id, skip, limit)
    return posts


@router.delete("/{post_id}")
async def remove_post(
        post_id: int,
        db: AsyncSession = Depends(get_async_session),
        current_user: User = Depends(get_current_user)
):
    post = await get_post(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    if post.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own posts"
        )

    await delete_post(db, post_id)
    return {"message": "Post deleted successfully"}