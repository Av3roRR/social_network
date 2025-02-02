from fastapi import Depends, Request 
from jose import jwt, JWTError 
from datetime import datetime, timezone

from app.exceptions import *
from app.config import settings
from app.users.dao import UsersDAO

def get_token(request: Request):
    token = request.cookies.get("_user_cookie")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.HASH_ALGO
        )
    except JWTError:
        raise IncorrectTokenFormatException

    expire: str = payload.get("exp")
    if not expire or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise ExpiredTokenException
    
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException

    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException

    return user

