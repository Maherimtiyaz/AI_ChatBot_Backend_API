from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_URI)

db = client["chatbot_db"]

users_collection = db["users"]
sessions_collection = db["sessions"]
messages_collection = db["messages"]