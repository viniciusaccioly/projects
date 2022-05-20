import napalm
import json

# Use the ap propriate net work driver to connect to the device:
driver=napalm.get_network_driver("ios")

# Connect :
device = driver (
hostname="192.168.122.101",
username="vinicius",
password="melo",
optional_args={"port": 22},
)


print ( " Opening ... " )
device.open()
output = device.get_interfaces()
#output_dict = json.loads(output)
#print (output_dict)
print ("Uptime: " , output)