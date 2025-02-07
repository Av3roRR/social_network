from datetime import datetime
from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import relationship, mapped_column, Mapped  # Добавлен Mapped
from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    # Аннотации с использованием Mapped (SQLAlchemy 2.x стиль)
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text)
    media_url: Mapped[str | None] = mapped_column(nullable=True)  # Явное указание Optional
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Отношения с ленивой загрузкой
    author = relationship("User", back_populates="posts", lazy="selectin")
    comments = relationship(
        "Comment",
        back_populates="post",
        lazy="selectin",
        cascade="all, delete-orphan",
        order_by="Comment.created_at.desc()"
    )
    likes = relationship(
        "Like",
        back_populates="post",
        lazy="selectin",
        cascade="all, delete-orphan"
    )