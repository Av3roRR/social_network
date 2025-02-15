from fastapi import APIRouter, Depends

from app.exceptions import AlreadyLikeExist, PostIsNotPresentException, LikeIsNotPresentException, CommentIsNotPresentException
from app.models.user import User
from app.users.dependencies import get_current_user, get_async_session
from app.posts.dao import PostDao
from app.likes.dao import LikesDao
from app.comments.dao import CommentDao
router = APIRouter(prefix="/likes", tags=["likes"])

@router.post("/posts/{post_id}")
async def like_post(post_id: int, current_user: User = Depends(get_current_user)):
    new_like = await LikesDao.find_one_or_none(post_id=post_id,user_id = current_user.id)
    if new_like:
        raise AlreadyLikeExist
    is_post_exist = await PostDao.find_one_or_none(id=post_id)
    if not is_post_exist:
        raise PostIsNotPresentException
    await LikesDao.add(post_id=post_id, user_id=current_user.id)
    return "лайк поставлен"
@router.post("/comment/{comment_id}")
async def like_comment(comment_id: int, current_user: User = Depends(get_current_user)):
    new_like = await LikesDao.find_one_or_none(comment_id=comment_id,user_id = current_user.id)
    if new_like:
        raise AlreadyLikeExist
    is_post_exist = await CommentDao.find_one_or_none(id=comment_id)
    if not is_post_exist:
        raise CommentIsNotPresentException
    await LikesDao.add(comment_id=comment_id, user_id=current_user.id)
    return "лайк поставлен"
@router.delete("/{like_id}")
async def remove_like(like_id: int, current_user: User = Depends(get_current_user)):
    like = await LikesDao.find_one_or_none(id=like_id, user_id=current_user.id)
    if not like:
        raise LikeIsNotPresentException
    await LikesDao.delete_like(current_user.id,like_id)
    return "лайк удален"


