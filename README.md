# There are two parts of this project. 
# MAC Changer for Kali-Linux and Random Password Generator for any kind of OS platform.
---
## About
### Basic scripts written by python to automate basic security processes.

### What is MAC Address?<br>A Media Access Control address (MAC address) is a hardware identifier that uniquely identifies each device on a network.[^1]

### What is IP address?</b><br>IP controls how devices on the internet communicate and defines the behavior of internet router.[^2]

### Key differences between MAC Address and IP Address:<br>The main difference between MAC and IP address is that MAC Address is used to ensure the physical address of the computer. It uniquely identifies the devices on a network. While IP addresses are used to uniquely identifies the connection of the network with that device takes part in a network.[^3]

### Why is MAC changer?<br>MAC address spoofing is used to bypass security measures by allowing an attacker to impersonate a legitimate host device, usually for the purpose of collecting network traffic.[^4]

### Why is Password generator?<br> If you don't want to use your gmail account while signing up to unknown web sites and also want to be secure in any way then password generator automatize random passwords just for you!
---
## Executing MAC Changer script

### You might want to use Kali Linux on Virtual Machine to execute MAC Changer script properly.
### You should execute the following code "python First_Part_Of_Project.py --interface eth0 --mac xx:xx:xx:xx:xx:xx" on terminal window.<br> x must be only 12 hexadecimal digits(0 to 9, a to f).
### For example, I want to change my MAC Address as "00:11:22:33:44:55" thus I have to write in the code that is beloww<br> 
### python First_Part_Of_Project.py --interface eth0 --mac 00:11:22:33:44:55

[^1]: Rebekah Taylor, 5/13/21, https://bluecatnetworks.com/blog/mac-address-vs-ip-address-whats-the-difference/
[^2]: John Burke, 6/21, https://www.techtarget.com/searchnetworking/answer/What-is-the-difference-between-an-IP-address-and-a-physical-address
[^3]: 5/31/22, https://www.geeksforgeeks.org/difference-between-mac-address-and-ip-address/
[^4]: 10/23/20, https://itexamanswers.net/question/why-would-an-attacker-want-to-spoof-a-mac-address
