class Mathemetics:
    x=1
    @staticmethod
    def AddNumbers(x,y):
        return x+y

    def SubNumbers(self,x=1,y=5):
        return x-y

#Mathemetics.AddNumbers = staticmethod(Mathemetics.AddNumbers)
Ma = Mathemetics()
print(Ma.AddNumbers(5,4))
print(Ma.SubNumbers(19,100))
print("The sum of number : ",Mathemetics.AddNumbers(5,6))
print("The sum of number : ",Mathemetics.AddNumbers(6,6))

class Count_Check:
    def countMethod():
        count = 0
        count += 1
        return count
Count_Check.countMethod = staticmethod(Count_Check.countMethod)
Count_Check_obj = Count_Check()
print("Iteration 1 : ",Count_Check_obj.countMethod())
print("Iteration 2 : ",Count_Check_obj.countMethod())

class A:
    message = 'Class message'
    @classmethod
    def c_foo(cls):
        print(cls.message)

    def foo(self, msg):
        self.message = msg
        print(self.message)

    def __str__(self):
        return self.message

a = A()
a.foo('instance call')
#A.foo('self',"Foo message")
a.c_foo()
