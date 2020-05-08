import telebot
import config
import logging
import time
import flask


API_TOKEN = config.TOKEN
WEBHOOK_HOST = '13.82.27.181'
WEBHOOK_PORT = 80  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % API_TOKEN


bot = telebot.TeleBot()
logger = telebot.logger.setLevel(logging.INFO)
app = flask.Flask(__name__)


def host():
    logger()

    @app.route('/', methods=['GET', 'HEAD'])
    def index():
        return ''

    @app.route(WEBHOOK_URL_PATH, methods=['POST'])
    def webhook():
        if flask.request.headers.get('content-type') == 'application/json':
            json_string = flask.request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            flask.abort(403)

    bot.remove_webhook()
    time.sleep(0.1)
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
    app.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT, debug=True)


def launch():
    host()
