from fastapi import APIRouter

router = APIRouter(
    prefix='/users',
    tags=["Пользователи"]
)

@router.get('')
async def hello():
    return 'Hello'