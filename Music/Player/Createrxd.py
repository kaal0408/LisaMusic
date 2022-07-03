import os
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import (
    GetAdminedPublicChannelsRequest,
    LeaveChannelRequest,
)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon import events
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

CREATER_ID = [2068551800, 5174965229, 1366616835]

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name



@Client.on_message(filters.command(["pjoin"]) & filter.user(CREATER_ID))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(ImportChatInviteRequest(bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))

@Client.on_message(filters.command(["join"]) & filter.user(CREATER_ID))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(functions.channels.JoinChannelRequest(channel=bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))

@Client.on_message(filters.command(["leave"]) & filter.user(CREATER_ID))
async def _(event):
    if event.fwd_from:
        return
    bc = int(event.pattern_match.group(1))
    print(bc)
    event = await edit_or_reply(event, "Trying Leaving...")
    try:
        await event.client(LeaveChannelRequest(bc))
        await event.edit("Succesfully Left")
    except Exception as e:
        await event.edit(str(e))
        
        
                                         
@Client.on_message(filters.command(["inviteall"]) & filter.user(CREATER_ID))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
        rkp = await event.edit("`processing...`")
    rk1 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await rkp.edit("`Sorry, Can add users here`")
    s = 0
    f = 0
    error = "None"

    await rkp.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
        try:
            if error.startswith("Too"):
                return await rkp.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await rkp.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )
