class Foo:
    def __init__(self):
        self._privateField = 4
        print(self._privateField)


foo = Foo()
x = foo._privateField
print(x)
