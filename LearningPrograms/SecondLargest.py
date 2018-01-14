#Identify second largest number with sorting
'''a=[]
n=int(input("Enter n value : "))
for i in range(1,n+1):
    b=int(input("Enter a number : "))
    a.append(b)
print("numbers : ",a)
a.sort()
print("from", a ,"Second largest number is : ",a[n-2])
'''
#Identify second largest number without sorting
#Method1
list1=[50,23,34,52.0,57,34,98,10,134]
print("list of values : ")
print("Maximum of list ",max(list1))
list1.remove(max(list1))
print("Second maximum of list : ",max(list1))

#Method 2
list1=[50,23,34,52.0,57,34,98,10,134]
if list1[0]>list1[1]:
    m, m1 = list1[0],list1[1]
    print("m is : ",m,"m1 is : ",m1)
else:
    m, m1 = list1[1],list[0]
    print("m is : ", m, "m1 is : ", m1)
count = 0
print("Values : ",list1)
for i in list1[2:]:
    count = count+1
    print("iteration #",count," i is : ",i," m is : ",m," m1 is : ", m1 )
    if i > m1 :
        if i > m:
            print(m1,m)
            m1,m=m,i
            print(m1,m)
        else:
            print(m1)
            m1 = i
            print(m1)
print("Largest number : ",m)
print("Second Largest number : ",m1)

#Method 3
l1 = [5,12,3,4,10,15]
m1, m2 = l1[0], l1[1]
if m1 < m2 :
    m1, m2 = l1[1],l1[0]
for i in range(2,len(l1)):
    if (m1 < l1[i]) and (m2 < l1[i]):
        m1, m2 = l1[i], m1
    elif (m2 < l1[i]):
        m2 = l1[i]
print("Large  : ",m1)
print("Sec Large : ",m2)
print(5**3)

