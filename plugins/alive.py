import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/52408ad857d8c3a91aff6.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ Owner : [Owner](https://t.me/Murat_30_God)

┣★ updates : [Support channel](https://t.me/Murat_30_God)

┣★ Youtube : [Youtuber channel](https://t.me/adityadiscus)

┣★ Make your own  music bot › : [REPO](https://github.com/kaal0408/Music)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/Murat_30_God) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " support Channel ", url=f"https://t.me/Murat_30_God")
                ]
                [
                    InlineKeyboardButton(
                        "YouTube", url=f"https://youtube.com/channel/UCpZBwvZJdRsInUBgAWfpVMA")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/c6e1041c6c9a12913f57a.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Support channel 💞", url=f"https://t.me/Murat_30_God")
                ]
                [
                    InlineKeyboardButton(
                        "YouTube", url=f"https://youtube.com/channel/UCpZBwvZJdRsInUBgAWfpVMA")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/52408ad857d8c3a91aff6.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💞 Make your own bot 💞", url=f"https://github.com/kaal0408/Music")
                ]
               [
                    InlineKeyboardButton(
                        "YouTube", url=f"https://youtube.com/channel/UCpZBwvZJdRsInUBgAWfpVMA")
                ] 
            ]
        ),
    )
