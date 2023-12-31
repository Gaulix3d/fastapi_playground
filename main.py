from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from auth.router import auth_router
from database import init_db
from chat.router import chat_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(router=auth_router)
app.include_router(router=chat_router)

@app.get('/')
def hi():
    return 'Fuck'
