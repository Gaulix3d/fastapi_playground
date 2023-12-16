from chat.schemas import MessageSchema
from chat.models import MessageModel
from database import get_db

def add_message(message_data: MessageSchema, db: get_db):
    data_to_add = MessageModel(**message_data.model_dump())
    db.add(data_to_add)
    db.commit()
    db.refresh(data_to_add)
    return data_to_add

def get_messages(db: get_db):
    return db.query(MessageModel).all()
