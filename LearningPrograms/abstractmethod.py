from abc import ABC, abstractmethod
class Foo:
    def __getitem__(self, item):
        print("Items : ",item)
    def __len__(self):
        print("Length function")
    def get_iter(self):
        return iter(self)

class myABC(ABC):

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iter(self):
        return self.__iter__()

    @classmethod
    def __subclasscheck__(self, cls, C):
        if cls is myABC:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
            return NotImplemented
myABC.register(Foo)
myABC.register(tuple)
assert issubclass(tuple, myABC)
assert isinstance((), myABC)
print(isinstance((),myABC))
print(issubclass(tuple, myABC))