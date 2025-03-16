from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

app = FastAPI()

@app.get("/users")
async def get_user(format: UsersFormat):
    return {"format": format}