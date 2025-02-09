
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.comments.crud import create_comment, get_comments_for_post, get_comment, delete_comment
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

@router.get("/",response_model=list[CommentResponse])
async def read_comments(post_id: int,
                        skip: int = 0,
                        limit: int = 100,
                        db: AsyncSession = Depends(get_async_session)):
    return await get_comments_for_post(db=db, post_id=post_id,skip=skip,limit=limit)

@router.delete("/{comment_id}")
async def remove_comment(comment_id: int,
                         db: AsyncSession = Depends(get_async_session),
                         current_user: User = Depends(get_current_user)):
    comment = await get_comment(db,comment_id)
    if not comment:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="комментарий не найден")
    if comment.author_id != current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="нельзя удалять чужой комментарий")
    await delete_comment(db,comment_id)
    return {"message":"комментарий удален"}
