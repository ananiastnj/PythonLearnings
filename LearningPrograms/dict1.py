dict1 = {'a': 5, 'b':10,'c': 3}
dict2 = {'b': 10, 'e' : 34, 'c' : 7}
dict1_key = list(dict1.keys())
dict2_key = list(dict2.keys())
dict3 = {}
print(dict1)
print(dict2)
print(dict1_key)
print(dict2_key)
for i in dict1_key:
    for j in dict2_key:
        if(i == j):
            dict2[j] += dict1[i]
        dict3[j] = dict2[j]
    dict3_key=list(dict3.keys())
    if i not in dict3_key:
        dict3[i] = dict1[i]
print(dict3)

'''for i in range(len(dict1_key)):
    val1 = dict1[dict1_key[i]]
    for j in range(len(dict2_key)):
        val2 = dict2[dict2_key[j]]
        if(dict1_key[i]==dict2_key[j]):
            val = dict1[dict1_key[i]]+dict2[dict2_key[j]]
        dict3[dict2_key[j]] = val2
    dict3[dict1_key[i]] = val
'''