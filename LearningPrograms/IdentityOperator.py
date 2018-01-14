print("***** Identity Operater *****")
a=10
b=20
if (a is b):
    print(a,"is ", b)
else:
    print(a,"is not", b)

if(a is not b):
    print(a, "is not",b)
else:
    print(a," is ", b)

print("ID")
print("id of a", id(a))
print("id of b", id(b))
c=10
print("id of c", id(c))
print("id of 10", id(10))

print("***** Thank You *****")