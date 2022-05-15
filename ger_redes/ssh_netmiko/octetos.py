from pysnmp.hlapi import *
import time
# criar um loop que fica consultando a quantidade de 
# octetos que saíram e a quantidade de octetos que entraram na porta G0/0

router=[('192.168.122.101','r1'), ('192.168.122.102','r2'), ('192.168.122.103','r3')]
while True:
    print("_"*20)
    for routes in router:
        
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(str(routes[1])),
            UdpTransportTarget((str(routes[0]), 161)),
            ContextData(),
            ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets', 1)),
            ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets', 1))
            
        )
       
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            print(errorIndication)

        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            
            for varBind in varBinds:
               value = [x.prettyPrint() for x in varBind]
            
            print(routes[1] + ' = in' + ': '+ str(varBinds[1][1]) + ' out' + ': ' + str(varBinds[0][1]))
 
        time.sleep(10)

"""
R1 = in : 100
R2 = in : 132
R3 = in : 112
============
out :120
out :133
out :111
"""
