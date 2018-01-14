'''# Method1
val1 = input("Enter a number : ")
if val1.isdigit():
    print("It's a number")
    int(val1)
else:
    print("It's not a number")
'''
# Method2 - This is best method to get the input
#val1 = int(input("Enter a number : "))
while True:
    try:
        val1 = int(input("Enter a number : "))
    except ValueError:
        print("Not an integer!")
        continue
    else:
        print("It's an integer ...!")
        break

