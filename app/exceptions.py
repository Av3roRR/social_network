from fastapi import HTTPException, status

UserAlreadyExist = HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                 detail="Пользователь с такой почтой уже сущестует")

IncorrectEMailOrPasswordException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Неправильная почта или пароль"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Токен не найден"
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Неправильный токен"
)

ExpiredTokenException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Токен просрочен"
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Пользователь не найден"
)

AlreadyFollowingException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Вы уже подписаны на этого пользователя"
)