#!/bin/bash
sudo apt install vim screen htop cmake

#Intalar o ambiente em python
sudo apt install virtualenv python-all-dev python3-pip

#Intalar a biblioteca CoAP em python

sudo pip3 install aiocoap

#Para executar o servidor CoAP

#sudo pip install dtls
sudo pip3 install python3-dtls coapthon


# Entrar no  /usr/local/lib/python3.10/dist-packages/aiocoap/util/asyncio/recvmsg.py 
# e comentar a função "del"  na linha 96
#    def __del__(self):
#        if self.__sock is not None:
#            self.close()


#https://meet.google.com/bfa-ompz-ubk