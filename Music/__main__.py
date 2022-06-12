

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

"from Music.config import BOT_NAME"
"from Music.config import UPDATE"
"from Music.config import SUPPORT"
"from Music.config import START_IMG"
"from Music.config import DURATION_LIMIT"
"from Music.config import MONGO_DB_URI"

response = requests.get(BG_IMG)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)

if BOT_NAME:
    BOT_NAME = config.BOT_NAME
else: 
    BOT_NAME = 'KaalXMusic'

if UPDATE:
    UPDATE = config.UPDATE
else: 
    UPDATE = 'Murat_30_God'

if SUPPORT:
    SUPPORT = config.SUPPORT
else: 
    SUPPORT = 'Murat_30_God'

if START_IMG:
    START_IMG = config.START_IMG
else: 
    START_IMG = 'https://telegra.ph/file/f6d20eb3b3a7c810c09a0.jpg'

if DURATION_LIMIT:
    DURATION_LIMIT = config.DURATION_LIMIT
else: 
    DURATION_LIMIT = '180'

if MONGO_DB_URI:
    MONGO_DB_URI = config.MONGO_DB_URI
else: 
    MONGO_DB_URI = 'mongodb+srv://mabma:BlackMamba@cluster0.ok5je.mongodb.net/?retryWrites=true&w=majority'

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
