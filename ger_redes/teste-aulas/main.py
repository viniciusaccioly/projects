from pysnmp.hlapi import *
import time

valor_lido=0
media=0
cont=1
while True:
    iterator = getCmd(
        SnmpEngine(),
        UsmUserData('vinicius', '12345678', '12345678'),
        UdpTransportTarget(('127.0.0.1', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets', 1))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
       
        for varBind in varBinds:
            valor_lido=[x.prettyPrint() for x in varBind]
            valor_lido=int(valor_lido[1])
                
        media = media + valor_lido / cont
        media_acrescimo = media + (media * (10 / 100))
        
        if valor_lido > media_acrescimo:
            print ("Valor lido: ", valor_lido,"Media:", media,  " Trafego excede limite!")
            
            
        else:
            print ("Valor lido: ", valor_lido ,"Media:", media)

        cont += 1
        time.sleep(10)
