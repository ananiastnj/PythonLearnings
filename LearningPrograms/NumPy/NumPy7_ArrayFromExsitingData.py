import numpy as np
x = [1,2,3]
a = np.asarray(x)
print(a)

a = np.asarray(x, dtype=float)
print(a)

x = (1,2,3)
a = np.asarray(x)
print(a)

x = [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)
'''
s = 'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)
'''
list1 = range(5)
print(list(list1))

it = iter(list1)
# use iterator to create ndarray
x = np.fromiter(it, dtype=float)
print(x)