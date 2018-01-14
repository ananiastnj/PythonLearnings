'''
************ DICTIONARY **************
 -> Each key separated from values by :
 -> Each item separated by commas
 -> Seq of items in the { 1 : "One", "Two" : 2, "Three" : 3}
 -> Items are Key and Value pair
 -> You can create a empty Dictionary {} 
 -> You can access a value using a Key

 Accessing a Values in Dictionary 

 dict1 = {"name " : "Ant", "Age" : 27}
  1. dict["age"] - returns the value of age - 27 
 2. 
 i)del dict1 - Delete the dict1 completely
 ii) dict1.clear() - Clears the complete dictionary values
 iii) del dict1["Age"] - Delete the age value from the dictionary
3.
 -> Keys are unique in the sequence while values may not be. 
 -> Keys should be immutable data type such as "Strings","Numbers" and "Tuples"

Built-in functions 
1. cmp(dict1,dict2) - no longer in the Python 3
2. len(dict1) -  Returns the length of the Dictionary
3. str(dict1) - Produces the printable string representation of the dictionary
Ex: Str(dict1) => {"name" : "Ant", "Age" : 27}
4. type(variable) - returns the type of the passed variable. if passed variable is in the dictionary then it would return the dictionary type
Ex : type(dict1) => type 'Dict'

Built-in Methods
1. dict1.clear() - Removes all elements of dictionary
2. dict2 = dict1.copy() - Returns the shallow copy of the dictionary
3. dict1.fromkeys(seq, Values) - Create a new dictionary with keys from seq and values set to value.
4. dict.get(key, default=None) - For key, returns value or default if key not in dictionary.
5 dict.has_key(key) - Removed, use the in operation instead.
6 dict.items() - Returns a list of dict's (key, value) tuple pairs.
7 dict.keys() - Returns list of dictionary dict's keys.
8 dict.setdefault(key, default=None) - Similar to get(), but will set dict[key]=default if key is not already in dict.
9 dict.update(dict2) - Adds dictionary dict2's key-values pairs to dict.
10 dict.values() - Returns list of dictionary dict's values.
 



'''
seq = ['name', 'age', 'sex']
dict = dict.fromkeys(seq)
print ("New Dictionary : %s" % str(dict))
dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" % str(dict))