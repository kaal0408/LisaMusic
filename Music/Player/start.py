from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Music.config import (
    ASSISTANT_NAME,
    BOT_USERNAME,
)
from Process.filters import other_filters2
from time import time
from Process.filters import command
from datetime import datetime
from Process.decorators import authorized_users_only

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello {message.from_user.mention()}💞💞.
I'm a🎶 telegram streaming bot with some useful features🎵.
Feel free to add me to your groups🎧.
Total modules -22
Total commands-40
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "😕Commands & Help😕 ", callback_data="cbbasic"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "😔Assistant command😔", callback_data="cbhowtouse"
                    ),
                  ],[
                    InlineKeyboardButton(
                       "💛Repo💛", url=f"https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkaal0408%2FMusic&plugins=postgresql&envs=SESSION_NAME%2CASSISTANT_NAME%2CBOT_TOKEN%2CAPI_ID%2CAPI_HASH%2CBOT_USERNAME%2CSUDO_USERS"
                    ),
                    InlineKeyboardButton(
                       "💜Support💜", url=f"https://t.me/Murat_30_God"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💞 Add Me To Your Group 💞",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
    )

@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f6d20eb3b3a7c810c09a0.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💜ʀᴇᴘᴏ 💜", url=f"https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkaal0408%2FMusic&plugins=postgresql&envs=SESSION_NAME%2CASSISTANT_NAME%2CBOT_TOKEN%2CAPI_ID%2CAPI_HASH%2CBOT_USERNAME%2CSUDO_USERS")
                ]
            ]
        ),
    )
