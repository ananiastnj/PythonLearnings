print("Decision making")
print("age : ");age = input()
if(int(age) <= 17):
    print(" School boy")
elif(int(age) >= 18 and int(age) <= 23):
    print("College boy")
else:
    print("Grown man")

print("year : ");
year = input()
leap = int(year) % 4
if(leap == 0):
    print("Leap year")
else:
    print("Not leap year")

print("*** THANK YOU ***")