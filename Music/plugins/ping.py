from datetime import datetime
from pyrogram import Client
from pyrogram import filters
from main import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

ms = "Kaalxuser"

@manjeet.on_message(filters.command(["ping", "Ping"], [".", "!" , "/"]) & filters.me)
@manjeet.on_message(filters.command(["ping", "Ping"], [".", "!" ,"/"]) & filters.user(SUDO_USER))
async def ping(_, message: Message):
    await message.reply_text(f"""⭐ **
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱
┃╰━╯┃╭━━╮╭━━╮╭━━╮
┃╭━━╯┃╭╮┃┃╭╮┃┃╭╮┃
┃┃╱╱╱┃╰╯┃┃┃┃┃┃╰╯┃
╰╯╱╱╱╰━━╯╰╯╰╯╰━╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
** ⭐MY MS → `{ms}`\n """)
