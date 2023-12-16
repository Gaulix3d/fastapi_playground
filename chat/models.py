from sqlalchemy import Column, String, DateTime
from database import Base
import datetime

class MessageModel(Base):
    __tablename__ = "Messages"
    email = Column(String)
    message = Column(String)
    sent_date = Column(DateTime)
