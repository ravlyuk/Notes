from time import sleep
from functools import lru_cache


@lru_cache
def some_logic(*args, **kwargs):
    sleep(1)
    return True


some_logic(1)
some_logic(1)
some_logic(1)
some_logic(1)
some_logic(1)
print("Програма завершилась!")
