n =int(input("Enter a length of list : "))
l1 = []
for i in range(n):
    l1.append(input("Enter a value : "))
print("List : ", l1)
for i in range(n):
    print("I value : ", i)
    for j in range(1,n-i):
        print("J Value : ", j)
        print("l1[", j - 1, "] > l1[", j, "] : ", l1[j-1], " > ", l1[j])
        if l1[j-1] > l1[j]:
            print("Condition True - Swap happen")
            l1[j-1], l1[j] = l1[j], l1[j-1]
print("Sorterd list : ",l1)
