from pydantic import BaseModel
from datetime import datetime
from app.users.schemas import UserResponse

class FollowBase(BaseModel):
    pass

class FollowCreate(FollowBase):
    followed_id: int

class FollowResponse(FollowBase):
    id: int
    follower: UserResponse
    followed: UserResponse
    created_at: datetime