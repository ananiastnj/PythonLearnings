stud = {}
n = int(input("Enter a size of studtent dict : "))
for i in range(n):
    l1 = []
    stud_name = input("Enter a student name : ")
    age = input("Enter a age : ")
    city = input("Enter a city : ")
    l1.append(age)
    l1.append(city)
    stud[stud_name] = l1
#print(stud)
search = input("Enter a search name : ")
#print(stud[search])
stud_names = stud.keys()
#print(stud_names)
if search in stud_names:
    l_v = stud[search]
    print("Student name : ",search)
    print(search, " age is : ",l_v[0])
    print(search, " city is : ",l_v[1])
else:
    print(search, " name is not in the list")



