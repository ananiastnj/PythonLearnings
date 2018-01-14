
'''def FindDuplicates(in_list):
    unique = set(in_list)
    for each in unique:
        count = in_list.count(each)
        if count > 1:
            print 'There are duplicates in this list'

list1 = [1, 2, 3, 5, 7, 8, 1, 2, 3, 7]
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list1.count(list1[i])
print(dict1)

dict2={1:1,1:2}
print(dict2[1])
'''
l1 = ["name", "age", "qual"]
dict1 = dict1.fromkeys( l1, "")
print(dict1)