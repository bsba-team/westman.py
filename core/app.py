import telebot
import config
import logging
import time


bot = telebot.TeleBot(config.TOKEN)
logger = telebot.logger


def localhost():
    logger.setLevel(logging.DEBUG)
    while True:
        try:
            bot.infinity_polling(True)
        except:
            time.sleep(10)
        pass
    pass


def launch():
    localhost()
