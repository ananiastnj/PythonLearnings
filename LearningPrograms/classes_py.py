class Human(object):
    species = "H Sapiens"
    def __init__(self,name):
        self.name = name
        self.age = 5

    def say(self, msg):
        print("Name and msg ",self.name, msg)

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "***** GRUNT ***** "

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age

i = Human(name = "Ant")
print("Calling say : ",i.say("Hi"))
print("Calling get_species : ",i.get_species())
print(Human.grunt())
i.age = 27
print("i.age : ",i.age)
del i.age
#print(i.age) #-its shows "AttributeError"