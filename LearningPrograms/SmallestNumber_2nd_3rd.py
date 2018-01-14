list1=[10,78,98,99,34,54,7,8,4]
list1.sort()
print("Samllest number ",list1[0])
print("2nd smallest number",list1[1])
print("3rd smallest number is : ",list1[2])
#Without sorting 2nd smallest
lst=[10,45,3,7,8,9,100,10.3,2.3]
if lst[0]<lst[1]:
    s1,s2=lst[0],lst[1]
else:
    s1,s2=lst[1],lst[0]

for i in lst[2:]:
    if i<s2 and i<s1:
        s1,s2=i,s1
    elif i<s2:
        s2=i

print("list of values : ",lst)
print("Smallest nmuber : ",s1)
print("2nd smallest number is : ",s2)
#Without sorting smallest number
lst=[10,45,3,7,8,9,100,10.3,2.3]
s1=lst[0]
for i in lst[1:]:
    if i<s1:
        s1=i
print("Smallest number : ",s1)

#Without sorting 3rd smallest number
lst1=[10,45,3,7,8,9,100,10.3,2.3]
'''n=int(input("Enter n value list : "))
lst=[]
for i in n:
    lst[i]=int(input("Enter a number : "))
    lst
   '''

#Total 9 numbers
#First 3 number identified 1st,2nd, 3rd - conditions
#4-n values for loop - with
if lst[0]<lst[1] and lst[0]<lst[2]:
    s1=lst[0]
    if lst[1]<lst[2]:
        s2,s3=lst[1],lst[2]
    else:
        s2,s3=lst[2],lst[1]
elif lst[1]<lst[0] and lst[1]<lst[2]:
    s1=lst[1]
    if lst[0]<lst[2]:
        s2,s3=lst[0],lst[2]
    else:
        s2,s3=lst[2],lst[0]
else:
    s1=lst[2]
    if lst[0]<lst[1]:
        s2,s3=lst[0],lst[1]
    else:
        s2,s3=lst[1],lst[0]

print("Smallest number is : ",s1,"2nd smallest number is : ", s2,"3rd smallest number is : ",s3)
print(lst)
for i in lst[3:]:
    if i<s3 and i<s2 and i<s1:
        s1,s2,s3=i,s1,s2
    elif i<s3 and i<s2:
        s2,s3=i,s2
    elif i<s3:
        s3=i
    print("Smallest number is : ", s1, "2nd smallest number is : ", s2, "3rd smallest number is : ", s3)
print("List of values : ",lst)
print("Smallest number is : ",s1,"2nd smallest number is : ", s2,"3rd smallest number is : ",s3)