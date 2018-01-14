a = "Antony"
b = "Ananias"
print(set(a))
print(set(b))
c = list(zip(a,b))
print("c : ", c)
d = list(zip(c,b))
print("d : ", d)
e = list(zip(d,c))
print("e : ",e)
print(tuple(zip(a,b)))
print(a,b)