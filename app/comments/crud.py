from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from app.models.comment import Comment
from app.comments.schemas import CommentCreate
from sqlalchemy.orm import selectinload

async def create_comment(db:AsyncSession, comment_data:CommentCreate, user_id: int, post_id: int):
    comment = Comment(
        text = comment_data.text,
        author_id = user_id,
        post_id = post_id
    )
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    return comment

async def get_comment(db:AsyncSession, comment_id: int):
    result = await db.execute(
        select(Comment)
        .options(selectinload(Comment.author))
        .where(Comment.id == comment_id)
                             )
    return result.scalar_one_or_none()


