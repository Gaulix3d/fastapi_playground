from auth.token import get_current_user
from sqlalchemy.orm import Session
from database import get_db
from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketException,
    status,
    APIRouter,
)
from chat.schemas import MessageSchema
from datetime import datetime
from chat.crud import add_message, get_messages
chat_router = APIRouter()


@chat_router.websocket('/chat')
async def chat_page(websocket: WebSocket, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        schema_message = MessageSchema(email=current_user, message= str(data), sent_date= datetime.utcnow())
        add_message(schema_message, db)
        await websocket.send_json(schema_message)

@chat_router.get('/messages')
async def get_all_messages(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_messages(db)


