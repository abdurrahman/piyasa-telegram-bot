from flask import Flask, request, jsonify
from config import TELEGRAM_INIT_WEBHOOK_URL
from telegram_bot import TelegramBot

app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/webhook', methods=["POST"])
def index():
    req = request.get_json()
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    success=bot.action()
    return jsonify(success=success)

if __name__ == '__main__':
    app.run(5000)