import calendar
import time
#cal = calendar.mdays()
#print(cal)

def printant(a,*b):
    print("Output : ",a)
    for i in b:
        print("i ", i)

printant(10)
printant(4,5,3,2)

def sum(a,b): return a+b
print("sum : ",sum(10,20))

a=10
b=20
sum=a+b

sum1 = lambda a,b : a+b
print("Sums : ",sum1(6,7))


def minusas(a,b):
    minus1 = a-b
    print(minus1)

print(minusas(a,b))
print(minus1)
