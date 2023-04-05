

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS
from modules import bot

@bot.on_message(filters.command(["gcast", "post", "post"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`StarTiNG BroAdCaST...`")
        if not message.reply_to_message:
            await wtf.edit("**__Ƥɭɘɑsɘ Ʀɘƥɭy Ƭø ɑ Mɘssɑʛɘ Ƭø Stɑɤt Ɓɤøɑɗƈɑst ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in bot.iter_dialogs():
            try:
                await bot.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Ɓɤøɑɗƈɑstɩŋʛ` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`Ɠƈɑst Sʋƈƈɘssfʋɭɭy` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} Ƈɦɑts")





#assistant_broadcast

@Client.on_message(filters.command(["agcast", "apost", "asend"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`StarTiNG BroAdCaST...`")
        if not message.reply_to_message:
            await wtf.edit("**__Ƥɭɘɑsɘ Ʀɘƥɭy Ƭø ɑ Mɘssɑʛɘ Ƭø Stɑɤt Ɓɤøɑɗƈɑst ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Ɓɤøɑɗƈɑstɩŋʛ` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`Ɠƈɑst Sʋƈƈɘssfʋɭɭy` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} Ƈɦɑts")
