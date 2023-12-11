from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.schemas import UserPostSchema
from database import get_db
from auth.crud import create_user

auth_router = APIRouter()

@auth_router.post('/register')
def user_register(user: UserPostSchema, db: Session = Depends(get_db)):
    return create_user(user, db)

@auth_router.post('/login')
def user_login(user: UserPostSchema, db: Session = Depends(get_db)):
    pass



