import telegram
from email import message
import time
from telegram import Update
from cabecalho import *

#bot = telegram.Bot(token=api_key)
#bot.send_message(chat_id=user_id, text='Python e telegram!')
#message = "Hello, " + update.message.from_user.first_name
#bot.send_message(chat_id=update.message.chat_id, text=message)

from telegram.ext import Updater
updater = Updater(token=api_key)
dispatcher = updater.dispatcher

def start(bot, update):
    message = "Hello, " + Update.message.from_user.first_name
    bot.send_message(chat_id=Update.message.chat_id , text=message )



from telegram.ext import CommandHandler

start_handler = CommandHandler("start", start)
# create a CommandHandler that responds to the command "/start" and runs the function start
dispatcher.add_handler(start_handler)
# add this handler to the dispatcher
def echo(bot, update):
    bot.send_message(chat_id=user_id, text=update.message.text)
    # text = update.message.text here because we want to retrieve the text from the original message and send the same thing back

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
# instead of a string to specify a command name, now we use Filters.text to filter out all text based messages
dispatcher.add_handler(echo_handler)

food_list = ["fish", "rice", "sushi"]

def find_food(bot, update):
    words = update.message.text.split()
    for i in words:
        if i in food_list:
            bot.send_message(chat_id=user_id, text="FOOD!!")




updater.start_polling()
time.sleep(20)
updater.stop()