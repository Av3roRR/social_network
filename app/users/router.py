from fastapi import APIRouter, Response, Request
from pydantic import EmailStr

from app.users.schemas import RegistrationModel, UserResponse, UserCreateResponse
from app.users.dao import UsersDAO
from app.exceptions import UserAlreadyExist
from app.users.auth import get_password_hash, create_access_token, auth_user
from app.exceptions import UserIsNotPresentException
from app.users.dependencies import get_token

router = APIRouter(
    prefix='/users',
    tags=["Пользователи"]
)

@router.post('/registration',response_model=UserCreateResponse)
async def registration(user_data: RegistrationModel):
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise UserAlreadyExist
    
    new_user = await UsersDAO.add(username=user_data.username,
                                  email=user_data.email,
                                  hashed_password=get_password_hash(user_data.password))
    if new_user:
        return {"msg":"Пользователь создан", "user":new_user}
    else:
        return "Не создан"
    

@router.post("/auth")
async def login(response: Response, email: EmailStr, password: str):
    user = await auth_user(email=email, password=password)
    if user:
        cookie = create_access_token({"sub": str(user.id)})
        
        response.set_cookie("_user_cookie", cookie, httponly=True)
        return "Вы вошли в свою учетную запись"
    return "Вы не смогли войти в аккаунт"

@router.get("")
async def quit_account(response: Response):
    response.delete_cookie("access_token")