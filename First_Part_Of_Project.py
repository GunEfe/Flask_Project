import subprocess
import optparse
import re

# Code a new option for MAC_changer with 'optparse' library
def get_user_input():
	parse_object = optparse.OptionParser()
	parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
	parse_object.add_option("-m","--mac",dest="mac_address",help="new mac_address")

	return parse_object.parse_args()
# Request the new MAC Address 
# Changing the MAC address with call function
def change_mac_address(user_interface,user_mac_address):
	subprocess.call(["ifconfig",user_interface,"down"])
	subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
	subprocess.call(["ifconfig",user_interface,"up"])
# Controling the MAC Address    
def control_new_mac(interface):

	ifconfig = subprocess.check_output(["ifconfig",interface])
	# Catch tinghe pattern while using regex
	# "\w" means any word character which can be seen in any MAC address
	new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

	if new_mac:
		return new_mac.group(0)
	else:
		return None

print("MyMacChanger started!")
(user_input,arguments) = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
	print("Success!")
else:
	print("Error")