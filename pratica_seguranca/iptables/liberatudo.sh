#LIMPANDO AS CHAINS
iptatables -F
iptatables -F -t nat

#DEFINIR AS POLITICAS
iptatables -P INPUT ACCEPT
iptatables -P OUPUT ACCEPT
iptatables -P FORWARD ACCEPT