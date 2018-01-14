'''Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters'''

class InputOut(object):
    def __init__(self):
        print("Program begins")

    def getString(self):
        self.str=input("Enter a string : ")

    def printString(self):
        print(self.str.lower())

    def add(self,x,y):
        return x+y

    def sub(self,x,y):
        return x-y

def anto():
    print("Antony Ananias")

strobj = InputOut()
strobj.getString()
strobj.printString()
anto()