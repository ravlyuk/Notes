class A:
    def __init__(self, x: int):
        self.x = x

    def __sub__(self, other):
        new = A(self.x)
        new.x -= other.x
        return new

    def __str__(self):
        return str(self.x)


obj1, obj2 = A(10), A(20)

print(obj1 - obj2)
