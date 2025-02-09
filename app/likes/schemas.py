from pydantic import BaseModel


class LikeBase(BaseModel):
    pass
class LikeResponse(LikeBase):
    id: int
    user_id: int
    post_id: int|None
    comment_id: int|None
