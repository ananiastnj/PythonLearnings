class static_class:
    x = "Class"

    @staticmethod
    def static_method(x):
        print("I am ",x)

    @classmethod
    def class_method(cls,x):
        cls.x = x
        print("I am ",cls.x)

    def normal_method(self,x):
        self.x = x
        print("I am ",self.x)

static_class.static_method("Static")
static_class.class_method("Function X")
static_class().normal_method("Normal Method")