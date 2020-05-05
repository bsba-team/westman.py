import random

from core import bot
from config import CONFESSION, CONTENT, PERSON


def _document():
    @bot.message_handler(content_types=['document'])
    def __document(message):
        bot.reply_to(message, "<b>Document Received</b>", parse_mode='HTML')
        content = f"<b>{random.choice(PERSON)} {random.choice(CONTENT)}.</b>"
        bot.send_document(
            chat_id=CONFESSION,
            data=message.document.file_id,
            caption=content,
            parse_mode='HTML',
        )
        reply = "<b>Document has been sent to the confession! Check the channel</b>"
        bot.reply_to(message, reply, parse_mode='HTML')
        pass
    pass
