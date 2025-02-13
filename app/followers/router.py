from fastapi import APIRouter, Depends

from app.users.dependencies import get_current_user
from app.exceptions import UserIsNotPresentException
from app.followers.dao import FollowersDao

router = APIRouter(
    prefix="/follows"
)

@router.get("")
async def get_follows(user = Depends(get_current_user)):
    if not user:
        raise UserIsNotPresentException
    
    user_follows = await FollowersDao.find_all(follower_id=user.id)
    
    return user_follows

@router.post("")
async def add_follow(followed_id: int, user = Depends(get_current_user)):
    if not user:
        raise UserIsNotPresentException
    
    await FollowersDao.add(follower_id=int(user.id), followed_id=int(followed_id))
    return "Подписка оформлена"

@router.post("")
async def delete_follow(followed_id, user = Depends(get_current_user)):
    await FollowersDao.delete(user.id, followed_id)