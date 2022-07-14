class Foo:
    def __init__(self):
        self._privateField = 4
        self.__privateField2 = 10


foo = Foo()
print(foo._privateField)
print(foo._Foo__privateField2)
