import random

from core import bot
from config import CONFESSION, DIALOG, PERSON


def _sticker():
    @bot.message_handler(content_types=['sticker'])
    def __sticker(message):
        bot.send_sticker(
            chat_id=CONFESSION,
            data=message.sticker.file_id,
        )
        reply = "<b>Photo has been sent to the confession! Check the channel</b>"
        bot.reply_to(message, reply, parse_mode='HTML')
        pass
    pass
