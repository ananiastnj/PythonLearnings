'''
def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". Good morning!")

def add1():
    a = 10
    b = 5
    sum = a + b
    print("Total of two numbers : ",a,"+",b,"=",sum)

def add_v(a,b):
    print("Total of two numbers : ", a, "+", b, "=", (a+b))

def add_v2(a,b):
    return a+b

add1()
add_v(10,9)
add_v(8,5)

print(add_v2(7,5))
sum = add_v2(10,20)
print(sum)

'''
def val1():
    i=15
    print("inside fun x : ", i)

val1()
i=20
print("Ouside fun i : ", i)
x=10
print("Ouside fun x : ", x)
val1()

