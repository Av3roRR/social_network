
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,  delete
from app.models.like import Like
from sqlalchemy.orm import selectinload

async def create_like(db: AsyncSession, user_id: int, post_id: int|None = None, comment_id: int|None = None):
    existing_like = await db.execute(
        select(Like)
        .where(
            (Like.user_id == user_id)&((Like.post_id == post_id)|(Like.comment_id == comment_id))
        )
    )
    existing_like = existing_like.scalar_one_or_none()
    if existing_like:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="лайк уже был поставлен")
    like = Like(
        user_id=user_id,
        post_id=post_id,
        comment_id=comment_id
    )
    db.add(like)
    await db.commit()
    await db.refresh(like)
    return like


async def get_like(db: AsyncSession, like_id: int):
    result = await db.execute(
        select(Like)
        .where(Like.id == like_id)
    )
    return result.scalar_one_or_none()

async def delete_like(db: AsyncSession, like_id: int, user_id: int):
    like = await get_like(db,like_id)
    if not like:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="лайк не обнаружен")
    if like.user_id != user_id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="нельзя удалить чужой like")
    await db.delete(like)
    await db.commit()
    return {"message":"лайк удален"}


