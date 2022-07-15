import telegram
import os

api_key = '5367726074:AAH2d2dZejyvQB557mbg3akYLM9mHcUOWtc'
user_id = '532612155'

bot = telegram.Bot(token=api_key)
bot.send_message(chat_id=user_id, text='Bom dia , seja bem vindo ao suporte da Atend Tecnologia. Sou o atendente virtual J.J,{os.linesep} Em que posso te ajudar? BY: ACCIOLY')