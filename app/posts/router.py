from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["Посты"]
)

@router.post()
async def create_post():
    pass