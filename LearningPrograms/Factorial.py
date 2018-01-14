def fact(x):
    #print("X Value : ",x)
    if x==0:
        return 1
    else:
        #print(x," * ",x-1)
        return x*fact(x-1)
x=int(input("Enter a number : "))
print(fact(x))
