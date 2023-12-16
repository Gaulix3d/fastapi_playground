from sqlalchemy import Column, String, DateTime, Integer
from database import Base
import datetime

class MessageModel(Base):
    __tablename__ = "Messages"
    message_id = Column(Integer, primary_key= True, index=True)
    email = Column(String)
    message = Column(String)
    sent_date = Column(DateTime)

