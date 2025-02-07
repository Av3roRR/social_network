from app.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, ForeignKey, func, relationship

from datetime import datetime

class Comment(Base):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    author = relationship("User", back_populates="comments")
