from datetime import datetime
from pydantic import BaseModel, Field
from app.users.schemas import UserResponse
#from app.comment.schemas import CommentResponse на будущее

class PostBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=2000)
    media_url: str|None

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author: UserResponse
    created_at: datetime
    likes_count: int
    comments_count: int
    #top_comments: List[CommentResponse] = [] на будущее
