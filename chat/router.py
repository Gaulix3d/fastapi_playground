from auth.token import get_current_user
from sqlalchemy.orm import Session
from database import get_db
import json
from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketException,
    status,
    APIRouter,
    Request,
    WebSocketDisconnect
)
from chat.schemas import MessageSchema
from datetime import datetime
from chat.crud import add_message, get_messages
chat_router = APIRouter()


@chat_router.websocket('/chat')
async def chat_page(websocket: WebSocket, token: str = None, db: Session = Depends(get_db)):
    print(token)
    if token is None:
        await websocket.close()
        return

    await websocket.accept()
    print(f'Someone connected with token: {token}')
    current_user = await get_current_user(token=token, db=db)

    while True:
        try:
            data = await websocket.receive_text()
            schema_message = MessageSchema(email=current_user.email, message=data, sent_date=datetime.utcnow())
            add_message(schema_message, db)
            await websocket.send_json(schema_message.model_dump_json())
        except WebSocketDisconnect as e:
            # Handle the disconnect, log, or perform cleanup
            print(f"WebSocket disconnect: {e}")
            break  # Exit the loop on disconnect
        except WebSocketException as e:
            # Handle other exceptions
            print(f"Error in WebSocket communication: {e}")

@chat_router.get('/messages')
async def get_all_messages(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_messages(db)



