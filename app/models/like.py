from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from social_network.app.models.base import Base

class Like(Base):
    __tablename__ = "likes"
    id = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    post_id = mapped_column(ForeignKey("posts.id"))
