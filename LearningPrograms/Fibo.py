def fib(n):
    result=[0]
    a,b=0,1
    while b<n:
        a,b = b,a+b
        result.append(a)
    #print(result)
    return result
