from fastapi import APIRouter, Depends
from auth.token import get_current_user
chat_router = APIRouter()


@chat_router.get('/chat')
def chat_page(current_user: dict = Depends(get_current_user)):
    return current_user
