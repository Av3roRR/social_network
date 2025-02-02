from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy import Text, func
from models.base import Base



class Post(Base):
    __tablename__ = "posts"
    id = mapped_column(primary_key=True)
    content = mapped_column(Text)
    media_url = mapped_column(nullable=True)
    author_id = mapped_column(ForeignKey("users.id"))
    created_at = mapped_column(server_default=func.now())
    

