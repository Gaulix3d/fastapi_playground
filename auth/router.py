from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.schemas import UserPostSchema, Token
from database import get_db
from auth.crud import create_user
from auth.token import authenticate_user, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta

auth_router = APIRouter()
ACCESS_TOKEN_EXPIRE_MINUTES = 10000
@auth_router.post('/register')
def user_register(user: UserPostSchema, db: Session = Depends(get_db)):
    return create_user(db=db, item=user)

@auth_router.post('/token', response_model=Token)
def user_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}


