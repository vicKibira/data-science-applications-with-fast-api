from fastapi import FastAPI


app = FastAPI()


# @app.get("/users/{id}")
# async def get_user_id(id: int):
#     return {"id": id}


class UserType(str):
    STANDARD = "standard"
    ADMIN = "admin"

@app.get("/users/{type}/{id}")
async def get_user(type: str, id: int):
    return {"type": type, "id": id}


@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}