import re
in_mac = input("Enter the MAC address : ") #aa:11:bb:22:33:cc
mo = re.match(r'^((([a-f0-9]{2}:){5})([a-f0-9]{2}))$',in_mac)
#print(mo.groups())
print(mo.group())
if mo:
    print(" Mac address is valid ")
else: print("Mac address is not valid")