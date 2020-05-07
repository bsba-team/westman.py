from core import bot


def _exit():
    @bot.message_handler(commands=['exit'])
    def __exit(message):
        bot.stop_polling()
        bot.stop_bot()
        exit(1)
        pass
