class Person():
    def __init__(self,first, last):
        self.first = first
        self.last = last

    def Name(self):
        return self.first+ " "+ self.last

class Employee(Person):
    def __init__(self, first, last, staffnum):
        super().__init__(first,last)
        self.staffnum = staffnum

    def GetEmployee(self):
        return self.Name()+ ", "+ self.staffnum

p1 = Person("Antony","Ananias")
e1 = Employee("Jeya","Susee","557")

print(p1.Name())
print(e1.Name())
print(e1.GetEmployee())
