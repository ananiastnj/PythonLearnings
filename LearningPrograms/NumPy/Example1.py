import numpy as np
a=np.array([1,2,3])
print(a)
a = np.array([[1, 2], [3, 4]])
print(a)
a=np.array([1, 2, 3,4,5], ndmin=2)
print(a)
a = np.array([1, 2, 3], dtype=complex)
print(a)
dt = np.dtype([('age',np.int8)])
print(dt)
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a)
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a['age'])
student=np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
student=np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype=student)
print(a)
