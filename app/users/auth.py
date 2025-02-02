from argon2 import PasswordHasher
from datetime import datetime, timedelta, timezone
from jose import jwt
from pydantic import EmailStr

from app.users.dao import UsersDAO
from app.config import settings
from app.exceptions import IncorrectEMailOrPasswordException

pwd_context = PasswordHasher()

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(hashed_password, plain_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.HASH_ALGO
    )
    return encode_jwt

async def auth_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    try:
        if user and verify_password(password, user.hashed_password):
            return user
    except Exception:
        raise IncorrectEMailOrPasswordException

