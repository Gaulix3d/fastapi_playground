from datetime import timedelta, datetime
from jose import jwt, JWTError
from typing import Annotated
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.schemas import UserGetSchema
from auth.crud import get_user_data
from database import get_db
from auth.security import security

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


SECRET_KEY = 'ff32476201ee03bc6a0ce5292ce5863eb1ac1351df7367778a4d01262af77981'
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        email = UserGetSchema(email=username)
    except JWTError:
        raise credentials_exception
    user = get_user_data(get_db, email)
    if user is None:
        raise credentials_exception
    return user.email


def authenticate_user(get_db, username: str, password: str):
    user = get_user_data(get_db, UserGetSchema(email=username))
    if not user:
        return False
    if not security.verify_password(password, user.password):
        return False
    return user
