class First():
    def sum(self):
        print("First Method")

class Second():
    def sum(self):
        print("Second Method")

class Third(First,Second):
    def third_method(self):
        print("Third Method")

t = Third()
t.third_method()
t.sum()
#t.first_method()