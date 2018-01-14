import pandas as pd

#Create a DataFrame from List of Dicts
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
#print(df)

df = pd.DataFrame(data, index=['first', 'second'])
#print(df)

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])

#print(df1)
#print(df2)

d = {'one' : pd.Series([1, 2, 3], index=['raa', 'b', 'c']),
'two' : pd.Series([1, 2, 3, 4], index=['10', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
#print(df)

d = {'one' : pd.Series([1, "A2", 3], index=['a', 'b', 'c']),
'two' : pd.Series([1, 2, 3, "Ant"], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
#print(df['one'])

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
# Adding a new column to an existing DataFrame object with column label by passing new series
print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print("Adding a new column using the existing columns in DataFrame:")
df['four']=df['two']+df['three']
print(df)
