#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
import time
import random
import os
import asyncio

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

time = []
admins = []

start_img = [
    "https://telegra.ph/file/bf15b6794e857518655d9.jpg",
    "https://telegra.ph/file/5b0406dd7b743de513c46.jpg",
    "https://telegra.ph/file/5c91495538b0c78af8afe.jpg"]

cyp = Client(
    'cyp_bot',
    api_id=api_id, 
    api_hash=api_hash, 
    bot_token=bot_token
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

    await asyncio.sleep(15)
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
        message.reply_text("ok good. pass time in seconds")
        
    
cyp.run()
