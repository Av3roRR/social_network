from select import select

from app.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship, column_property
from sqlalchemy import Text, ForeignKey, func, select, where
from datetime import datetime
from app.models.like import Like

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    author = relationship("app.models.user.User", back_populates="comments")
    post = relationship("app.models.post.Post", back_populates="comments")
    likes = relationship("app.models.like.Like", back_populates="comment")  # Исправил

    #лайки для комментариев
    likes_count = column_property(
        select(func.count(Like.id)).where(Like.comment_id == id).scalar_subquery()
    )