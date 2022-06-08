import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.raw.base import Update
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram import filters


@Client.on_message(command("start") & filters.private )
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c247284e8ddc50f01a314.png",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜**""",
    reply_markup=InlineKeyboardMarkup(
            [   
                [
                    InlineKeyboardButton("✗ ᴡᴀɴɴᴀ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ​ ✗", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
               ],
                [
                    InlineKeyboardButton(
                        "♥️ Creator ♥️", url=f"https://t.me/Murat_30_God")
               ],
                [
                    InlineKeyboardButton(
                        "Repo ✨", url=f"https://github.com/kaal0408/Music")
               ], 
                [
                    InlineKeyboardButton(
                        "👨‍💻 YouTube", url=f"https://youtube.com/channel/UCpZBwvZJdRsInUBgAWfpVMA")
               ],
                [
                    InlineKeyboardButton(
                        "💝 Commands 💝", url=f"https://telegra.ph/Music-04-06-2")
                ]
                
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group )
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c247284e8ddc50f01a314.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Repo 💞", url=f"https://github.com/kaal0408/Music")
                ]
            ]
        ),
    )


