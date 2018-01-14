import re
str1 = "I am mac address : cd:01:34:21:12:10"
sea1 = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', str1, re.I).group()
print(sea1)

#import re
s = "http://[ipaddress]/SaveData/127.0.0.1/00-0C-F1-56-98-AD/"
s1 = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', s, re.I).group()
print(s1)