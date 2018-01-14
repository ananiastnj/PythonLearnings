x = 5
print('x+1')
print(eval('x+1'))
from math import sqrt
print(eval('sqrt(5)'))
print('sqrt(5) : ',sqrt(5))
print(eval('sqrt(5)',{'__builtin__':None},{'x':x, 'sqrt':sqrt}))
