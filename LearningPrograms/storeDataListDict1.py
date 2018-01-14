def getIntInput(print_stmt):
    while True:
        try:
            val1 = int(input(print_stmt))
        except ValueError:
            print("Enter a valid number ")
            continue
        else:
            #print("It's a integer ")
            break
    return val1

items1 = {}
n = getIntInput("Enter a type of items size : ")
for i in range(n):
    type1 = input("Enter a item type : ")
    m = getIntInput("Enter a number of items in above type : ")
    l1 = []
    for j in range(m):
        ite = input("Enter a items : ")
        l1.append(ite)
    items1[type1] = l1
print(items1)
'''
search = input("Enter a item type to be search : ")
item_types = items1.keys()
print(item_types.__sizeof__())
'''
