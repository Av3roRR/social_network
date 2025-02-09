
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.comment import Comment
from app.comments.schemas import CommentCreate


async def create_comment(db:AsyncSession, comment_data:CommentCreate, user_id: int, post_id: int):
    comment = Comment(
        text = comment_data.text,
        author_id = user_id,\
        post_id = post_id
    )
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    return comment


