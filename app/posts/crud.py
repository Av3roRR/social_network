from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.models.post import Post
from app.models.comment import Comment
from app.models.follow import Follow
from app.posts.schemas import PostCreate

async def create_post(db: AsyncSession, post_data: PostCreate, user_id: int):
    new_post = Post(
        content=post_data.content,
        media_url=post_data.media_url,
        author_id=user_id
    )
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post

async def get_post(db: AsyncSession, post_id: int):
    result = await db.execute(
        select(Post)
        .options(selectinload(Post.author))
        .where(Post.id == post_id)
    )
    return result.scalar_one_or_none()

async def get_posts_feed(
    db: AsyncSession,
    user_id: int,
    skip: int = 0,
    limit: int = 100
):
    result = await db.execute(
        select(Post)
        .join(Follow, Follow.followed_id == Post.author_id)
        .where(Follow.follower_id == user_id)
        .order_by(Post.created_at.desc())
        .offset(skip)
        .limit(limit)
        .options(
            selectinload(Post.author),
            selectinload(Post.comments).selectinload(Comment.author),
            selectinload(Post.likes)
        )
    )
    return result.scalars().all()

async def delete_post(db: AsyncSession, post_id: int):
    await db.execute(delete(Post).where(Post.id == post_id))
    await db.commit()