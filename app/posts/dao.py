from app.dao.base import BaseDAO
from app.models import Post

class PostDao(BaseDAO):
    model = Post