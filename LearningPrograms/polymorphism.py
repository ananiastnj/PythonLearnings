class bear():
    def sound(self):
        print("Gorrrr")

class dog():
    def sound(self):
        print("Bow Bow")

def makeSound(animaltype):
    animaltype.sound()

makeSound(dog())
makeSound(bear())

list1 = [1,2,3,4]
str1 = str(list1)
print(str1)
print(type(str1))
