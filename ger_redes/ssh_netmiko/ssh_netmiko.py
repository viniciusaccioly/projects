from netmiko import ConnectHandler

R1 = {
" device_type " : " cisco_ios " ,
" host " : " 192.168.122.101 " ,
" username " : "vinicius" ,
" password " : "melo" ,
}

connect = ConnectHandler(**R1)
output = connect.send_command(" show ip interface brief")
print(output)