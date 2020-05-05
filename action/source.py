from core import bot
from telebot import types


def _keyboard():
    markup = types.InlineKeyboardMarkup()
    github = types.InlineKeyboardButton(text="GitHub", url="https://github.com/genemators/")
    repo = types.InlineKeyboardButton(text="Repository", url="https://github.com/genemators/westman/")
    markup.add(github, repo)
    return markup


def _source():
    @bot.message_handler(commands=['source'])
    def __source(message):
        source = "<b>[🤵‍‍] If you are experienced developer, contribute with me!</b>"
        bot.send_message(message.from_user.id, source, parse_mode='HTML', reply_markup=_keyboard())
    pass
