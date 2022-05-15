from netmiko import ConnectHandler
from pysnmp.hlapi import *
import time


# 4 Automação da Criação de VLANs com Netmiko
vlans= [(2, 'Alunos'), (3, 'Professores'), (4, 'Tecnicos')]

SW1 = {
'device_type': 'cisco_ios',
'host': '192.168.122.111',
'username': 'vinicius',
'password': 'melo',
}

SW2 = {
'device_type': 'cisco_ios',
'host': '192.168.122.112',
'username': 'vinicius',
'password': 'melo',
}

SW3 = {
'device_type': 'cisco_ios',
'host': '192.168.122.113',
'username': 'vinicius',
'password': 'melo',
}
SW4 = {
'device_type': 'cisco_ios',
'host': '192.168.122.114',
'username': 'vinicius',
'password': 'melo',
}

for switches in (SW1, SW2, SW3,SW4):
    connect = ConnectHandler(**switches)
    for vlan in vlans:
        cfg_list = [
        "vlan " + str(vlan[0]),
        "name " + str(vlan[1]),
        ]
        cfg_output = connect.send_config_set(cfg_list)
        print(cfg_output)
connect.save_config()
print(connect.find_prompt())
connect.disconnect()

# 5 Script para Habilitação do SNMP em todos os Roteadores
# Conecanto com varios HOST

R1 = {
'device_type': 'cisco_ios',
'host': '192.168.122.101',
'username': 'vinicius',
'password': 'melo',
}

R2 = {
'device_type': 'cisco_ios',
'host': '192.168.122.102',
'username': 'vinicius',
'password': 'melo',
}

R3 = {
'device_type': 'cisco_ios',
'host': '192.168.122.103',
'username': 'vinicius',
'password': 'melo',
}

router=[('192.168.122.101','r1'), ('192.168.122.102','r2'), ('192.168.122.103','r3')]
count=1
for routers in (R1, R2, R3):
    connect = ConnectHandler(**routers)
    cfg_list = [
       "snmp-server community r" + str(count) + " rw",
        ]
    cfg_output = connect.send_config_set(cfg_list)
    print(cfg_output)
    count+=1
connect.save_config()
print(connect.find_prompt())
connect.disconnect()

# 5.1 criar um loop que fica consultando a quantidade de 
# octetos que saíram e a quantidade de octetos que entraram na porta G0/0
"""
R1 = in : 100 out :120
R2 = in : 132 out :133
R3 = in : 112 out :111
============
"""

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


