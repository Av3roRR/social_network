from app.comments import crud
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.comments.crud import create_comment
from app.comments.schemas import CommentResponse, CommentCreate
from app.models.user import User
from app.users.dependencies import get_async_session, get_current_user

router = APIRouter(prefix="/posts/{post_id}/comments",tags=["comments"])

@router.post("/", response_model=CommentResponse)
async def create_new_comment(post_id: int,
                             comment_data: CommentCreate,
                             db: AsyncSession = Depends(get_async_session),
                             current_user: User = Depends(get_current_user)):
    return await create_comment(db=db,comment_data=comment_data,user_id=current_user.id,post_id = post_id)