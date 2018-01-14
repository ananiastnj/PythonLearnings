#Identify 3rd largest number from list without sorting
list1=[10,24,45,34,98,67,57]
if (list1[0]>list1[1])and list1[0]>list1[2]:
    m1 = list1[0]
    if(list1[1]>list1[2]):
        m2,m3=list1[1],list1[2]
    else:
        m2,m3=list1[2],list1[1]
elif(list1[1]>list1[0]) and (list1[1]>list1[2]):
    m1=list1[1]
    if(list1[0]>list1[2]):
        m2,m3=list1[0],list1[2]
    else:
        m2,m3=list1[2],list1[0]
else:
    m1=list1[2]
    if(list1[0]>list1[1]):
        m2,m3=list1[0],list1[1]
    else:
        m2,m3=list1[1],list1[0]
print("Largest number is : ",m1,"2nd largest number is : ",m2,"3rd largest number is : ",m3)
for i in list1[3:]:
    if i>m3 and i>m2 and i>m1:
        m1,m2,m3=i,m2,m3
    elif i>m3 and i>m2:
        m2,m3=i,m2
    elif i>m3:
        m3=i
    print("Largest number is : ", m1, "2nd largest number is : ", m2, "3rd largest number is : ", m3)
print("List of values : ",list1)
print("Largest number is : ",m1,"2nd largest number is : ",m2,"3rd largest number is : ",m3)

