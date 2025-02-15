from app.dao.base import BaseDAO
from app.models import Comment


class CommentDao(BaseDAO):
    model = Comment