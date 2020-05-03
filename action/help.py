from core import bot


def _help():
    @bot.message_handler(commands=['help'])
    def __help(message):
        instructions = \
            "<b>Let me show you some helpful tips to handle with me</b> \n" \
            "*"
        bot.send_message(message.from_user.id, instructions, parse_mode='HTML')
        pass
    pass
