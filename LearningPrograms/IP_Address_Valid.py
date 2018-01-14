import re
import ipaddress
ip_add = input("Enter a IP address : ")
'''
1. Lenght should not exceed 15 including a period
2. Should be 3 .
3. Value should not exceed 255
'''
#mo = re.match(r'^((\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}))$',ip_add)
mo1 = re.match(r'^((\d{1,3})\.){3}\d{1,3}$',ip_add)
print("Match onj : ", mo1.group())
#print("Match onj : ", mo1.groups())
#print("Match obj : ", mo.groups())
ip_split = mo1.group().split(".")
print(ip_split)
for i in ip_split:
    if int(i)>=0 and int(i)<=255:
        flags = 1
    else:
        flags = 0
        break
if flags==1:
    print("Ip Address is Valid IPv4 : ",ip_add)
else:
    print("IP address is not valid IPv4 : ",ip_add)