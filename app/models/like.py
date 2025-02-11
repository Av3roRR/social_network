from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base

from sqlalchemy.orm import relationship


class Like(Base):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int | None] = mapped_column(ForeignKey("posts.id"), nullable=True)
    comment_id: Mapped[int | None] = mapped_column(ForeignKey("comments.id"), nullable=True)

    # Отношения
    user = relationship("User", back_populates="likes")  # Добавлено
    post = relationship("Post", back_populates="likes")
    comment = relationship("Comment", back_populates="likes")