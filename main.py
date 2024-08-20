from datetime import datetime

from fastapi import FastAPI, Body, Path

from queue_manager import queue_manager

app = FastAPI()


@app.get("/")
async def index():
    return {
        "running": True,
        "time": datetime.utcnow()
    }


@app.post("/queue/{queue_name}")
async def post_to_queue(queue_name: str = Path(...),
                        body: dict = Body(...)):
    await queue_manager.publish(queue_name, body)


@app.post("/mndy-queue")
async def handle_message():
    return "Ok"
