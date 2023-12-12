from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    email: EmailStr


class UserPostSchema(UserSchema):
    password: str

class UserGetSchema(UserSchema):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

