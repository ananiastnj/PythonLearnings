in1 = int(input("Enter a number1 : "))
in2 = int(input("Enter a number2 : "))
min1 = lambda a, b: a if(a<b) else b
#if(a>b)
#min1 = min1(in1,in2)
qu = [i for i in range(2,min1(in1,in2)) if(in1%i==0 and in2%i==0) in1=in1//i in2=in2//i]
print(qu)
'''
for i in range(2,min1(in1,in2)):
    if(in1%i==0 and in2%i==0):
       qu.append(i)
       in1 = in1//i
       in2 = in2//i
qu.extend([in1,in2])
'''
lcm = 1
#lcm = [lcm * i for i in qu]
for i in qu:
    lcm *= i
print("LCM : ",lcm)

