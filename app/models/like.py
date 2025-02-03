from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base

class Like(Base):
    __tablename__ = "likes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    #is_comment_like = mapped_column(default=False)
    