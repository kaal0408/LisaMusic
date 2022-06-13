import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from Music.utils.filters import command

from Music import BOT_NAME, BOT_USERNAME
from Music.config import * 

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**Welcome {message.from_user.mention()}** 👋

This is the **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Bot,** a bot for playing high quality and unbreakable music in your groups voice chat.

Just add me to your group & make as a admin with needed admin permissions to perform a right actions, now let's enjoy your music!

Use the given buttons for more info📍""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", callback_data="cbcmnds"),
                    InlineKeyboardButton(
                        "About", callback_data="cbabout")
                ],
                [
                    InlineKeyboardButton(
                        "Basic Guide", callback_data="cbguide")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )
