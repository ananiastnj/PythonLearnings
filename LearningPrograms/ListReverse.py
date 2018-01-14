l1 = [5,6,7,12,90]
l1.reverse()
print(l1)
l2 = []
for i in range(len(l1)-1,-1,-1):
    #print(i)
    print(l1[i])
    l2.append(l1[i])
print(l2)
