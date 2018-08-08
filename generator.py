# пример работы генератора
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2
		
for number in even_range(0, 10):
    print(number)
	
# Результат:
# 0
# 2
# 4
# 6
# 8


# работа генератора с добавляемым значением

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()
next(generator)
# 0
print('Accumulated: {}'.format(generator.send(1)))
# Got: 1
# Accumulated: 1
print('Accumulated: {}'.format(generator.send(1)))
# Got: 1
# Accumulated: 2
print('Accumulated: {}'.format(generator.send(1)))
# Got: 1
# Accumulated: 3