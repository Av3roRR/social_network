from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.models import Like
from sqlalchemy import delete
class LikesDao(BaseDAO):
    model = Like
    @classmethod
    async def delete_like(cls, user_id: int, like_id: int):
        async with async_session_maker() as session:
            query = delete(cls.model).where((cls.model.user_id == user_id) & (cls.model.id == like_id))
            if query is not None:
                await session.execute(query)
                await session.commit()
            return "лайк удален"
