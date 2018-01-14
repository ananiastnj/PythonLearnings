l1 = []
n = int(input("Enter list length : "))
for i in range(n):
    l1.append(int(input("Enter a number : ")))
print(l1)

for i in l1[:]:
    print(" I : ", i)
    count = l1.count(i)
    print("Count : ",count)
    if count > 1 :
        del l1[]
print(l1)

'''
for i in range(n):
    for j in range(1,n-i):
        print("l1[", i, "] == [", j, "] : ",l1[i], "== ",l1[j])
        if l1[i] == l1[j]:
            l1.pop(j)
            print(l1)
'''

#Method 1
dict1={}
l2 = dict1.fromkeys(l1).keys()
print(l2)