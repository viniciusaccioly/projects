from cabecalho import *
import telegram
import requests
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
                   resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                   self.responder(resposta,chat_id)

    # obter mensagens
    def obter_mensagens(self,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
    #def criar_resposta(self):
        mensagem = mensagem['message']['text']
        if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
            return f'''Digite o numero do Hamburguer que gostaria de pedir{os.linesep}1- Queijo MAX{os.linesep}2- Duplo Burguer{os.linesep}3- Triple XXX'''
        if mensagem == '1':
            return f'''Queijo MAX - R$ 20,00 {os.linesep}Confirmar Pedido(s/n)'''
        if mensagem == '2':
            return f'''Duplo Burguer - R$ 30,00 {os.linesep}Confirmar Pedido(s/n)'''
        if mensagem == '3':
            return f'''Triple XXX - R$ 40,00 {os.linesep}Confirmar Pedido(s/n)'''
        
        if mensagem.lower() in ('s', 'sim'):
            return f'''Pedido confirmado com Sucesso! O pedido está sendo preparado e logo saira para entrega.{os.linesep} SÓ AGUARDAR ESFOMEADO!!'''
        else:
            return f'Olá, Bem vindo a Atend Tecnologia!{os.linesep}Gostaria de acessar o menu? Digite "menu"'
            
            
    # Responder
    def responder(self, resposta,chat_id):
        #enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)

bot = TelegBot()
bot.iniciar()