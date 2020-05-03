from core import bot


def _video():
    @bot.message_handler(content_types=['video'])
    def __video(message):
        reply = "Video type object not implemented yet... \n" \
                "It may be supported in future releases. Stay stunned!"
        bot.send_message(message.from_user.id, reply)