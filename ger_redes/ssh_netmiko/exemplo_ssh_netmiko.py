from netmiko import ConnectHandler

# Conexão direta com apenas um HOST
R1 = {
'device_type': 'cisco_ios',
'host': '192.168.122.101',
'username': 'vinicius',
'password': 'melo',
}

connect = ConnectHandler(**R1)
output = connect.send_command("show ip interface brief")
print(output)

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

for routers in (R1, R2, R3):
    connect = ConnectHandler(**routers)
    print(connect.find_prompt())
    connect.disconnect()

print("Script finalizado!")

#3.2 -Lista de Comandos com Netmiko
SW1 = {
'device_type': 'cisco_ios',
'host': '192.168.122.111',
'username': 'vinicius',
'password': 'melo',
}

connect = ConnectHandler(**SW1)
cfg_list = [
    "vlan 3",
    "name Professor",
]
cfg_output = connect.send_config_set(cfg_list)
print(cfg_output)
connect.save_config()