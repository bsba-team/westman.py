from core import bot


def _document():
    @bot.message_handler(content_types=['document'])
    def __document(message):
        reply = "Document type object not implemented yet... \n" \
                "It may be supported in future releases. Stay stunned!"
        bot.send_message(message.from_user.id, reply)
        pass
