from fastapi import APIRouter, Depends

from app.users.dependencies import get_current_user
from app.exceptions import UserIsNotPresentException, AlreadyFollowingException
from app.followers.dao import FollowersDao
from app.models import User
from fastapi_cache.decorator import cache
router = APIRouter(
    prefix="/follows",
    tags=["follows"]
)

@router.get("")
@cache(expire=30)
async def get_follows(user = Depends(get_current_user)):
    if not user:
        raise UserIsNotPresentException
    
    user_follows = await FollowersDao.find_all(follower_id=user.id)
    #await sleep(5)
    return user_follows

@router.post("")
async def add_follow(followed_id: int, user: User = Depends(get_current_user)):
    if not user:
        raise UserIsNotPresentException
    
    follows = await FollowersDao.find_one_or_none(follower_id=int(user.id), followed_id=int(followed_id))
    
    if not follows:
        raise AlreadyFollowingException
    
    await FollowersDao.add(follower_id=int(user.id), followed_id=int(followed_id))
    
    return "Подписка оформлена"

@router.post("")
async def delete_follow(followed_id, user = Depends(get_current_user)):
    await FollowersDao.delete_follow(user.id, followed_id)