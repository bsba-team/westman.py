import random

from core import bot
from config import CONFESSION, DIALOG, PERSON, CONTENT


def _photo():
    @bot.message_handler(content_types=['photo'])
    def __photo(message):
        bot.reply_to(message, "<b>Photo Received</b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        content = f"<b>{random.choice(PERSON)} {random.choice(CONTENT)}.</b>"
        bot.send_photo(CONFESSION, downloaded_file, caption=content, parse_mode='HTML')
        reply = "<b>Photo has been sent to the confession! Check the channel</b>"
        bot.send_message(message.from_user.id, reply, parse_mode='HTML')
        pass
    pass
