import napalm

def get_down_interface(interfaces):
    if_down = []
    for int in interfaces:
        if interfaces[int]['is_up'] == False:
            if_down.append(int)
    if len(if_down) > 0:
        print(f'Interfaces desabilidatas: {len(if_down)}')
        for i in range(len(if_down)):
            print(f"{if_down[i]}")
def get_velocidade(interfaces):
    speed= []
    for inte in interfaces:
        speed.append(interfaces[inte]['speed'])

    for x in speed:
        if x == 1000.0:
            return 'Interfces com mesma velocidade em Mbits'
        else:
            return 'Interfces com velocidade diferentes em Mbits'
def get_mac_mtu(interfaces):
    for int in interfaces:
        print(f"{int}\tMac: {interfaces[int]['mac_address']}\t Mtu: {interfaces[int]['mtu']} ")


driver = napalm.get_network_driver("ios")
# Connect :
R1 = driver(
    hostname="192.168.122.101",
    username="vinicius",
    password="melo",
    optional_args={"port": 22},
)

R2 = driver(
    hostname="192.168.122.102",
    username="vinicius",
    password="melo",
    optional_args={"port": 22},
)

R3 = driver(    hostname="192.168.122.103",
    username="vinicius",
    password="melo",
    optional_args={"port": 22},
)
dispositivos = ['R1', 'R2', 'R3']
roteadores = [R1, R2,R3]
for x in range(len(roteadores)):
    print(f'Iniciando router {dispositivos[x]}')
    roteadores[x].open()
    output = roteadores[x].get_interfaces()
    get_down_interface(output)
    print(get_velocidade(output))
    get_mac_mtu(output)
    print('-' * 40,"\n")
