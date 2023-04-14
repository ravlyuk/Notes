# SIMPLE DECORATOR

def decorator(func):
    def wrapper(*args, **kwargs):
        print("wrapper")
        return func()

    return wrapper


@decorator
def some_function():
    print("Simple decorator.")


some_function()

print()


# DECORATOR WITH ARGUMENTS

def decorator_func(x, y):
    def inner(func):
        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks Summation of values - {}".format(x + y))

            func(*args, **kwargs)

        return wrapper

    return inner


@decorator_func(12, 15)
def my_fun(*args):
    for ele in args:
        print(ele)


# another way of using decorators
my_fun('Decorator with arguments.')
