import timeit


def cube_cycle():
    for j in range(1000000):
        j ** 3


print(timeit.Timer(cube_cycle).repeat(number=10, repeat=3))
print(timeit.Timer(cube_cycle).repeat(number=1, repeat=5))
