from pydantic import BaseModel, EmailStr

class RegistrationModel(BaseModel):
    username: str
    email: EmailStr
    password: str
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
