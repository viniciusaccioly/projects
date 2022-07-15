#Open VPN
ip_servidor=10.0.0.1
ip_cliente=10.0.0.2


#Pratica 1 : Openvpn  - sem segurança
#(Servidor e Cliente)

sudo apt install Openvpn
sudo modprobe tun

# Adiciona linha "tun" no final do arquivo "/etc/modules" para que o modulo passe a ser carregado automaticamente durante o boot
# 
sudo echo tun >> /etc/modules

#Pratica 2 : Openvpn  - tunel com chave estatica

sudo /etc/openvpn
sudo openvpn --genkey --secret static.key

# Servidor
# No arquivo "/etc/openvpn/server.conf" adicionar o seguinte conteudo

dev tun 
ifconfig $ip_servidor $ip_cliente
secret static.key

# Cliente
# No arquivo "/etc/openvpn/client.conf" adicionar o seguinte conteudo

remote 192.168.1.101
dev tun 
ifconfig $ip_cliente $ip_servidor
secret static.key


sudo openvpn --config /etc/openvpn/client.conf
sudo openvpn --config /etc/openvpn/server.conf

Ou 
sudo /etc/init.d/openvpn restart