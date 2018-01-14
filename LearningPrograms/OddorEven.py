'''num = int(input("Enter a number : "))
if (num % 2) == 0: print(num, "is a even number")
else: print(num, " is a odd number")
'''
'''
#Fibonacci series 1, 2, 3, 5, 8,13
n = int(input("Enter a number : "))
f1, f2 = 0, 1
l1 = []
while f2 < n:
    f1, f2 = f2, f1 +f2
    l1.append(f1)
print(l1)
'''
'''
#Factorial
n = int(input("Enter a number : "))
fact = 1
for i in range(1,n+1):
    fact = i * fact
print("FACTORIAL : ", fact)
'''