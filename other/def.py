# (одна звёздочка *)итерированный тип аргумента
def printer(*args):
    print(type(args))
    
    for argument in args:
        print(argument)

printer(1, 2, 3, 4, 5)


# (две звёздочки **)итерированный тип аргумента в виде словаря
def printer(**kwargs):
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value)) 
        
printer(a=10, b=11)


# map - применение итерации в функции
def squarify(a):
	return a ** 2

list( map( squarify, range(5) ) )
 

# filter - фильтрует аргументы
def is_positive(a):
	return a > 0

list( filter( is_positive, range( -2, 3 ) ) )


# lambda - анонимная функция
list(map(lambda x: x ** 2, range(5)))


# Списочное выражение
square_list = [number ** 2 for number in range(10)]
print(square_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Списочное выражение с условием
even_list = [ num for num in range(10) if num % 2 == 0 ]
print(even_list)
