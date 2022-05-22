from netmiko import ConnectHandler
<<<<<<< HEAD
sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.122.100',
    port = 22,
    username = 'cisco',
    password = 'cisco123!'
)
output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))

config_commands = [
    'int loopback 1',
    'ip add 10.1.1.1 255.255.255.0',
    'description [Vinicius Accioly]\'s loopback'
    ]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))

config_commands = [
    'int loopback 2',
    'ip add 10.1.1.1 255.255.255.0',
    'description [Vinicius Accioly]\'s loopback'
    ]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))
config_commands = [
    'int loopback 10',
    'ip add 10.10.1.1 255.255.255.0',
    'description [Vinicius Accioly]\'s loopback'
    ]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))
config_commands = [
    'int loopback 12',
    'ip add 10.12.1.1 255.255.255.0',
    'description [Vinicius Accioly]\'s loopback'
    ]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))
config_commands = [
    'int loopback 2',
    'ip add 10.1.1.1 255.255.255.0',
    'description [Vinicius Accioly]\'s loopback'
    ]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))

config_commands = [
    'int loopback 14',
    'ip add 10.14.1.1 255.255.255.0',
    'description [Vinicius Accioly]\'s loopback'
    ]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))
config_commands = [
    'int loopback 16',
    'ip add 10.16.1.1 255.255.255.0',
    'description [Vinicius Accioly]\'s loopback'
    ]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))
=======

sshCli = ConnectHandler(
device_type = 'cisco_ios',
host = '192.168.122.100',
port = 22,
username = 'cisco',
password = 'cisco123!'
)

output = sshCli.send_command("sh ip int br")
print(output)
>>>>>>> d8fe467 (Pratica Cisco)
