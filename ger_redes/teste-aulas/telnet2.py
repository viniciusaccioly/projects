import getpass
import telnetlib
import time
from pysnmp.hlapi import *

switches = ["192.168.0.111", '192.168.0.112', '192.168.0.113', '192.168.0.114']
vlans= ([2, 'Alunos'], [3, 'Professores'], [4, 'Tecnicos'])

user = input("Digite o seu usuario: ")
password = getpass.getpass()

# Selecionando o switches
for switch in switches:
    tn = telnetlib.Telnet(switch)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    # Configurando as VLANS     
    for vlan in vlans:
        tn.write(b"enable\n")
        tn.write(b"conf t\n")
        tn.write(b"vlan " + str(vlan[0]).encode('ascii') + b"\n")
        tn.write(b"vlan " + str(vlan[1]).encode('ascii') + b"\n")
        tn.write(b"exit\n")
        tn.write(b"do wr\n")
        tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    time.sleep(5)

# Configurando SNMP no roteadores
router=([100,"192.168.0.101","R1"], [101,'192.168.0.102',"R2"], [103,"192.168.0.103","R3"])

for rt in router:
    tn = telnetlib.Telnet(rt[1])
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    out = "snmp-server community " + rt[0] + " rw\n"
    tn.write(b"conf t\n")
    tn.write(out.encode('ascii'))
    tn.write(b"do wr\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))

while True:
    for rt in router:

        iterator = getCmd(
        SnmpEngine(),
        CommunityData(rt[0]),
        UdpTransportTarget((rt[1], 161)),
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
                print(rt[2] + ' -- ' + value[1])
    time.sleep(10)