import getpass
import telnetlib
import time
from pysnmp.hlapi import *

user = input("Digite o seu usuario: ")
password = getpass.getpass()

router=[('192.168.122.101','R1'), ('192.168.122.102','R2'), ('192.168.122.103','R3')]

# Configurando SNMP no roteadores
for rt in router:
    tn = telnetlib.Telnet(rt[0])
    tn.write(user.encode('ascii') + b"\n")
    tn.write(password.encode('ascii') + b"\n")  
    out = "snmp-server community " + rt[1] + " rw\n"
    tn.write(b"conf t\n")
    tn.write(out.encode('ascii'))
    tn.write(b"do wr\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    
# Coletando dados das interfaces
while True:
    for rt in router:

        iterator = getCmd(
        SnmpEngine(),
        CommunityData(rt[1]),
        UdpTransportTarget((rt[0], 161)),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.1'))
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
                print(rt[1] + ' -- ' + value[1])
    print('\n')
    time.sleep(10)