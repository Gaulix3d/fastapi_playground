from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware




class Item(BaseModel):
    key1: str
    key2: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return item