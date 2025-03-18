import uvicorn
from fastapi import FastAPI

app = FastAPI()


def start():
    uvicorn.run(app="tsn.main:app", reload=True)


@app.get("/")
async def index():
    return {"status": "It's ALIVE!"}