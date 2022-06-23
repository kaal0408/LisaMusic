from pyrogram import filters
import pytgcalls
from Process.main import bot 

calls = pytgcalls.GroupCallFactory(musicbot).get_group_call()


@bot.on_message(filters.command('leavevc'))
async def leavevc(_, message):
    await calls.stop()
    await calls.leave_current_group_call()



