from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.comments.crud import create_comment
from app.likes.crud import create_like, delete_like
from app.likes.schemas import LikeResponse
from app.users.dependencies import get_current_user, get_async_session
router = APIRouter(prefix="/likes", tags=["likes"])

@router.post("/posts/{post_id}", response_model=LikeResponse)
async def like_post(post_id: int, db:AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_user)):
    return await create_like(db=db,user_id=current_user.id,post_id=post_id)

@router.post("/likes/{like_id}", response_model=LikeResponse)
async def like_comment(comment_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_user)):
    return await create_like(db=db,user_id=current_user.id,comment_id=comment_id)

@router.delete("/{like_id}")
async def remove_like(like_id: int, db:AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_user)):
    return delete_like(db,like_id,current_user.id)
