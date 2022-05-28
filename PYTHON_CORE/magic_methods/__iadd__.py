class A:
    def __init__(self, x: int):
        self.x = x

    def __iadd__(self, other):
        self.x += other.x
        return self

    def __str__(self):
        return str(self.x)


obj1, obj2 = A(10), A(20)

print(obj1)

obj1 += obj2

print(obj1)
