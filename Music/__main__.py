
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
 

async def load_start():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[INFO]: SENDING RESTART STATUS")
        try:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted the Bot Successfully.**",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        print("Error came while clearing db")
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)
        except Exception as e:
            print("Error came while clearing db")
    

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())

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
