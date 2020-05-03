from core import bot


def _start():
    @bot.message_handler(commands=['start'])
    def __start(message):
        text = \
            "<b>Ladies and Gentlemen, welcome to my confession!</b> \n" \
            f"<i>Dear, {message.from_user.first_name}. Feel free to start " \
            "writing to me and I'll deliver your messages to our elegant confession...</i> \n" \
            "\n" \
            "<code>If you're having some trouble with me, just type </code>/help<code> " \
            "and I'll show you instructions!</code>"
        bot.send_message(message.from_user.id, text, parse_mode='HTML')
        pass
    pass
