import re
s = open("output1.txt",'r')
print(s)
str1 = s.readlines()
print(str1)
d = {}
for i in str1:
    n = re.search(r'(.*) Image : (\d).*',i)
    print(n)
    print(n.group())
    if n:
        x=re.match(r'(.*) Image : \d.\d.\d{0,3}\.\d',n.group())
        if x:
            a=x.group().split(":")
            d[a[0]] = a[1]
print(d)