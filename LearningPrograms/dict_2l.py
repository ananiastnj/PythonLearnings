l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
dict1 = {}; #dict1 = dict1.fromkeys(l1)
print(len(dict1))
for i in range(len(l1)):
    dict1[l1[i]] = l2[i]
print(dict1)