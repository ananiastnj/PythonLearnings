'''for num in range(500,600):

    for i in range(2,num):
        if((num%i) == 0):
            print(num," is ", i ," times in ", num//i, " So its not a prime number")
            break
    else:
        print(num, " is a prime number")
'''
'''num = 901
for i in range(2,num):
    if(num%i == 0):
        print(num, " is ", i, " times in ", num // i, " So its not a prime number")
        break
'''
k = 5
n = 5
str1 = "5 7 13 19 3"
l1 = str1.split(" ")
print(l1)
flag = 0
count = 0
for l in l1:
    num = int(l)
    for i in range(2, num):
        if ((num % i) == 0):
            #print(num, " is ", i, " times in ", num // i, " So its not a prime number")
            flag = 0
            break
        else:
            #print(num, " is a prime number")
            flag = 1
    if(flag == 1):
        #print("list contains prime number")
        count = 1
    else:
        print("list contains non prime number")
        break
if(count == 1):
