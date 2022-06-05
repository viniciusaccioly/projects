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

sudo ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /usr/lib/libcrypto.so.1.0.0