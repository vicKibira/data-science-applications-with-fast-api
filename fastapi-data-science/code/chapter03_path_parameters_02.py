# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users/{type}/{id}")
# async def get_useer(type: str, id: int):
#     return {"type": type, "id": id}


# class UserType(str):
#     STANDARD = "standard"
#     ADMIN = "admin"

# @app.get("/users/{type}/{id}")
# async def get_user(type: UserType, id: int):
#     return {"type": type, "id": id}


from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {"type": type.value, "id": id}
