from pydantic import BaseModel, EmailStr


class Usersignup(BaseModel):
    email: EmailStr
    password: str


class Userlogin(BaseModel):
    email: EmailStr
    password: str