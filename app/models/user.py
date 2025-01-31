from sqlalchemy import String, func
from sqlalchemy.orm import mapped_column

from social_network.app.models.base import Base
class User(Base):
    __tablename__ = "users"
    id = mapped_column(primary_key=True)
    email = mapped_column(String(255),index=True, unique=True)
    username = mapped_column(String(255), unique=True)
    hashed_password = mapped_column(String(255))
    avatar_url = mapped_column(String(2048), nullable=True)
    is_active = mapped_column(default=True)
    created_at = mapped_column(server_default= func.now())