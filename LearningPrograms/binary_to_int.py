'''bin1 = input("Enter the , sequence binary value : ")
l1 = bin1.split(",")
#print(l1)
for i in l1:
    #print(i)
    bin_v = bin(i)
    con_v = int(bin_v)
    if con_v%5 == 0:
        print(i)

#0100,0011,1010,1001
'''
items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p,1)
    print(x)
    if not x%5:
        items.append(p)
print(','.join(items))