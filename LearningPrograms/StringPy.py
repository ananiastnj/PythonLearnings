name = "Antony Ananias "
print(name)
print(name[0])
print(name[2:5])
print(name[2:])
print(name * 5)
print(name + name)
print(name, "o")

print("name : ",name[:-1])
print(len(name))

count=0
for i in name:
    count+=1
print("Length : ",count)

#a=a+b-(b=a)
a,b = 10, 5
print("a and b",a," and ",b)
a,b = b,a
print("a and b",a," and ",b)

str = "this is string example....wow!!!"
print (str.split( ))
print (str.split('i',2))
print (str.split('w'))

items = [x for x in input("Enter a strings with comma : ").split(',')]
print(items.sort())