
import os
import asyncio
import requests
from pyrogram import Client
from pytgcalls import idle
from Music import app
from Music import client
from Music.database.functions import clean_restart_stage
from Music.database.queue import get_active_chats, remove_active_chat
from Music.tgcalls.calls import run
from Music.config import API_ID, API_HASH, BOT_TOKEN, BG_IMG, BOT_NAME
from Music.config import *

# Directly access!
UPDATE = os.environ.get("UPDATE", "")
response = requests.get(BG_IMG)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)

# Directly access!
BOT_NAME = os.environ.get("BOT_NAME", "")


UPDATE = os.environ.get("UPDATE", "") if os.environ.get("UPDATE", "") else "Murat_30_God"
    
SUPPORT = os.environ.get("SUPPORT", "") if os.environ.get("SUPPORT", "") else "Murat_30_God"
    
START_IMG = os.environ.get("SUPPORT", "") if os.environ.get("START_IMG", "") else "https://telegra.ph/file/f6d20eb3b3a7c810c09a0.jpg"

DURATION_LIMIT = os.environ.get("DURATION_LIMIT", "180")

MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "") if os.environ.get("MONGO_DB_URI", "") else "mongodb+srv://CALLMEVP:CALLMEVP@cluster0.scvdq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
 

Client.run()
idle()

Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Music.modules"},
).start()

run()
idle()
loop.close()
