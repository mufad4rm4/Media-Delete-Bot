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
t_group = os.environ["TGP_USERNAME"]

start_img = "https://telegra.ph/file/bf15b6794e857518655d9.jpg"

cyp = Client(
    'cyp_bot',
    bot_token,
    api_id,
    api_hash,
)
print("bot starting")

s_channel = "1445436774"

@cyp.on_message(filters.command(['start']))
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
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    video_id = message.message_id
    #============================ main()
    message.copy(s_channel, caption= "@neela_kkuyil")
    #============================ done()
    cyp.send_chat_action(chat_id=t_group, action= "typing")
    cyp.delete_messages(chat_id=chat_id, message_ids=video_id)
    cyp.send_message(chat_id=t_group, text=f"{mention} you're video successfully added to our channel.")

    return

cyp.run()
