from cabecalho import *
import requests
import time


while True:
    # Ler mensagens
    url_base = f'https://api.telegram.org/bot{api_key}/getUpdates'
    resultado = requests.get(url_base)
    # Imprimir Resultados
    print(resultado.json())
    time.sleep(10)


    #https://devaprender.com/como-criar-um-bot-no-telegram/