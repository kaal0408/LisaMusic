import yt_dlp
from Process.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Music.config import (
    ASSISTANT_NAME,
    BOT_USERNAME,
)
from Music.inline import menu_markup, song_download_markup, stream_markup, audio_markup

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Hello , My name is Vc Bot .

I'm a telegram streaming bot with some useful features.

Feel free to add me to your groups.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
               [                   
                    InlineKeyboardButton(
                        "😕Commands 😕 ", callback_data="cbbasic")
                ]
                [
                    InlineKeyboardButton(
                       "💛Repo💛", url=f"https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkaal0408%2FMusic&plugins=postgresql&envs=SESSION_NAME%2CASSISTANT_NAME%2CBOT_TOKEN%2CAPI_ID%2CAPI_HASH%2CBOT_USERNAME%2CSUDO_USERS")
                ]
                    InlineKeyboardButton(
                       "💜Support💜", url=f"https://t.me/Astro_HelpChat")
                ]
                [
                    InlineKeyboardButton(
                        "💞 Add Me To Your Group 💞",
                        url= f"https://t.me/{BOT_USERNAME}?startgroup=true",
                  )
               ]
                    
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🎶  commands🎶""",
         reply_markup=InlineKeyboardMarkup(
            [
               [                   
                    InlineKeyboardButton(
                        "Player ", callback_data="cbplays")
                    InlineKeyboardButton(
                        "Quote", callback_data="cbquotes")
                ]
                [
                    InlineKeyboardButton(
                       "telegraph", callback_data="cbteles")
                    InlineKeyboardButton(
                       "Userbot", callback_data="cbuserbots")
                ]
                [                   
                    InlineKeyboardButton(
                        "Broadcast ", callback_data="cbgcasts")
                    InlineKeyboardButton(
                        "Dictionary", callback_data="cbdefins")
                ]
                [
                    InlineKeyboardButton(
                       "Github", callback_data="cbgits")
                    InlineKeyboardButton(
                       "Paste", callback_data="cbpasites")                
                [                   
                    InlineKeyboardButton(
                        "Song", callback_data="cbsongs")
                ]
                [
                    InlineKeyboardButton(
                       "information", callback_data="cbinfos")
                    InlineKeyboardButton(
                       "id", callback_data="cbids")            
                 [                   
                    InlineKeyboardButton(
                        "Uptime", callback_data="cbups")
                    InlineKeyboardButton(
                       " Live Stream", callback_data="cbstreams")
                ]
                [
                    InlineKeyboardButton(
                       "Wallpaper", callback_data="cbwalls")
                    InlineKeyboardButton(
                       "Anime", callback_data="cbanimes")
                ] 
                [
                    InlineKeyboardButton(
                       "Database", callback_data="cbdbms")
                    InlineKeyboardButton(
                       "Repo", callback_data="cbrepos")
                ] 
                [
                    InlineKeyboardButton(
                        "🔙 Go Back ", callback_data="cbstart") 
                ]
                    
            ]
        ),

@Client.on_callback_query(filters.regex("cbplays"))
async def cbplays(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Player menu
Play - To play song from YouTube
Vplay - To play a video song from YouTube
Skip - To skip a song
end - To end voice chat
mute - To mute in voice chat
unmute - To unmute in voice chat
resume - To resume song
pause - To pause song
stop - To stop music bot
For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbquots"))
async def cbquots(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Quote menu
Quote - To make a quote

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbteles"))
async def cbteles(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Telegraph menu
tm - To change pic and video in link
tgm - To change pic and video in link
For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbuserbots"))
async def cbuserbots(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""userbot menu
reload - To Reload the not
userbotjoin - To join in group
join - To join in group
userbotleave - To leave from group
leaveall - To leave all group
For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbgcasts"))
async def cbgcasts(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Broadcast menu
gcast - To broadcast any message or media (only sudo)

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbdefins"))
async def cbdefins(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Dictionary menu
define - To define any word

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbgits"))
async def cbgits(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Github menu
github - To check some one github account

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbpastes"))
async def cbpaste(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""paste menu
paste- To paste documents

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsongs"))
async def cbsongs(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Song menu
song - To download any song
vsong - To download any video
lyrics - To download any song lyrics
search - To search any video

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbinfos"))
async def cbinfos(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""infomation menu
info - To get user information

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbups"))
async def cbups(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""uptime menu
uptime - To check uptime
ping - To check ping speed
speedtest - To check speed

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbstreams"))
async def cbstreams(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""stream menu
stream - To stream live video
vstream - To stream live YouTube channel

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back",  callbacack_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbwalls"))
async def cbwalls(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""wallpaper menu
wall - To preview wallpaper

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbanimes"))
async def cbanimes(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Anime menu
whatanime - To check anime

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbrepos"))
async def cbrepos(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Source code menu
repo - To get the source code

For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbdbsms"))
async def cbdbems(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Database menu
rmd,clear - To delete download files
rmw,clean- To delete Raw files
cleanup - To clean datbase
For more join @Kaalxsupport.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbbasic")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
          await query.answer("Control Panel Opened")
          await query.edit_message_reply_markup(         
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ Nothing is Currently Streaming", show_alert=True)

@Client.on_callback_query(filters.regex("cbdown"))
async def cbdown(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = song_download_markup(videoid)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex(pattern=r"song_back"))
async def songs_back_helper(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = song_download_markup(videoid)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex(pattern=r"gets"))
async def song_helper_cb(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    try:
        await CallbackQuery.answer("soon", show_alert=True)
    except:
        pass
    if stype == "audio":
        try:
            formats_available, link = await YouTube.formats(
                videoid, True
            )
        except:
            return await CallbackQuery.edit_message_text("Download audio")
        keyboard = InlineKeyboard()
        done = []
        for x in formats_available:
            check = x["format"]
            if "audio" in check:
                if x["filesize"] is None:
                    continue
                form = x["format_note"].title()
                if form not in done:
                    done.append(form)
                else:
                    continue
                sz = convert_bytes(x["filesize"])
                fom = x["format_id"]
                keyboard.row(
                    InlineKeyboardButton(
                        text=f"{form} Quality Audio = {sz}",
                        callback_data=f"song_download {stype}|{fom}|{videoid}",
                    ),
                )
        keyboard.row(
            InlineKeyboardButton(
                text="🔙 Back",
                callback_data=f"song_back {stype}|{videoid}",
            ),
            InlineKeyboardButton(
                text="✖️ Close ", callback_data=f"cls"
            ),
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=keyboard
        )
    else:
        try:
            formats_available, link = await YouTube.formats(
                videoid, True
            )
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("Download video")
        keyboard = InlineKeyboard()
        # AVC Formats Only [ YUKKI MUSIC BOT ]
        done = [160, 133, 134, 135, 136, 137, 298, 299, 264, 304, 266]
        for x in formats_available:
            check = x["format"]
            if x["filesize"] is None:
                continue
            if int(x["format_id"]) not in done:
                continue
            sz = convert_bytes(x["filesize"])
            ap = check.split("-")[1]
            to = f"{ap} = {sz}"
            keyboard.row(
                InlineKeyboardButton(
                    text=to,
                    callback_data=f"song_download {stype}|{x['format_id']}|{videoid}",
                )
            )
        keyboard.row(
            InlineKeyboardButton(
                text="🔙 Back",
                callback_data=f"song_back {stype}|{videoid}",
            ),
            InlineKeyboardButton(
                text="✖️ Close", callback_data=f"cls"
            ),
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=keyboard
        )

@Client.on_callback_query(filters.regex(pattern=r"song_download"))
async def song_download_cb(client, CallbackQuery):
    try:
        await CallbackQuery.answer("Downloading")
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, format_id, videoid = callback_request.split("|")
    mystic = await CallbackQuery.edit_message_text(_["song_8"])
    yturl = f"https://www.youtube.com/watch?v={vidid}"
    with yt_dlp.YoutubeDL({"quiet": True}) as ytdl:
        x = ytdl.extract_info(yturl, download=False)
    title = (x["title"]).title()
    title = re.sub("\W+", " ", title)
    thumb_image_path = await CallbackQuery.message.download()
    duration = x["duration"]
    if stype == "video":
        thumb_image_path = await CallbackQuery.message.download()
        width = CallbackQuery.message.photo.width
        height = CallbackQuery.message.photo.height
        try:
            file_path = await YouTube.download(
                yturl,
                mystic,
                songvideo=True,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
            return await mystic.edit_text("error".format(e))
        med = InputMediaVideo(
            media=file_path,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=title,
            supports_streaming=True,
        )
        await mystic.edit_text("video")
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_video",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text("soonvideo")
        os.remove(file_path)
    elif stype == "audio":
        try:
            filename = await YouTube.download(
                yturl,
                mystic,
                songaudio=True,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
            return await mystic.edit_text("error".format(e))
        med = InputMediaAudio(
            media=filename,
            caption=title,
            thumb=thumb_image_path,
            title=title,
            performer=x["uploader"],
        )
        await mystic.edit_text("audio")
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_audio",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text("soonaudio")
        os.remove(filename)

@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id, dlurl)
    if chat_id in QUEUE:
          await query.answer("Back")
          await query.edit_message_reply_markup(         
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ Nothing is Currently Streaming", show_alert=True)
    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
