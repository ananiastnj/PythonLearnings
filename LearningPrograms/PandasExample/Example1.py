import pandas as pd
s = pd.Series()
#print(s)

#import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
#print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s= pd.Series(data)
#print(s)

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
#retrieve the first element
print(s[0])
print(s)
#retrieve the first three element
print(s[:3])
#retrieve the last three element
print(s[-3:])
#based on our index we given
print(s['a'])
#retrieve multiple elements
print(s[['a','c','d']])

