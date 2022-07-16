from cabecalho import *
import telegram
import requests
import time
import json
import os

class TelegBot:
    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot{api_key}/'
    # Iniciar o bot
    def iniciar(self):
        update_id = None
        while True:
           atualizacao = self.obter_mensagens(update_id)
           #print(atualizacao)
           mensagens = atualizacao['result']
           if mensagens:
               for mensagem in mensagens:
                   update_id = mensagem['update_id']
                   chat_id = mensagem['message']['from']['id']
                   eh_primeira_mensagem = mensagem['message']['message_id'] == 1
                   resposta = self.criar_resposta()
                   self.responder(resposta,chat_id)

    # obter mensagens
    def obter_mensagens(self,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    #def criar_resposta(self, mensagem, eh_primeira_mensagem):
    def criar_resposta(self):
        #if eh_primeira_mensagem == True:
        return '''Boa noite , seja bem vindo ao suporte da Atend Tecnologia. Sou o atendente virtual J.J,{os.linesp} Em que posso te ajudar? BY: ACCIOLY '''
    # Responder
    def responder(self, resposta,chat_id):
        #enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)

bot = TelegBot()
bot.iniciar()