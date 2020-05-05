import random

from core import bot
from config import CONFESSION, CONTENT, PERSON


def _audio():
    @bot.message_handler(content_types=['audio'])
    def __audio(message):
        bot.reply_to(message, "<b>Audio Received</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        fileID = message.audio.file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        content = f"<b>{random.choice(PERSON)} {random.choice(CONTENT)}.</b>"
        bot.send_audio(
            CONFESSION,
            downloaded_file,
            title=message.audio.title,
            performer=message.audio.performer,
            caption=content,
            parse_mode='HTML')
        reply = "<b>Audio has been sent to the confession! Check the channel</b>"
        bot.send_message(message.from_user.id, reply, parse_mode='HTML')
    pass
