from core import bot
from telebot import types


def _keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    automator = types.InlineKeyboardButton(text="Automator", url="https://github.com/genemators/automator")
    genoxs = types.InlineKeyboardButton(text="GenoXS", url="https://github.com/genemators/genoxs")
    remotely = types.InlineKeyboardButton(text="Remotely", url="https://github.com/genemators/remotely")
    markup.add(automator, genoxs, remotely)
    return markup


def _prod():
    @bot.message_handler(commands=['prod'])
    def __prod(message):
        source = "<b>[🤵] ‍Our very own projects that inspired and supported this one!</b>"
        bot.send_message(message.from_user.id, source, parse_mode='HTML', reply_markup=_keyboard())
    pass
