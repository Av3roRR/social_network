from app.dao.base import BaseDAO
from app.models.user import User


class UsersDAO(BaseDAO):
    model = User