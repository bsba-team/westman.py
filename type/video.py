import random

from core import bot
from config import CONFESSION, PERSON, CONTENT


def _video():
    @bot.message_handler(content_types=['video'])
    def __video(message):
        bot.reply_to(message, "<b>Video Received</b>", parse_mode='HTML')
        content = f"<b>{random.choice(PERSON)} {random.choice(CONTENT)}.</b>"
        bot.send_video(
            chat_id=CONFESSION,
            data=message.video.file_id,
            caption=content,
            parse_mode="HTML")
        reply = "<b>Video has been sent to the confession! Check the channel</b>"
        bot.reply_to(message, reply, parse_mode='HTML')
    pass
