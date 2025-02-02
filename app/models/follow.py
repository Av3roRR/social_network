from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy import func
from social_network.app.models.base import Base


class Follow(Base):
    __tablename__ = "follows"
    follower_id = mapped_column(ForeignKey("users.id"), primary_key=True)
    followed_id = mapped_column(ForeignKey("users.id"),primary_key=True)
    created_at = mapped_column(server_default=func.now())

