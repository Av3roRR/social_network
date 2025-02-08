from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base

class Like(Base):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int | None] = mapped_column(ForeignKey("posts.id"), nullable=True)  # Может быть null
    comment_id: Mapped[int | None] = mapped_column(ForeignKey("comments.id"), nullable=True)  # Добавил

    # Отношения
    user = relationship("app.models.user.User", back_populates="likes")
    post = relationship("app.models.post.Post", back_populates="likes")
    comment = relationship("app.models.comment.Comment", back_populates="likes")  # Добавил
