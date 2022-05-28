class Old:
    def get(self):
        return '123'


class New:
    def get(self):
        return 456


class Adapter:
    def get(self):
        return str(super(Adapter, self).get())


def main(obj):
    print(f'Result: {obj.get()}')


if __name__ == '__main__':
    res = New()
    main(res)
