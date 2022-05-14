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


# Configurando snmp-server 

community = input("Digite o nome da comunidade: ")
out = "snmp-server community " + community + " rw\n"


tn.write(b"conf t\n")
tn.write(out.encode('ascii'))
tn.write(b"do wr\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

enable
conft
int g0/0
ip addr dhcp
no shut
end
conf t
username vinicius priv 15 secret accioly
line vty 0 4
login local
transport input all