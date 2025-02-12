from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.models.follow import Follow
from sqlalchemy.orm import selectinload

async def create_follow(db: AsyncSession,
                        follower_id: int,
                        followed_id: int):
    if follower_id==followed_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="нельзя подписаться на себя")

    existing_follow = await db.execute(
        select(Follow).where((Follow.follower_id == follower_id)&
                             (Follow.followed_id == followed_id)
                             )
    )
    if existing_follow.scalar_one_or_none():
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="вы уже подписаны")
    new_follow = Follow(followed_id=followed_id,follower_id=follower_id)
    db.add(new_follow)
    await db.commit()
    return new_follow

async def delete_follow(db: AsyncSession,
                   follower_id: int,
                   followed_id: int):
    follow = await db.execute(
        select(Follow)
        .where((Follow.follower_id==follower_id)&
               (Follow.followed_id==followed_id)
               )
    )
    follow = follow.scalar_one_or_none()
    if not follow:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="подписка не обнаружена")
    await db.delete(follow)
    await db.commit()
    return {"message":"вы отписались"}

async def get_followers(db: AsyncSession, users_id: int):
    result = await db.execute(
        select(Follow)
        .where(Follow.followed_id==users_id)
        .options(selectinload(Follow.follower))
    )
    return result.scalars().all()

async def get_following(db: AsyncSession,
                        user_id: int):
    result = await db.execute(
        select(Follow)
        .where(Follow.follower_id==user_id)
        .options(selectinload(Follow.followed))
    )
    return result.scalars().all()
