import pip._internal as packager

try:
    import telebot
except ImportError:
    packager.main(['install', 'pyTelegramBotAPI'])
    pass
import config
import logging
import time
import os


from flask import Flask, request


bot = telebot.TeleBot(config.TOKEN)
logger = telebot.logger
server = Flask(__name__)


def localhost():
    logger.setLevel(logging.DEBUG)
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=0)
        except:
            time.sleep(10)
        pass
    pass


def hosting():
    @server.route('/' + config.TOKEN, methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    pass

    @server.route('/')
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url=config.APPLICATION + config.TOKEN)
        return "!", 200
    pass

    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


def launch():
    if config.PRODUCTION is True:
        hosting()
    else:
        localhost()
    pass
