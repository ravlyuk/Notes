def foo():
    return 1


def monkey_patch():
    return 10


foo = monkey_patch
