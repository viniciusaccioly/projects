#!/bin/bash
sudo apt install vim screen htop cmake

#Intalar o ambiente em python
sudo apt install virtualenv python-all-dev python3-pip python-pip


#Intalar a biblioteca CoAP em python

sudo pip3 install aiocoap

#Para executar o servidor CoAP

#sudo pip install dtls
sudo pip3 install python3-dtls
sudo pip3 install coapthon


# Entrar no /usr/local/lib/python3.X/dist-packages/aiocoap/util/asyncio/recvmsg.py 
# e comentar a função "del"  na linha 96
#    def __del__(self):
#        if self.__sock is not None:
#            self.close()


#https://meet.google.com/bfa-ompz-ubk

#https://github.com/chrysn/aiocoap link  a mais
https://aiocoap.readthedocs.io/en/latest/installation.html

apt install python3-dev build-essential autoconf
ade "git+https://github.com/chrysn/aiocoap#egg=aiocoap[all]"




#DTLS
pip3 install --upgrade "aiocoap[all]"
git clone https://github.com/chrysn/aiocoap
cd aiocoap
pip3 install --upgrade ".[all,docs]"
ip3 install --upgr