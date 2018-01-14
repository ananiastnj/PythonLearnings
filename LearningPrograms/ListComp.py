l1, l2 = [],[]
n = int(input("Enter a lenght of list1 : "))
m = int(input("Enter a length of list2 : "))
if n == m:
    for i in range(n):
        l1.append(input("Enter a value for List1 : "))
    for i in range(m):
        l2.append(input("Enter a value for List2 : "))
    print("List1 : ", l1)
    print("List2 : ", l2)
    #if len(l1) == len(l2):
    for i in range(len(l2)):
        if l1[i] == l2[i]:
            if i+1 == len(l2):
                print("List is same")
            continue
        else:
            print("List is not same")
            break

else: print("Both list length is different")