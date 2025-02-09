from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    author_id: int
    post_id: int
    created_at: datetime
    likes_count: int = 0

