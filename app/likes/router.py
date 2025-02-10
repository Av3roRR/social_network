from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.comments.crud import create_comment
from app.likes.crud import create_like
from app.likes.schemas import LikeResponse
from app.users.dependencies import get_current_user, get_async_session
router = APIRouter(prefix="/likes", tags=["comments"])

@router.post("/posts/{post_id}", response_model=LikeResponse)
async def like_post(post_id: int|None, db:AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_user)):
    return await create_like(db,current_user.id,post_id)
