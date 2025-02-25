from datetime import datetime
from sqlalchemy import ForeignKey, Text, func, select
from sqlalchemy.orm import relationship, mapped_column, Mapped, column_property
from app.database import Base
from app.models.comment import Comment
from app.models.like import Like
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text)
    media_url: Mapped[str | None] = mapped_column(nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Отношения
    author = relationship("app.models.user.User", back_populates="posts", lazy="selectin")
    comments = relationship(
        "app.models.comment.Comment",
        back_populates="post",
        lazy="selectin",
        cascade="all, delete-orphan",
        order_by="app.models.comment.Comment.created_at.desc()"
    )
    likes = relationship(
        "app.models.like.Like",
        back_populates="post",
        lazy="selectin",
        cascade="all, delete-orphan"
    )
    # для подсчета лайков и комментариев
    likes_count = column_property(
        select(func.count(Like.id)).where(Like.post_id == id).scalar_subquery()
    )
    comments_count = column_property(
        select(func.count(Comment.id)).where(Comment.post_id == id).scalar_subquery()
    )

    def __str__(self):
        return f"Пост №{self.id}"