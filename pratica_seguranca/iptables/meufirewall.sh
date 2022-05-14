#LIMPANDO AS CHAINS
iptatables -F
iptatables -F -t nat

#DEFINIR AS VARIAVEIS
IP_LAN="192.168.0.0/24"
IP_DMZ="172.16.0.4/30"
IP_DNS="8.8.8.8"
IF_LAN="eth1"
IF_DMZ="eth2"
IF_INT="eth0"

#DEFINIR AS POLITICAS
iptatables -P INPUT DROP
iptatables -P OUPUT DROP
iptatables -P FORWARD DROP

"""Obs: É inidicado fazer nessa Ordem (interface, rede e protocolo)"""
#LIBERAR O TRAFEGO WEB DA LAN PARA A INTERNET (NAT)
iptables -t nat -A POSTROUTING -o $IF_INT -s $IP_LAN -j MASQUERADE

#LIBERAR ICMP DA LAN PARA INTERNET
iptables -t filter -A FORWARD -i $IF_LAN -o $IF_INT -s $IP_LAN -p icmp --icmp-type 8 -j ACCEPT
iptables -t filter -A FORWARD -i $IF_INT -o $IF_LAN -s $IP_LAN -p icmp --icmp-type 0 -j ACCEPT

#LIBERAR DNS DA LAN PARA INTERNET PORTA 53
iptables -t filter -A FORWARD -i $IF_LAN -o $IF_INT -s $IP_LAN -d $IP_DNS -p udp --dport 53 -j ACCEPT 
iptables -t filter -A FORWARD -i $IF_INT -o $IF_LAN -s $IP_LAN -s $IP_DNS -p udp --sport 53 -j ACCEPT

#LIBERAR WEB DA LAN PARA INTERNET
##PORTA 80
iptables -t filter -A FORWARD -i $IF_LAN -o $IF_INT -s $IP_LAN -p tcp --dport 80 -j ACCEPT 
iptables -t filter -A FORWARD -i $IF_INT -o $IF_LAN -s $IP_LAN -p tcp --sport 80 -j ACCEPT
##PORTA 443
iptables -t filter -A FORWARD -i $IF_LAN -o $IF_INT -s $IP_LAN -p tcp --dport 443 -j ACCEPT 
iptables -t filter -A FORWARD -i $IF_INT -o $IF_LAN -s $IP_LAN -p tcp --sport 443 -j ACCEPT

#LIBERAR O TRAFEGO WEB DA INTERNET PARA DMZ (DNAT)
iptables -t nat -A PREROUTING -i $IF_INT -p tcp --dport 80 -j DNAT --to 172.16.0.5

#LIBERAR PORTA 80 DA INTERNET PARA DMZ
iptables -t filter -A FORWARD -i $IF_INT -o $IF_DMZ -d $IP_DMZ -p tcp --dport 80 -j ACCEPT
iptables -t filter -A FORWARD -i $IF_DMZ -o $IF_INT -s $IP_DMZ -p tcp --sport 80 -j ACCEPT