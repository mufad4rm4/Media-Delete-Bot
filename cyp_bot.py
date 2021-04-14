#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import random
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]
s_channel = os.environ["S_CHANNEL_ID"]
sc_channel = int(os.environ["SEC_CHANNEL_ID"])

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
    message.reply_photo(photo=random.choice(start_img), caption= "💣 അധോലോകം💣",
                     reply_markup=InlineKeyboardMarkup(

                            [
                                [  # First row
                                    InlineKeyboardButton(  # Generates a callback query when pressed
                                        "Join Now",
                                        url="https://t.me/Adholokam_Official"
                                    )
                                ]
                            ]
                        )
                        )


    return


@cyp.on_message(filters.photo | filters.video | filters.document)
def video_filter(client, message):
    chat_id = message.chat.id
    video_id = message.message_id
    #============================ main()
    first = message.copy(chat_id=s_channel, caption= "@neela_kkuyil")
    second = message.copy(chat_id=sc_channel, caption= "@neela_kkuyil")
    #============================ done()
    time.sleep(15)
    cyp.delete_messages(chat_id=chat_id, message_ids=video_id)
    time.sleep(3570)
    first.delete()
    return

cyp.run()
