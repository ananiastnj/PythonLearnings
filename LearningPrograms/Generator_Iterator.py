'''for i in [1,2,3,4]: print(i)
for c in "Antony": print(c)
for d in {"x" : 1, "y" : 2}: print(d)
for line in open("Test.txt"): print(line)
'''
''' # Example 1
x = iter([1,2,3,4])
print(x)
print(x.__next__())
print(x.__next__())
'''
'''
#Example 2 : Iterator 
class yrange:
    def __init__(self,n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()

y = yrange(3)
print(y.__next__())
print(list(yrange(5)))
print(sum(yrange(5)))
print(sum({2:1 , 7:2}))
'''
#Generator
def grange(n):
    i=0
    while i < n:
        yield i
        i += 1

g = grange(3)
print(g)
print(g.__next__())
print(g.__next__())

a = (x*x for x in range(10))
print(a)
print(a.__next__())
print(sum(a))




