import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

# import callback functions
from main import (
    start,
    roli,
    toli,
    query,
)

app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return {'status': 200}

    elif request.method == 'POST':
        # get data from request
        data: dict = request.get_json(force=True)

        # convert data to Update obj
        update: Update = Update.de_json(data, bot)

        # Dispatcher
        dp: Dispatcher = Dispatcher(bot, None, workers=0)

        # handlers
        dp.add_handler(CommandHandler('start',start))
    
        dp.add_handler(CallbackQueryHandler(query))

        # process update
        
        dp.add_handler(MessageHandler(Filters.text('🛍 Videolar'),roli))
        dp.add_handler(MessageHandler(Filters.text('Rasmlar'),toli))
        dp.process_update(update=update)
        return {'status': 400}
# print(bot.setWebhook('https://muhammad001.pythonanywhere.com/'))