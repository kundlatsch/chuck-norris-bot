import requests
import json
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def get_phrase():
	API_TOKEN = os.getenv('API_TOKEN')
	url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

	headers = {
    		'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
    		'x-rapidapi-key': API_TOKEN,
    		'accept': "application/json"
    	}

	response = requests.request("GET", url, headers=headers)

	json_response = json.loads(response.text)
	phrase = json_response["value"]

	return phrase

def start(update, context):
        update.message.reply_text("Hello there.")

def help(update, context):
        update.message.reply_text('Get random Chuck Norris facts jokes using this bot! Commands:'
                                  '\n/start - Start bot.'
                                  '\n/help - Get help.'
                                  '\n/procurar - Pick a random joke.')

def joke(update, context):
        phrase = get_phrase()
        update.message.reply_text(phrase)

if __name__ == '__main__':
	TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
	updater = Updater(TELEGRAM_TOKEN, use_context=True)

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("joke", joke))
	
    PORT = os.getenv('PORT')
	HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
	updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TELEGRAM_TOKEN)
	updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TELEGRAM_TOKEN))
