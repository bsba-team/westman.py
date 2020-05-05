import random

from core import bot
from config import CONFESSION, PERSON, CONTENT


def _photo():
    @bot.message_handler(content_types=['photo'])
    def __photo(message):
        bot.reply_to(message, "<b>Photo Received</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        content = f"<b>{random.choice(PERSON)} {random.choice(CONTENT)}.</b>"
        bot.send_photo(
            chat_id=CONFESSION,
            photo=message.photo[-1].file_id,
            caption=content,
            parse_mode='HTML',
        )
        reply = "<b>Photo has been sent to the confession! Check the channel</b>"
        bot.reply_to(message, reply, parse_mode='HTML')
        pass
    pass
