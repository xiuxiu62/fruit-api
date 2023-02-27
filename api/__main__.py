import asyncio
from fastapi import FastAPI, HTTPException
from uvicorn import Server, Config as ServerConfig

from api.database import database
from api.services.fruit import FruitService


app = FastAPI()
fruit_service = FruitService(database)


@app.get("/ping")
def ping():
    return "pong"


@app.get("/fruit")
async def list_fruits():
    return fruit_service.list()


@app.get("/fruit/{id}")
async def get_fruit(id: int):
    return fruit_service.get(id)


@app.post("/fruit")
async def create_fruit(name: str):
    return fruit_service.create(name)


@app.patch("/fruit/{id}")
async def update_fruit(id: int, name: str):
    return fruit_service.update_or_insert(id, name)


@app.delete("/fruit/{id}")
async def remove_fruit(id: int):
    match fruit_service.remove(id):
        case None:
            raise HTTPException(
                status_code=400, detail=f"Could not find fruit with id `{id}`")
        case fruit:
            return fruit


async def serve():
    config = ServerConfig(app, reload=True, log_level="info")
    await Server(config).serve()


if __name__ == "__main__":
    asyncio.run(serve())
