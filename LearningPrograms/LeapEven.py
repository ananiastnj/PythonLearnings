year1, number1 = input("Enter a year and number : ").split(",")
year1=int(year1)
number1=int(number1)
if(year1%4==0):
    print(year1," is a leap year")
else:
    print(year1," is not a leap year")

if(number1%2==0):
    print(number1," is even number")
else:
    print(number1," is odd number")

