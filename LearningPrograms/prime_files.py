dict1={}
with open("prime_out","w+") as file1:
    for num in range(901,1001):
        for i in range(2, num):
            if((num%i) == 0):
                file1.write("{} is {} times in {} so its not a prime number\n".format(num,i,num//i))
                break
        else:
            print(num, " is a prime number")

l1 = []
with open("prime_out","r") as file1:
    #for line in file1.readlines():
        #l1.append(line.split(" ")[2])
    l1 = [int(line.split(" ")[2]) for line in file1.readlines()]
print(l1)
m = int(l1[0])
print(" m : ",m)
for i in l1[1:]:
    if(int(m) < int(i)):
        m = i
print("Max of l1 : ", m)
print("Max of l1 : ", max(l1))

'''for num in range(900,1000):

    for i in range(2,num):
        if((num%i) == 0):
            print(num," is ", i ," times in ", num//i, " So its not a prime number")
            break
    else:
        print(num, " is a prime number")
'''