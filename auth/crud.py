from database import get_db
from auth.models import UserModel
from auth.schemas import UserPostSchema, UserGetSchema
from auth.security import security


def create_user(db: get_db, item: UserPostSchema):
    item.password = security.get_password_hash(password= item.password)
    db_item = UserModel(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user_data(db: get_db, item: UserGetSchema):
    return db.query(UserModel).filter(UserModel.email == item.email).first()
    