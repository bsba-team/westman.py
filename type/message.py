import random

from core import bot
from config import CONFESSION, DIALOG, PERSON


def _message():
    @bot.message_handler(func=lambda message: True)
    def __message(message):
        content = \
            f"#{message.message_id} \n" \
            f"<b>{random.choice(PERSON)} {random.choice(DIALOG)}:</b> <i>" + message.text + "</i>"
        bot.send_message(CONFESSION, content, parse_mode='HTML')
        pass
    pass
