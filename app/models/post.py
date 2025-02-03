from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text, func
from app.database import Base

from datetime import datetime

class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text)
    media_url: Mapped[str] = mapped_column(nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    

