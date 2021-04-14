#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]
s_channel = os.environ["S_CHANNEL_ID"]
t_group = int(os.environ["TGP_USERNAME"])

start_img = "https://telegra.ph/file/bf15b6794e857518655d9.jpg"

cyp = Client(
    'cyp_bot',
    api_id=api_id, 
    api_hash=api_hash, 
    bot_token=bot_token
)
print("bot starting")

@cyp.on_message(filters.command(['start']) & filters.private)
def start(client, message):
    message.reply_photo(start_img, caption= "💣 അധോലോകം💣",
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


@cyp.on_message(filters.video & filters.chat(t_group))
def video_filter(client, message):
    chat_id = message.chat.id
    video_id = message.message_id
    #============================ main()
    message.copy(chat_id=s_channel, caption= "@neela_kkuyil")
    #============================ done()
    time.sleep(30)
    cyp.delete_messages(chat_id=chat_id, message_ids=video_id)
    return

@cyp.on_message(filters.photo & filters.chat(t_group))
def pic_filter(client, message):
    chat_id = message.chat.id
    pic_id = message.message_id
    #============================ main()
    message.copy(chat_id=s_channel, caption= "@neela_kkuyil")
    #============================ done()
    time.sleep(30)
    cyp.delete_messages(chat_id=chat_id, message_ids=pic_id)
    return

@cyp.on_message(filters.document & filters.chat(t_group))
def doc_filter(client, message):
    chat_id = message.chat.id
    doc_id = message.message_id
    #============================ main()
    message.copy(chat_id=s_channel, caption= "@neela_kkuyil")
    #============================ done()
    time.sleep(30)
    cyp.delete_messages(chat_id=chat_id, message_ids=doc_id)
    return

cyp.run()
