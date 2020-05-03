from core import bot
from config import CONFESSION


def _echo():
    @bot.message_handler(commands=['echo'])
    def __echo(message):
        sender = message.from_user.first_name
        _message = message.text[6:]
        content = \
            f"<b>ATTENTION!</b> \n" \
            f"<i>{_message}</i>"
        pm = bot.send_message(CONFESSION, content, parse_mode='HTML')
        bot.pin_chat_message(CONFESSION, pm.message_id)
        pass
