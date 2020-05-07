from core import bot


def _help():
    @bot.message_handler(commands=['help'])
    def __help(message):
        instructions = \
            "<b>This is the list of available commands:</b> \n" \
            "/help - <code>Show this mesage</code> \n" \
            "/echo - <code>Announce an important message</code> \n" \
            "/prod - <code>Production funds of this project</code> \n" \
            "/source - <code>Source code of this project</code> \n" \
            "\n" \
            "<i>In order to send messages, start writing to me as you do in pms with people. " \
            "Send me videos, gifs, sticker and photos and I'll deliver them to our confession!</i>"
        bot.send_message(message.from_user.id, instructions, parse_mode='HTML')
        pass
    pass
