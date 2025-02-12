from app.dao.base import BaseDAO
from app.models.follow import Follow
from sqlalchemy import insert, delete, select, update

from app.database import async_session_maker

class FollowersDao(BaseDAO):
    model=Follow
    
    @classmethod
    async def delete(cls, user_id: int, followed_id: int):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.follower_id == user_id, cls.model.followed_id == followed_id)
            if query is not None:
                await session.execute(query)
                await session.commit()
            
            return "Удалено из подписок"