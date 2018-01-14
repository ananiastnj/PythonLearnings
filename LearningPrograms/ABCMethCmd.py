'''
-> Abstract classes are classess that contain one or more abstract method but no implementations
-> Abstract method is declared but conatains no implementation.
-> Abstract class may not be instantiated and require subclasses to provide implementations for the abstract methods.

'''
from abc import ABC, abstractmethod
class AbsClassMethod(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class doAdd(AbsClassMethod):
    def do_something(self):
        return self.value + 24

class doMul(AbsClassMethod):
    def do_something(self):
        return self.value*2

x = doAdd(4)
y = doMul(4)
print(x.do_something())
print(y.do_something())

class inh1():
    def do_s(self, a, b):
        return a+b

class inh2(inh1):
    def do_s(self,a,b):
        return a*b

inh1_obj = inh1()
inh2_obj = inh2()
print(inh1_obj.do_s(5,6))
print(inh2_obj.do_s(5,6))
