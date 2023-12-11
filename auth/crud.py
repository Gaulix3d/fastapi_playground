from database import get_db
from models import UserModel
from schemas import UserPostSchema, UserGetSchema
from security import Security

def create_user(db: get_db, item: UserPostSchema):
    item.password = Security.get_password_hash(password= item.password)
    db_item = UserModel(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_user_data(db: get_db, item: UserGetSchema):
    pass