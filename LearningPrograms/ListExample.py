'''odd = [1, 9]
odd.insert(1,[3,5])
print(odd)
#[1, 3, 9]
odd[2:3] = [5, 7, 11]
print(odd)
#[1, 3, 5, 7, 9]
'''
import sys
while(True):
    try:
        x = int(input("Enter an integer: "))
        r = 1/x
        break
    except:
        #print("Oops!",sys.exc_info()[0],"occured.")
        print("Zero not accept, Please try again.")

print()
print("The reciprocal of",x,"is",r)
