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
                        "😕Commands 😕 ", callback_data="cbbasic"
                ]
                [
                    InlineKeyboardButton(
                       "💛Repo💛", url=f"https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkaal0408%2FMusic&plugins=postgresql&envs=SESSION_NAME%2CASSISTANT_NAME%2CBOT_TOKEN%2CAPI_ID%2CAPI_HASH%2CBOT_USERNAME%2CSUDO_USERS"
                ]
                    InlineKeyboardButton(
                       "💜Support💜", url=f"https://t.me/Astro_HelpChat"
                ]
                [
                    InlineKeyboardButton(
                        "💞 Add Me To Your Group 💞",
                        url= f"https://t.me/{BOT_USERNAME}?startgroup=true", 
                ]
                    
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🎶 **Assistant commands🎶:**

1.) **/realod- To reload the bot.**
2.) **/gcast - To broadcast a message.**
3.) **/q - To make a quote.**
3.) **/tm - to make a telegraph linl.**
4.) **/userbotjoin - To join assistant id.**
5.) **/userbotleave,leave - To leave assistant id
6.) **/leaveall - to leave all group
7.) **/define - to use dictionary
8.) **/github - to check github account 
9.) **/info - to get information about someone
10.) **/paste - to paste logs and documents files
11.) **/tgm - To make telegraph link
12.) **/wall - To previous wallpaper
13.) **/whatanime - To check anime

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @Murat_30_God***""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ℹ️ Command Menu

🤷 » /id - To get user id
🤷 » /uptime - To check uptime
🤷 » /relaod - To reload the bot
👩🏻‍💼 » /tm - to get telegraph img link
🤷 » /ping - To check server
🤷 » /stop - To stop the music
🤷 » /pause - To pause the music
🤷 » /resume - To resume the music
🤷 » /mute - To mute in vc
🤷 » /unmute - To unmute in vc
🤷 » /volume - To change the volume
🤷 » /rmd,clear - To delte all download file
🤷 » /rmw,clean - To delte all Raw download file
🤷 » /cleanup -To clean database
🤷 » /song - To get a song
🤷 » /vsong - To get a video song
🤷 » /lyric - To get lyrics to any song
🤷 » /search - To search an song
👩🏻‍🤷 »   » /q - to get reply message in stickers
👩🏻‍🤷 »  » /speedtest - To get Speedtest 
👩🏻🤷 »  » /play - Type this with give the song title or youtube link or audio file to play Music.
👩🤷 »   » /vplay - Type this with give the song title or youtube link or video file to play Video. 
👩🤷 »  » /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video.
🤷🤷 » » /skip - To Skip current song
🤷🤷 » » /repo - To get the repo of Music-Music
🙋🤷 » » /end - To end play song in vc.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
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
