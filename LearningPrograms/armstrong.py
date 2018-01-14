n = int(input("Enter a number : "))
sum1 = 0
i = n
while(n>0):
    r = n%10
    print("r : ",r)
    n = n//10
    print("n : ",n)
    sum1 = (r*r*r)+sum1
    print("sum1 : ",sum1)

if(i==sum1):
    print(i," is a armstrong number")
else:
    print(i," is not a armstrong number")
