
with open("ikyaQ.csv","r") as file1:
    file1_list = file1.readlines()
li1 = []
print(file1_list)
for i in file1_list:
    li1.append(i.split("\n")[0])
d1 = {}
print(li1)
li2 = []
for i in li1:
    li2.append(i.split(","))
    #d1[i[0]] = i[2]
print(li2)
for i in li2:
    li3 = list(d1.keys())
    print(li3)
    if k in li3:
        l4 = d1[k]
        l4.append
        d1[k] =
    else:
        d1[i[0]] = i[1]

print(d1)