# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
from pyrogram import Client
from Music.MusicUtilities.helpers.filters import command

@Client.on_message(command(["asupan"]))
async def asupan(client, message):
    message.from_user.id
    message.from_user.first_name
    message.from_user.id
    user_id = message.from_user.id
    message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(
            message.chat.id, video=results, caption=f"This the sexy video bro {rpk}"
        )
    except Exception:
        await message.reply_text("❌ There is something wrong...")


@Client.on_message(command(["wibu"]))
async def wibu(client, message):
    message.from_user.id
    message.from_user.first_name
    message.from_user.id
    user_id = message.from_user.id
    message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(
            message.chat.id, video=results, caption=f"This is the real wibu bro {rpk}"
        )
    except Exception:
        await message.reply_text("❌ There is something wrong...")


@Client.on_message(command(["chika"]))
async def chika(client, message):
    message.from_user.id
    message.from_user.first_name
    message.from_user.id
    user_id = message.from_user.id
    message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(
            message.chat.id, video=results, caption=f"She is beautiful right {rpk} ?"
        )
    except Exception:
        await message.reply_text("❌ There is something wrong...")


@Client.on_message(command(["truth"]))
async def truth(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/truth").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("❌ There is something wrong...")


@Client.on_message(command(["dare"]))
async def dare(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/dare").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("❌ There is something wrong...")
