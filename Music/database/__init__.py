## Copyright (©) Team Codexun

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from Codexun.config import MONGO_DB_URI


MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb
