import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("Shape rows and cols ",a.shape)

a=np.array([[1,2,3],[4,5,6]])
a.shape=(3,2)
print("Change the values 2,3 to 3, 2:\n", a)

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)

a = np.arange(24)
print(a)

a.ndim
# now reshape it
b = a.reshape(2,4,3)
print(b)

#This array attribute returns the length of each element of array in bytes.
x = np.array([1,2,3,4,5], dtype=np.int8)
print(x.itemsize)

x = np.array([1,2,3,4,5], dtype=np.float32)
print(x.itemsize)

x = np.array([1,2,3,4,5])
print(x.flags)