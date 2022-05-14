import getpass
import telnetlib

HOST = "192.168.122.239"
user = input("Digite o seu usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Confugurando ip interface loopback

tn.write(b"conf t\n")
tn.write(b"int loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
#tn.write(b"end\n")
tn.write(b"exit\n")

# Configurando snmp-server 

community = input("Digite o nome da comunidade: ")
out = "snmp-server community " + community + " rw\n"

#tn.write(b"conf t\n")
tn.write(out.encode('ascii'))
tn.write(b"do wr\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

