from pydantic import BaseModel, EmailStr

class RegistrationModel(BaseModel):
    username: str
    email: EmailStr
    password: str