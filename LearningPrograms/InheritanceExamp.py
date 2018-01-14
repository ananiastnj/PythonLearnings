class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling Parent Constructor")

    def getAttr(self):
        print("Parent Attribute : ", Parent.parentAttr)

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def ParentMethod(self):
        print("Printing parent method")

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

c = Child()
c.childMethod()
c.ParentMethod()
c.setAttr(2000)
c.getAttr()
