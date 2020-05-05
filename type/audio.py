import random

from core import bot
from config import CONFESSION, CONTENT, PERSON


def _audio():
    @bot.message_handler(content_types=['audio'])
    def __audio(message):
        bot.reply_to(message, "<b>Audio Received</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        content = f"<b>{random.choice(PERSON)} {random.choice(CONTENT)}.</b>"
        bot.send_audio(
            chat_id=CONFESSION,
            audio=message.audio.file_id,
            title=message.audio.title,
            performer=message.audio.performer,
            caption=content,
            parse_mode='HTML')
        reply = "<b>Audio has been sent to the confession! Check the channel</b>"
        bot.reply_to(message, reply, parse_mode='HTML')
    pass
