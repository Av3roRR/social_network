from social_network.app.models.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Text, ForeignKey, func


class Comment(Base):
    __tablename__ = "comments"
    id = mapped_column(primary_key=True)
    text = mapped_column(Text)
    author_id = mapped_column(ForeignKey("users.id"))
    post_id = mapped_column(ForeignKey("posts.id"))
    created_at = mapped_column(server_default=func.now())

