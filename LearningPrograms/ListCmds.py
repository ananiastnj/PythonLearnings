lst1 = ["anto" , "anan" , 24, "apr", 24, 1990, 27]
lst2 = [1, 2, 3, 4, 5]
lst3 = ["a", "b", 'c', 'd']
tup1 = (10, 20, "Anto", "Anan")
'''print("Accessing Value in List : ", lst2[4])
print(lst3[1:3])
print("***** Built in Functions in List *****")
print("1. cmp(lst1,lst2) - Not available in Python 3")
print("2. len(lst1) - returns the total length of the list \nex: lst1 length", lst1 , "\n List Length : ", len(lst1))
print("3. max(lst1) - returns the maximum value from the list \nex: lst2 max value : ", max(lst2))
print("4. min(lst1) - returns the minimun value from the list \nex: lst2 min value : ", min(lst2))
print("5. list(seq) - converts tuple into a list \n ex : tup1 convert as list : ", tup1 , "\nList value : ", list(tup1))
'''
print("***** Built in Methods in List *****")
print("1. list.append(obj) - append the object in the list : ", lst1.append(90), lst1)
print("2. list.count(obj) - returns the count of the object in the list : ", lst1.count(24))
print("3. list.extend(seq) - append the contents of seq to list : ", lst1.extend(tup1), lst1)
print("4. list.index(obj) -  returns the lowest index of the obj from the list : ", lst1.index("Anto"))
print("5. list.insert(index, obj) - insert the value in the list : ",lst1.insert(2,"Susee"),lst1)
print("6. list.pop(obj=list-1) - removes the element from the last in the list : ", lst1.pop(4),lst1, lst1.pop(), lst1)
print("7. list.remove(obj) -  removes obj from the list : ", lst1.remove(24), lst1)
print("8. list.reverse() - reverses the object in the list : ", lst1.reverse(), lst1)
print("9. list.sort() - Sorts the object in the list : ", lst2.sort(),lst2)

#print("10. List sort with different datattype : ", lst1.sort())



