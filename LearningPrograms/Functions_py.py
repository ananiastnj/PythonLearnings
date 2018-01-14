def add(x,y):
    print("x is {} and y is {}".format(x,y))
    return x+y

add(5,6)
add(y=6,x=5)

def varargs1(*args):
    return args
print(varargs1(1,2,3))

def kwargs1(**kwargs):
    print(kwargs)
    return kwargs
print(kwargs1(a=5,b=10))

def swap(x,y):
    return y,x
x,y = 5,6
print(x,y)
print(swap(x,y))
print(globals())
def x_num(x):
    #global x
    print(x)
print(x)
x_num(100)

def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_10 = create_adder(10)
print(add_10(3))

y = (lambda x : x > 2)(3)
print(y)
z = (lambda n1,n2: n1==n2) (5,10)
print(z)

sqrt = tuple([x*x for x in range(10)])
print(sqrt)

square1 = map((lambda x: x*x),(range(11)))
print("square1 : ",list(square1))

check = [x for x in range(20,10,-1) if x > 15]
print(check)