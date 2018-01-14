x = [x * x for x in range(1,11)]
print(x)
#l1 = list(range(1,11))
#print(l1)
y = list(map(lambda x,y: x*y,list(range(1,11)),list(range(0,5))))
print(y)

def sq(x):
    return x*x


sq1 = list(map(sq, list(range(1, 11))))
print("Sq1 : ",sq1)
f = lambda z: z*z
print(f(10))

c = lambda a, b: a+b
print(c(20,9))

fib = [0,1,1,2,3,5,8,13,21,34,55]
res = filter(lambda even: even%2,fib)
print(list(res))

res1 = list(filter(lambda even: even%2 == 0, list(range(1,11))))
print(res1)

#res12 = list(reduce(lambda x, y: x+y, range(1,101)))
#print(res12)
