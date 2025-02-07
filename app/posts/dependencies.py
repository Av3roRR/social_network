from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.posts.crud import get_post
from app.users.dependencies import get_async_session
from app.models.post import Post
async def get_current_post(
    post_id: int,
    db: AsyncSession = Depends(get_async_session)
) -> Post:
    post = await get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

def check_post_ownership(post: Post = Depends(get_current_post), user: User = Depends(get_current_user)):
    if post.author_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return post