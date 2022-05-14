import telnetlib
from paramiko import HostKeys
from pysnmp.hlapi import *
import getpass

switches = ['192.168.122.111', '192.168.122.112', '192.168.122.113', '192.168.122.114']
vlans= [(2, 'Alunos'), (3, 'Professores'), (4, 'Tecnicos')]
user = input("Digite o seu usuario: ")
password = getpass.getpass()
# Selecionando o switches
count=1
for switch in switches:
    tn = telnetlib.Telnet(switch)
    tn.write(user.encode('ascii') + b"\n")
    tn.write(password.encode('ascii') + b"\n")
    
    # Configurando as VLANS
    for vlan in vlans:
        tn.write(b"enable\n")
        tn.write(b"conf t\n")
        tn.write(b"hostname sw" +str(count).encode('ascii') + b'\n')   
        tn.write(b"vlan " + str(vlan[0]).encode('ascii') + b'\n')
        tn.write(b"name " + str(vlan[1]).encode('ascii') + b'\n')
        tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    count+=1
    print(tn.read_all().decode('ascii'))
    