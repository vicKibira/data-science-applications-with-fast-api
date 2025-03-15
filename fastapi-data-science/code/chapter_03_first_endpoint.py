from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"hello":"world"}


# if __name__ == "main":
#     hello_world()