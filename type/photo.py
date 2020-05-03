from core import bot


def _photo():
    @bot.message_handler(content_types=['photo'])
    def __photo(message):
        reply = "Photo type object not implemented yet... \n" \
                "It may be supported in future releases. Stay stunned!"
        bot.send_message(message.from_user.id, reply)
        pass
    pass
