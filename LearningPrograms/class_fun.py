class xyz:
    def add(self, x):
        self.x = x
        return 10+self.x

    #print(add(5))

s = xyz
print(xyz().add(5))
