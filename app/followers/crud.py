from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.follow import Follow

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

async def unfollow(db: AsyncSession,
                   follower_id: int,
                   followed_id: int):
    follow = await db.execute(
        select(Follow)
        .where((Follow.follower_id==follower_id)&
               (Follow.followed_id==followed_id)
               )
    )
    follow = follow.scalar_one_or_none()
    #я спать, надо дописать