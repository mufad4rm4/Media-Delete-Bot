#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
import time
import random
import os
import asyncio
import heroku3

# api_id = int(os.environ["API_ID"])
# api_hash = os.environ["API_HASH"]
# bot_token = os.environ["BOT_TOKEN"]

dtime = ['15']
cdtime = ['1800']
admins = []
media_channel = -1001390839405 
bk_channel = -1001298814143

heroku_conn = heroku3.from_key('ba75da2d-8fa5-4f35-b9ec-75e5352bb438')
happ = heroku_conn.apps()['fierce-cliffs-61294']


start_img = [
    "https://telegra.ph/file/bf15b6794e857518655d9.jpg",
    "https://telegra.ph/file/5b0406dd7b743de513c46.jpg",
    "https://telegra.ph/file/5c91495538b0c78af8afe.jpg"]

cyp = Client(
    'cyp_bot',
    api_id=1280226, 
    api_hash='40c6be639fd3e699783cbb43c511cef0', 
    bot_token='1756158596:AAG3nIW1Nce_Uafvf10gejRR7bag0hw0edo'
)
print("bot starting")

@cyp.on_message(filters.command(['start']) & filters.private)
def start(client, message):
    message.reply_photo(photo=random.choice(start_img),
                        caption= "💣 അധോലോകം💣",
                        reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Join Now",url="https://t.me/Adholokam_Official")]])
                        )

    return

@cyp.on_message(filters.photo | filters.video | filters.document)
async def media_files(client, message):
    chat_id = message.chat.id
    video_id = message.message_id
    c = await message.copy(media_channel)
    await message.copy(bk_channel)
    for ct in cdtime:
        await asyncio.sleep(int(ct))
        await cyp.delete_messages(media_channel, message_ids=c.message_id)
    for t in dtime:
        await asyncio.sleep(int(t))
    try:
        await cyp.delete_messages(chat_id=chat_id, message_ids=video_id)
    except FloodWait as e:
        time.sleep(e.x)
        await cyp.delete_messages(chat_id=chat_id, message_ids=video_id)
        
    return

@cyp.on_message(filters.command('st') & filters.group)
def set_time(__, message):
    user_id = message.from_user.id
    for member in cyp.get_chat_members(chat_id=message.chat.id, filter="administrators"):
        admin = member.user.id
        admins.append(admin)
    if user_id in admins:

        try:
            time = message.text.split()[1]
            print(time)
        except Exception:
            message.reply_text("pass time in seconds eg: 1-60")
            
        if int(time) > 60:
            message.reply_text(f"Max time time 60s, You entered {time}s.")
            return
        else:
            message.reply_text(f"Medias will be deleted after {time}s.")
            dtime.clear()
            dtime.append(time)
            admins.clear()
    else:
        message.reply_text("This Command only for admins")
    admins.clear()
    
@cyp.on_message(filters.command('cst') & filters.group)
def set_time(__, message):
    user_id = message.from_user.id
    for member in cyp.get_chat_members(chat_id=message.chat.id, filter="administrators"):
        admin = member.user.id
        admins.append(admin)
    if user_id in admins:

        try:
            time = message.text.split()[1]
            print(time)
        except Exception:
            message.reply_text("pass time in seconds eg: 1-3600")
            
        if int(time) > 3600:
            message.reply_text(f"Max time time 3600s, You entered {time}s.")
            return
        else:
            message.reply_text(f"Medias will be deleted after {time}s.")
            cdtime.clear()
            cdtime.append(time)
            
    else:
        message.reply_text("This Command only for group admins")
    admins.clear()
        
@cyp.on_message(filters.command('restart') & filters.group)
def  hrestart(client, message):
    user_id = message.from_user.id
    for member in cyp.get_chat_members(chat_id=message.chat.id, filter="administrators"):
        admin = member.user.id
        admins.append(admin)
    if user_id in admins: 
        msg = message.reply_text("Restarting ..")
        try:
            happ.restart()
            admins.clear()
        except Exception:
            msg.edit("failed to restart")
            admins.clear()
        
cyp.run()
