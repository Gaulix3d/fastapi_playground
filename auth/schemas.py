from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    email: EmailStr
    password: str

class UserPostSchema(UserSchema):
    pass

class UserGetSchema(UserSchema):
    id: int