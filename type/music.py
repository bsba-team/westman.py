from core import bot


def _music():
    @bot.message_handler(content_types=['audio'])
    def __music(message):
        reply = "Music type object not implemented yet... \n" \
                "It may be supported in future releases. Stay stunned!"
        bot.send_message(message.from_user.id, reply)
