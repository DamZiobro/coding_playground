import logging
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@app.get("/")
async def root():
    logger.info("triggering /")
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    logger.info("triggering /users")
    return {"message": "Get Users!"}

handler = Mangum(app)
