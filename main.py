from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


