class SuperList:
    def __init__(self, data=()):
        self.data = list(data)

    def __str__(self):
        return f'SuperList: {self.data}'

    def __getitem__(self, item):
        data = self.data[item]
        if isinstance(item, slice):
            return SuperList(data)
        elif item == 'all':
            return self.data

        return data


obj = SuperList([1, 2, 3, 4, 5])

print(obj[2])
