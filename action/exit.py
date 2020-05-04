from core import bot


def _exit():
    @bot.message_handler(commands=['exit'])
    def __exit(message):
        exit(1)
        pass
