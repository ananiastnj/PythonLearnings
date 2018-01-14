'''str1 = input("Enter a comma sequence string : ")
#print(str1)
str1 = str1.split(",")
str1.sort()
str1 = str(str1)
print(str1)
print(type(str1))
str2 = ""
print(type(str2))
for i in str1:
    str2 = str2 + i
print(str2)
#L = ['L','O','L']
#makeitastring = ','.join(map(str, L))
#print(makeitastring)
#anto,anan,susee,bala,veera
'''
items = input("Input comma separated sequence of words : ")
#words = [word for word in items.split(",")]
words = items.split(",")
print(words)
print(",".join(words))
print(",".join(sorted(words)))
print(",".join(sorted(list(words))))
print(words)
print(",".join(sorted(list(set(words)))))
print(words)