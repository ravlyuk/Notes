class SuperList:
    def __init__(self, data=()):
        self.data = list(data)

    def __str__(self):
        return f'SuperList: {self.data}'

    def __setitem__(self, key, value):
        self.data[key] = value


obj = SuperList([1, 2, 3, 4, 5])
obj[0] = True

print(obj)
