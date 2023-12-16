from pydantic import BaseModel, EmailStr, dat
from datetime import datetime


class MessageSchema(BaseModel):
    email: EmailStr
    message: str
    sent_date: datetime
