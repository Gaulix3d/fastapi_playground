from pydantic import BaseModel, EmailStr
from datetime import datetime


class MessageSchema(BaseModel):
    email: EmailStr
    message: str
    sent_date: datetime

