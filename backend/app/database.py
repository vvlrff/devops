import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase

DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["mongo"]

