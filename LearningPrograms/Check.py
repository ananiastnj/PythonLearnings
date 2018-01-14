lst=[10,6,98,99,34,54,7,8,4]
'''s1=lst[0]
for i in lst[1:]:
    if i<s1:
        s1=i
print("Smallest number : ",s1)
'''
if lst[0]<lst[1]:
    s1,s2=lst[0],lst[1]
else:
    s1,s2=lst[1],lst[0]

print("Smallest : ",s1, "2nd Smallest : ",s2)

for i in lst[2:]:  # i =lst[2]
    print("Small : ", s1, "2nd Small", s2, "i value : ", i)
    if i<s2 and i<s1:
        s1,s2=i,s1
    elif i<s2:
        s2=i

print("Small : ", s1, "2nd Small", s2)

