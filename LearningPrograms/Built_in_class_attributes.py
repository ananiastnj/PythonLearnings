#import InheritanceExamp
class Example1:
    str1 = "Antony"
    str2 = "Ananias"
    def print1(self,a,b):
        #print(type(Example1.str1))
        print("Print1 method")
        c = a+b
        return c
e = Example1()
print(e.print1(5,10))
print(e.__dict__)
print(e.__doc__)
print(e.__module__)
print(e.__class__)
print(e.__getattribute__)
print(e.__repr__())
print(e.__setattr__(Example1.str1,"Jeyasuseethra"),e.__setattr__(Example1.str2,"Ananias"))
#print(e.__getattribute__(Example1.str1),e.__getattribute__(Example1.str2))
#print(e.__delattr__(Example1.str2))
print(hasattr(e, Example1.str2))
print(getattr(e, Example1.str1),getattr(e, Example1.str2))