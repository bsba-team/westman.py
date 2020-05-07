import re

from core import bot
from better_profanity import profanity
from config import CONFESSION, OFFENSIVE


def cleaner(string):
    for badword in OFFENSIVE:
        string = string.replace(badword, "*"*len(badword))
    return string
    pass


def _message():
    @bot.message_handler(func=lambda message: True)
    def __message(message):
        url_pattern = r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(
        \([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])) '''
        censored = cleaner(profanity.censor(message.text))
        result = re.sub(url_pattern, '', censored)
        content = \
            f"#{message.message_id}: <i>" + result + "</i>"
        bot.send_message(CONFESSION, content, parse_mode='HTML')
        pass
    pass
